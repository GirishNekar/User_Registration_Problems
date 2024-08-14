"""
@Author: Girish
@Date: 2024-08-14
@Last Modified by: Girish
@Last Modified time: 2024-08-14
@Title: Check for Users First anme is Valid or not
"""

import unittest
from User_Registration_Problems.User_Registrsion.UC1 import validate_first_name  

class TestNameValidation(unittest.TestCase):
    """
    Unit test class for validating name functionality.
    
    """

    def test_valid_name(self):
        
        
        """
        Description:
            Checks if the name is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid name.
        """
        
        
        self.assertTrue(validate_first_name("John"),"Should be valid")
        self.assertTrue(validate_first_name("Alice"),"Should be valid")
        self.assertTrue(validate_first_name("Jo"), "Should be invalid due to length")
        self.assertFalse(validate_first_name("Al"), "Should be invalid due to length")
        self.assertFalse(validate_first_name("john"),"Should be invalid due to lowercase first letter")
        self.assertFalse(validate_first_name("alice"),"Should be invalid due to lowercase first letter")
        self.assertFalse(validate_first_name("Jo@n"), "Should be invalid due to  presence of a special character")
        self.assertFalse(validate_first_name("Al!ce"),  "Should be invalid due to  presence of a special character")
        self.assertFalse(validate_first_name("John123"), "Should be invalid due to  presence of a Number")
        self.assertFalse(validate_first_name("Alice456"), "Should be invalid due to  presence of a Number")



if __name__ == "__main__":
    unittest.main()
