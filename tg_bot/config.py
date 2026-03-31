from tg_bot.sample_config import Development as Config

class Config(Config):
    API_KEY = "your_api_id"
    OWNER_ID = 123456789
    OWNER_USERNAME = "your_username"

    SQLALCHEMY_DATABASE_URI = "your_database_url"

    SUDO_USERS = [123456789]
