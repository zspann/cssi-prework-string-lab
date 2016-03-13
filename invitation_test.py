import sys
import unittest

from invitation import weasley_invitation, invitee_name, create_invitation
rons_message= "The family of Ron Weasley proudly invite you to celebrate their graduation from Hogwarts on Sunday the May of 18th. Festivities will be held at The Burrow. See you then!"
class TestInvitation(unittest.TestCase):
    def test_weasley_invitation(self):
        """It replaces the original string with 4 parameters"""
        self.assertEqual(weasley_invitation("Ron","Sunday", "May", "18th" ), rons_message)

    def test_invitee_name(self):
       self.assertEqual(invitee_name("Harry Potter"), "H. Potter")
       self.assertEqual(invitee_name("Alstor 'Mad-Eye' Moody"), "A. Moody")

    def test_create_invitation(self):
       self.assertEqual(create_invitation(invitee_name("Alstor 'Mad-Eye' Moody"), weasley_invitation("Ron","Sunday", "May", "18th" )), "A. MOODY,\n"+rons_message)

if __name__ == '__main__':
    unittest.main()
