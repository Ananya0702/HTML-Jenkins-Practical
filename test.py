
import unittest
from pathlib import Path

class TestRegistrationForm(unittest.TestCase):

    def test_form_fields(self):
        html = Path("index.html").read_text(encoding="utf-8")

        self.assertIn('<form id="registrationForm">', html)
        self.assertIn('id="name"', html)
        self.assertIn('id="email"', html)
        self.assertIn('id="contact"', html)
        self.assertIn('type="submit"', html)

if __name__ == "__main__":
    unittest.main()
