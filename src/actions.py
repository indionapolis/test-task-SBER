import re
from abc import ABC

from src.restaurant_client import Client

restaurant_client = Client()


class Action(ABC):
    command: str = None
    params: str = None
    description: str = None

    def execute(self, params: str) -> str:
        pass


class MakeReservation(Action):
    command = "book"
    params = "<valid time: HH:MM> <number of people more then 0>"
    description = "creates booking according to params"

    # pattern to validate params
    pattern = re.compile(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9] [1-9]\d*$")

    def execute(self, params: str) -> str:

        if self.pattern.match(params):
            time, n_people = params.split(" ")
            restaurant_client.book(time, n_people)
            return "Your booking received!"
        else:
            return f"Incorrect format, example: {self.params}"


all_actions = [MakeReservation]
