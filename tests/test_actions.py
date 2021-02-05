import pytest

from src.actions import MakeReservation


@pytest.fixture
def reservation_action():
    return MakeReservation()


def test_incorrect_reservation(reservation_action):
    response = reservation_action.execute("")
    assert response == "Incorrect format, example: <valid time: HH:MM> <number of people more then 0>"

    response = reservation_action.execute("1:00 0")
    assert response == "Incorrect format, example: <valid time: HH:MM> <number of people more then 0>"

    response = reservation_action.execute("1:60 5")
    assert response == "Incorrect format, example: <valid time: HH:MM> <number of people more then 0>"


def test_correct_reservation(reservation_action):
    response = reservation_action.execute("12:00 1")
    assert response == "Your booking received!"

    response = reservation_action.execute("00:00 100")
    assert response == "Your booking received!"
