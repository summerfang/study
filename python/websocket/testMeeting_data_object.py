import unittest
import meeting_data_object
from meeting_data_object import Meeting, Participant, HOST, ATTENDEE


class MeetingTest(unittest.TestCase):
    def setUp(self):
        # Create a meeting first
        self.test_meeting = Meeting()

        # Create 3 participants
        participant1 = Participant("Summer", "Fang", HOST)
        participant2 = Participant("Weijia", "Fang", ATTENDEE)
        participant3 = Participant("Wendy", "Wang", ATTENDEE)

        self.test_meeting.join_meeting(participant1)
        self.test_meeting.join_meeting(participant2)
        self.test_meeting.join_meeting(participant3)

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_join_meeting(self):
        participant = Participant("John", "Smith", ATTENDEE)
        self.test_meeting.join_meeting(participant)
        self.assertEqual(self.test_meeting.total_participants(), 4, "should be 4")
        print(str(self.test_meeting))


if __name__ == "__main__":
    unittest.main()