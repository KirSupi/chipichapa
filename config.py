import json


# PATTERN Singleton может быть только один конфиг
class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        with open('config.json', 'r') as f:
            self._config = json.load(f)

    @property
    def sprites_directory(self) -> str:
        return self._config['sprites_directory']

    @property
    def sprites_format(self) -> str:
        return self._config['sprites_format']

    @property
    def sprites_size(self) -> str:
        return self._config['sprites_size']

    @property
    def background_sprite(self) -> str:
        return self._config['background_sprite']

    @property
    def difficulty(self) -> str|None:
        return self._config['difficulty'] if 'difficulty' in self._config else None


# Загрузка конфигурации
config = Config()
