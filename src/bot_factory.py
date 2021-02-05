from src.bots import TelegramBot, Bot

BOTS = {"TELEGRAM": TelegramBot}


class BotFactory:
    @staticmethod
    def get_instance(bot_type: str) -> Bot:
        bot = BOTS.get(bot_type)

        if not bot:
            raise ValueError(f"bot type {bot_type} is not available")

        return bot()
