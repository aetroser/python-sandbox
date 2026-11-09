"""Wspólny silnik testerów kolokwiów A–D.

Tematyka: uruchamianie programów, porównywanie stdout i ocena całych zadań.
Narzędzie pomocnicze autora zestawu, poza zakresem materiału do nauczenia.
Python 3.10+, bez instalowania pakietów. Uruchamiaj lokalne sprawdz.py.
"""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time


MAX_OUTPUT_BYTES = 1024 * 1024


def normalized(text):
    """Zachowaj wiersze i tokeny; pomiń różnice w odstępach w obrębie wiersza."""
    return [line.split() for line in text.splitlines()]


def grade(completed):
    return {0: "2.0", 1: "2.0", 2: "2.0", 3: "3.0", 4: "4.0", 5: "5.0"}[completed]


def run_program(path, stdin, timeout):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        process = subprocess.Popen(
            [sys.executable, "-B", "-X", "utf8", str(path)],
            stdin=subprocess.PIPE,
            stdout=stdout,
            stderr=stderr,
            cwd=str(path.parent),
            env=env,
        )
        reason = ""
        start = time.monotonic()
        try:
            try:
                process.stdin.write(stdin.encode("utf-8"))
                process.stdin.close()
            except BrokenPipeError:
                pass
            while process.poll() is None:
                if time.monotonic() - start > timeout:
                    reason = "przekroczony czas"
                    break
                if max(os.fstat(stdout.fileno()).st_size, os.fstat(stderr.fileno()).st_size) > MAX_OUTPUT_BYTES:
                    reason = "przekroczony limit wyjścia 1 MiB"
                    break
                time.sleep(0.01)
        finally:
            if process.poll() is None:
                process.kill()
            process.wait()
        if max(os.fstat(stdout.fileno()).st_size, os.fstat(stderr.fileno()).st_size) > MAX_OUTPUT_BYTES:
            reason = "przekroczony limit wyjścia 1 MiB"
        stdout.seek(0)
        stderr.seek(0)
        try:
            output = stdout.read(MAX_OUTPUT_BYTES).decode("utf-8")
            errors = stderr.read(MAX_OUTPUT_BYTES).decode("utf-8")
        except UnicodeDecodeError:
            return "wyjście nie jest poprawnym UTF-8", "", ""
        if not reason and process.returncode != 0:
            reason = f"kod zakończenia {process.returncode}"
        return reason, output, errors


def load_tests(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or set(data.get("tasks", {})) != {"1", "2", "3", "4", "5"}:
        raise ValueError("oczekiwano wersji 1 i dokładnie pięciu zadań")
    for cases in data["tasks"].values():
        if not isinstance(cases, list) or not cases:
            raise ValueError("każde zadanie musi mieć co najmniej jeden test")
        for case in cases:
            if not all(isinstance(case.get(k), str) for k in ("name", "stdin", "stdout")):
                raise ValueError("test wymaga tekstowych pól name, stdin, stdout")
    return data


def main(exam_dir, argv=None):
    parser = argparse.ArgumentParser(description="Tester kolokwium: zadanie zalicza tylko komplet testów.")
    parser.add_argument("--solutions-dir", type=Path, default=exam_dir,
                        help="folder z zad1.py–zad5.py; domyślnie folder tego kolokwium")
    parser.add_argument("--task", type=int, choices=range(1, 6), help="sprawdź tylko jedno zadanie, bez oceny całego arkusza")
    parser.add_argument("--details", action="store_true", help="pokaż wszystkie nieudane przypadki zamiast pierwszego")
    parser.add_argument("--timeout", type=float, default=2.0, help="limit sekund na pojedynczy test (domyślnie 2)")
    args = parser.parse_args(argv)
    if not 0 < args.timeout <= 60:
        parser.error("--timeout musi należeć do (0,60]")
    solutions = args.solutions_dir.resolve()
    if not solutions.is_dir():
        parser.error(f"nie istnieje folder rozwiązań: {solutions}")
    try:
        data = load_tests(exam_dir / "testy.json")
    except (OSError, ValueError, TypeError) as exc:
        print(f"BŁĄD KONFIGURACJI TESTERA: {exc}")
        return 2
    print(f"Kolokwium {data['exam']} — testy wyjścia")
    selected = [args.task] if args.task else list(range(1, 6))
    completed = 0
    for number in selected:
        path = solutions / f"zad{number}.py"
        cases = data["tasks"][str(number)]
        if not path.is_file():
            print(f"zad{number}: NIEZALICZONE — brak pliku {path.name}")
            continue
        passed = 0
        failures = []
        for case in cases:
            try:
                reason, output, errors = run_program(path, case["stdin"], args.timeout)
            except OSError as exc:
                reason, output, errors = f"nie można uruchomić: {exc}", "", ""
            if not reason and normalized(output) != normalized(case["stdout"]):
                reason = "niezgodne wyjście"
            if reason:
                failures.append((case, reason, output, errors))
            else:
                passed += 1
        success = passed == len(cases)
        completed += success
        print(f"zad{number}: {'ZALICZONE' if success else 'NIEZALICZONE'} — testy {passed}/{len(cases)}")
        for case, reason, output, errors in failures if args.details else failures[:1]:
            print(f"  {case['name']}: {reason}")
            print(f"  wejście:     {case['stdin'][:2000]!r}")
            print(f"  oczekiwano:  {case['stdout'][:2000]!r}")
            print(f"  otrzymano:   {output[:2000]!r}")
            if errors:
                print(f"  stderr:      {errors[:2000]!r}")
    if args.task:
        print("Tryb jednego zadania — bez oceny całego kolokwium.")
    else:
        print(f"\nCałe poprawne zadania: {completed}/5")
        print(f"Ocena treningowa: {grade(completed)}")
        print("Wynik: " + ("ZALICZONE" if completed >= 3 else "NIEZALICZONE"))
        print("Ocena dotyczy tych testów; nie gwarantuje wyniku oficjalnego kolokwium.")
    return 0 if completed == len(selected) else 1
