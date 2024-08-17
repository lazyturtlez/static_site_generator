import unittest

from extract_title import extract_title

class TextExtractTitle(unittest.TestCase):
    def test_title(self):
        title = extract_title("test.md")
        self.assertEqual("test", title)