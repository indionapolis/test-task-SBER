from src.bot_factory import BotFactory

if __name__ == "__main__":
    bot = BotFactory.get_instance("TELEGRAM")
    bot.run()
