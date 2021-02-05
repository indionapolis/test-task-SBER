import pytest
from aiogram import types, Bot

from src.bot_factory import BotFactory
from tests.fixtures import MESSAGE


@pytest.fixture
def telegram_bot():
    return BotFactory.get_instance("TELEGRAM")


@pytest.fixture
def non_booking_message():
    return types.Message(**MESSAGE)


@pytest.fixture
def booking_message():
    MESSAGE["text"] = "/book 1:00 1"
    return types.Message(**MESSAGE)


async def mock_answer(*args, **kwargs):
    assert args[1] == "Hi! available commands are:\n\n/book <valid time: HH:MM> <number of people more then 0> " \
                      "- creates booking according to params"


async def mock_answer_booking(*args, **kwargs):
    assert args[1] == "Your booking received!"


@pytest.mark.asyncio
async def test_non_booking_command(telegram_bot, non_booking_message, monkeypatch):
    Bot.set_current(telegram_bot._bot)
    monkeypatch.setattr(types.Message, "answer", mock_answer, raising=True)
    await telegram_bot._handle_update(non_booking_message)


@pytest.mark.asyncio
async def test_booking_command(telegram_bot, booking_message, monkeypatch):
    Bot.set_current(telegram_bot._bot)
    monkeypatch.setattr(types.Message, "answer", mock_answer_booking, raising=True)
    await telegram_bot._handle_update(booking_message)
