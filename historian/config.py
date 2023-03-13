from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="HISTORIAN",
    settings_files=['settings.yaml', '.secrets.yaml'],
)
