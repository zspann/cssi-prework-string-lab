import sys
import unittest

from invitation import *
rons_message= "The family of Ron Weasley proudly invite you to celebrate their graduation from Hogwarts on Sunday the May of 18th. Festivities will be held at The Burrow. See you then!"
class TestInvitation(unittest.TestCase):

    def test_percy_replacer(self):
      """It replaces instances of 'Percy' with 'Ron'"""
      self.assertEqual(percy_replacer("Today is the day that Percy Weasley Graduates" ), "Today is the day that Ron Weasley Graduates")
      self.assertEqual(percy_replacer("Percy Weasley is the best" ), "Ron Weasley is the best")

    def test_weasley_invitation(self):
        """It replaces the original string with 4 parameters"""
        self.assertEqual(weasley_invitation("Ron","Sunday", "May", "18th" ), rons_message)

    def test_seating_location(self):
       self.assertEqual(seating_location("Potter"), "You have a reserved seat in the middle section.")
       self.assertEqual(seating_location("Moody"), "You have a reserved seat in the middle section.")
       self.assertEqual(seating_location("Weasley"), "You have a reserved seat in the front row.")
       self.assertEqual(seating_location("Granger"), "You have a reserved seat in the rear section.")

    def test_create_invitation(self):
       self.assertEqual(create_invitation("Harry","Potter", weasley_invitation("Ron","Sunday", "May", "18th" )), "DEAR HARRY,\n"+rons_message+"\nP.S. You have a reserved seat in the middle section.")
       self.assertEqual(create_invitation("Ginny","Weasley", weasley_invitation("Ron","Sunday", "May", "18th" )), "DEAR GINNY,\n"+rons_message+"\nP.S. You have a reserved seat in the front row.")

if __name__ == '__main__':
    unittest.main()
