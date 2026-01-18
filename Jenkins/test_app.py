import unittest
from app import check_status

class TestJenkinsProject(unittest.TestCase):
    
    def test_check_status(self):
        # בדיקה שהפונקציה מחזירה True כפי שצפוי
        self.assertTrue(check_status())

if __name__ == "__main__":
    unittest.main()
