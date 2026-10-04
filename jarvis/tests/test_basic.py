from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main


class JarvisBasicTest(unittest.TestCase):
    def test_entrypoint_imports_and_initializes(self) -> None:
        jarvis = main.Jarvis()
        self.assertEqual(jarvis.settings.app_name, "jarvis")
        self.assertTrue(hasattr(jarvis, "brain"))
        self.assertTrue(hasattr(jarvis, "planner"))
        self.assertTrue(hasattr(jarvis, "executor"))


if __name__ == "__main__":
    unittest.main()
