import uuid
from enum import Enum
import json

class Meeting:
    def __init__(self):
        super().__init__()
        self.__meeting_uuid = uuid.uuid4()
        self.__participants = list()

    def join_meeting(self, participant):
        self.__participants.append(participant)
    
    def leave_meeting(self, participant):
        self.__participants.remove(participant)

    def total_participants(self):
        return len(self.__participants)

    def __str__(self):
        s = "{{'meeting_uuid':'{}',".format(str(self.__meeting_uuid))

        for x in range(len(self.__participants)):
            s += "'{}':{},".format(x, str(self.__participants[x]))

        s += "}"

        return s

HOST = 100
ATTENDEE = 200

class Participant():
    def __init__(self, first_name, last_name, role):
        self.__participant_uuid = str(uuid.uuid4())
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role = role
    
    def __str__(self):
        return f"""{{'participant_uuid':'{str(self.__participant_uuid)}','first_name':'{self.__first_name}','last_name':'{self.__last_name}','role':'{self.__role}'}}"""


# a = Participant("summer", "fang", HOST)
# print(str(a))
# print(a.__dict__)