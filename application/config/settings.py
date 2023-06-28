import os


class Settings:
    def __init__(self):
        self.load_dotenv()

        self.host = os.getenv("HOST", "127.0.0.1")
        self.port = int(os.getenv("PORT", 8000))

        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = int(os.getenv("DB_PORT", 3306))
        self.db_user = os.getenv("DB_USER", "")
        self.db_password = os.getenv("DB_PASSWORD", "")
        self.db_name = os.getenv("DB_NAME", "")
        self.db_socket = os.getenv("DB_SOCKET", "")

        # self.redis_host = os.getenv("REDIS_HOST", "localhost")
        # self.redis_port = int(os.getenv("REDIS_PORT", 6379))

    @staticmethod
    def load_dotenv():
        from dotenv import load_dotenv
        load_dotenv()


settings = Settings()
