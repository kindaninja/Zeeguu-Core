import random

from sqlalchemy.orm.exc import NoResultFound

from tests_core_zeeguu.rules.base_rule import BaseRule
from zeeguu.model import Language


class LanguageRule(BaseRule):
    """A Testing Rule class for Languages

    Has all supported languages as properties. Languages are created and
    saved to the database if they don't yet extist in the database.
    """

    languages = {
        "da": "Danish",
        "de": "German",
        "en": "English",
        "es": "Spanish",
        "fr": "French",
        "it": "Italian",
        "nl": "Dutch",
        "no": "Norwegian",
        "pt": "Portuguese",
        "ro": "Romanian"
    }

    @classmethod
    def __get_or_create_language(cls, language_id):
        try:
            return Language.find(language_id)
        except NoResultFound:
            return cls.__create_new_language(language_id)

    @classmethod
    def __create_new_language(cls, language_id):
        language_name = cls.languages.get(language_id)

        if language_name is None:
            raise KeyError

        new_language = Language(language_id, language_name)

        cls.save(new_language)

        return new_language

    @property
    def da(self):
        return self.__get_or_create_language("da")

    @property
    def de(self):
        return self.__get_or_create_language("de")

    @property
    def en(self):
        return self.__get_or_create_language("en")

    @property
    def es(self):
        return self.__get_or_create_language("es")

    @property
    def fr(self):
        return self.__get_or_create_language("fr")

    @property
    def it(self):
        return self.__get_or_create_language("it")

    @property
    def nl(self):
        return self.__get_or_create_language("nl")

    @property
    def no(self):
        return self.__get_or_create_language("no")

    @property
    def pt(self):
        return self.__get_or_create_language("pt")

    @property
    def ro(self):
        return self.__get_or_create_language("ro")

    @property
    def random(self):
        random_id, __ = random.choice(list(self.languages.items()))
        return self.__get_or_create_language(random_id)
