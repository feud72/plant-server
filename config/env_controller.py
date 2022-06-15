from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


class Env:
    ENV = environ.Env()

    def __init__(self) -> None:
        self.ENV.read_env(env_file=Path.joinpath(BASE_DIR, ".env"))
        self.SECRET_KEY = self.ENV("SECRET_KEY")
        self.API_KEY = self.ENV("API_KEY")
