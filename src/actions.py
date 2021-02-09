import re
from abc import ABC
from typing import Tuple

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
    params = "<valid time: HH:MM> <number of people more than 0>"
    description = "creates booking according to params"

    # pattern to validate params
    pattern = re.compile(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9] [1-9]\d*$")

    time = re.compile(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
    n_people = re.compile(r"^[1-9]\d*$")

    params_map = {"time": time, "n_people": n_people}

    def execute(self, params: set) -> Tuple[bool, str]:
        result = {}
        for param in params:
            for item in self.params_map.items():
                if item[1].match(param):
                    result[item[0]] = param

        if len(result.keys()) == len(self.params_map.keys()):
            msg = restaurant_client.book(**result)
            return True, msg
        else:
            difference = set(self.params_map.keys()) - set(result.keys())
            return False, f"need to specify following param{'' if len(difference) == 1 else 's'}: " \
                          f"{('<%s> ' * len(difference)) % tuple(difference)}"


# 2 2 1 4
# 2
all_actions = [MakeReservation]
