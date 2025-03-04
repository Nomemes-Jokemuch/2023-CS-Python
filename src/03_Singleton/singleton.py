from typing import Optional


class Singleton:
    single: Optional["Singleton"] = None

    def __new__(cls):
        if not cls.single:
            cls.single = super().__new__(cls)

        return cls.single
