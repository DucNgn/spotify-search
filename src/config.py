from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)

NAME = settings.APP.NAME
HOST = settings.APP.HOST
PORT = settings.APP.PORT
VERSION = settings.APP.VERSION

SPOTIFY_TOKEN = settings.SPOTIFY_TOKEN
