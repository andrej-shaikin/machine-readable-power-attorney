from environ import Env

env = Env()
env.read_env()

SECRET_KEY = env.str(
    var="SECRET_KEY",
    default="acb213c54c994669957355a51d9cb8c284cb6b695d454279bd974a2ff47f94df619962c710934824aec0d503422c928e"
)
DEBUG = env.bool(var="DEBUG", default=False)
DATABASE_URL = env.str(var="DATABASE_URL")

APPLICATIONS = [
    "user",
]
