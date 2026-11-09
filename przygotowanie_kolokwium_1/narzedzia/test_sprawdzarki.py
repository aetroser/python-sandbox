"""Testy samego narzędzia; nie zawierają rozwiązań zadań dla uczącego się.

Tematyka: rzetelność wyniku, limity i diagnostyka sprawdzarki.
Źródło: zasady oceny z opisu kolokwium; plik pomocniczy poza zakresem nauki.
Uruchom: python -m unittest discover -s przygotowanie_kolokwium_1/narzedzia -v
"""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import sprawdzarka as checker


class CheckerTests(unittest.TestCase):
    def test_grades(self):
        self.assertEqual([checker.grade(n) for n in range(6)],
                         ["2.0", "2.0", "2.0", "3.0", "4.0", "5.0"])

    def test_spaces_and_platform_newlines(self):
        self.assertEqual(checker.normalized("1  2\r\n3\t4\r\n"),
                         checker.normalized("1 2\n3 4"))

    def test_extra_blank_line_is_wrong(self):
        self.assertNotEqual(checker.normalized("1\n\n"), checker.normalized("1\n"))

    def test_line_structure_is_required(self):
        self.assertNotEqual(checker.normalized("1 2\n"), checker.normalized("1\n2\n"))

    def test_exact_numeric_format_is_required(self):
        self.assertNotEqual(checker.normalized("2.5\n"), checker.normalized("2.50\n"))

    def run_tiny(self, code, stdin="", timeout=2):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "program.py"
            path.write_text(code, encoding="utf-8")
            return checker.run_program(path, stdin, timeout)

    def test_utf8_and_input(self):
        reason, output, _ = self.run_tiny("print(input().upper())", "łódź\n")
        self.assertEqual(reason, "")
        self.assertEqual(output, "ŁÓDŹ\n")

    def test_exception(self):
        reason, _, errors = self.run_tiny("raise ValueError('test')")
        self.assertIn("kod zakończenia", reason)
        self.assertIn("ValueError", errors)

    def test_syntax_error(self):
        reason, _, errors = self.run_tiny("if:")
        self.assertIn("kod zakończenia", reason)
        self.assertIn("SyntaxError", errors)

    def test_timeout(self):
        reason, _, _ = self.run_tiny("while True: pass", timeout=0.15)
        self.assertEqual(reason, "przekroczony czas")

    def test_output_limit(self):
        reason, _, _ = self.run_tiny("print('x' * (2 * 1024 * 1024))")
        self.assertIn("limit wyjścia", reason)

    def test_nonzero_exit_is_failure_even_with_correct_output(self):
        reason, output, _ = self.run_tiny("print('OK'); raise SystemExit(1)")
        self.assertEqual(output, "OK\n")
        self.assertIn("kod zakończenia", reason)

    def run_fake_exam(self, completed, partial_failure=False, task=None, missing=False):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            tasks = {}
            for number in range(1, 6):
                tasks[str(number)] = [
                    {"name": "a", "stdin": "a\n", "stdout": "OK\n"},
                    {"name": "b", "stdin": "b\n", "stdout": "OK\n"},
                ]
                if not missing:
                    (folder / f"zad{number}.py").write_text("", encoding="utf-8")
            (folder / "testy.json").write_text(json.dumps({"exam": "TEST", "schema_version": 1, "tasks": tasks}), encoding="utf-8")

            def fake_run(path, stdin, timeout):
                number = int(path.stem[-1])
                good = number <= completed
                if partial_failure and number == 1 and stdin == "b\n":
                    good = False
                return "", "OK\n" if good else "ZLE\n", ""

            output = io.StringIO()
            with patch.object(checker, "run_program", side_effect=fake_run), contextlib.redirect_stdout(output):
                code = checker.main(folder, ["--task", str(task)] if task else [])
            return code, output.getvalue()

    def test_all_six_completion_counts(self):
        for n in range(6):
            with self.subTest(n=n):
                code, output = self.run_fake_exam(n)
                self.assertIn(f"Całe poprawne zadania: {n}/5", output)
                self.assertIn(f"Ocena treningowa: {checker.grade(n)}", output)
                self.assertEqual(code, 0 if n == 5 else 1)

    def test_partial_tests_do_not_count_as_full_task(self):
        _, output = self.run_fake_exam(5, partial_failure=True)
        self.assertIn("zad1: NIEZALICZONE — testy 1/2", output)
        self.assertIn("Całe poprawne zadania: 4/5", output)

    def test_single_task_does_not_issue_final_grade(self):
        code, output = self.run_fake_exam(5, task=3)
        self.assertEqual(code, 0)
        self.assertNotIn("Ocena treningowa:", output)

    def test_missing_files(self):
        code, output = self.run_fake_exam(5, missing=True)
        self.assertEqual(code, 1)
        self.assertIn("Całe poprawne zadania: 0/5", output)
        self.assertIn("brak pliku zad1.py", output)

    def test_incomplete_test_configuration_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "testy.json"
            path.write_text('{"schema_version":1,"tasks":{}}', encoding="utf-8")
            with self.assertRaises(ValueError):
                checker.load_tests(path)


if __name__ == "__main__":
    unittest.main()
