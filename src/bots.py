from abc import ABC

from aiogram import Dispatcher, Bot as TelegramBotClient, executor, types

from src.actions import all_actions

TELEGRAM_API_TOKEN = "1649979045:AAFHeqndPGoqas48PQQ_o_hS516ohUkGm5g"


class Bot(ABC):
    def __init__(self):
        self._init_bot()

    def _init_bot(self):
        pass

    def run(self):
        pass


class TelegramBot(Bot):
    def _init_bot(self):
        self._bot = TelegramBotClient(token=TELEGRAM_API_TOKEN)
        self._dp = Dispatcher(self._bot)

        self.actions = {action.command: action() for action in all_actions}
        self.commands_list = [f"/{action.command} {action.params} - {action.description}" for action in all_actions]

        self._dp.register_message_handler(self._handle_update)

    async def _handle_update(self, message: types.Message):
        command = message.get_command(pure=True)

        if command and command in self.actions.keys():
            action = self.actions.get(command)
            response = action.execute(message.get_args().strip())
            await message.answer(response)
        else:
            await message.answer("Hi! available commands are:\n\n" + "\n".join(self.commands_list))

    def run(self):
        executor.start_polling(self._dp, skip_updates=True)
