#!/usr/bin/env python3
"""Exercise the font wrapper with no live X connection."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Font(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.env = dict(os.environ, PATH=str(self.base))
        (self.base / 'awk').symlink_to(shutil.which('awk'))
        self.mock('dmenu', 'printf "%s\\n" "$@"; '
                  'while IFS= read -r line; do printf "%s\\n" "$line"; done; exit 3')
        self.mock('xrdb', 'printf "%s\\n" "${RESOURCES:-}"')

    def mock(self, name, body):
        path = self.base / name
        path.write_text('#!/bin/sh\n' + body + '\n')
        path.chmod(0o755)

    def run_menu(self, *args, resources=''):
        return subprocess.run(['/bin/sh', str(ROOT / 'dmenu-font'), *args],
                              env=dict(self.env, RESOURCES=resources), input='input item\n',
                              capture_output=True, text=True, timeout=5)

    def test_resource_preserves_arguments_and_stdin(self):
        r = self.run_menu('-p', 'A prompt', resources='dmenu.font:\tA Font:size=11')
        self.assertEqual(r.returncode, 3)
        self.assertEqual(r.stdout.splitlines(), ['-fn', 'A Font:size=11', '-p', 'A prompt', 'input item'])

    def test_explicit_font_wins(self):
        r = self.run_menu('-fn', 'Other Font:size=9', resources='dmenu.font: Ignored:size=11')
        self.assertEqual(r.stdout.splitlines(), ['-fn', 'Other Font:size=9', 'input item'])

    def test_default_and_missing_xrdb(self):
        for missing in (False, True):
            if missing:
                (self.base / 'xrdb').unlink()
            r = self.run_menu()
            self.assertEqual(r.stdout.splitlines(), ['-fn', 'monospace:size=11', 'input item'])


if __name__ == '__main__':
    unittest.main()
