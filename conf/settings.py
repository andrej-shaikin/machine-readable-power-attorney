from pathlib import Path

from environ import Env

env = Env()
env.read_env()

__all__ = [
    "BASE_DIR",
    "DEBUG",
    "DATABASE_URL",
    "APPLICATIONS",
]

BASE_DIR = Path(__file__).parent.parent
DEBUG = env.bool(var="DEBUG", default=False)
DATABASE_URL = env.str(var="DATABASE_URL")

APPLICATIONS = (
    "user",
    "reference",
    "power_attorney",
)
