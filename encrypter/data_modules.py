# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from typing import (
    cast,
    TYPE_CHECKING)

# 3rd party imports
from orjson import (
    dumps as orjson_dumps,
    loads as orjson_loads)

# Type checking
if TYPE_CHECKING:
    # Local imports
    from .custom_types import (
        TypedDictEncrypterDatabase,
        TypedDictEncrypterDatabaseGlobalSettings)


class EncrypterDatabase:
    def __init__(self, data: TypedDictEncrypterDatabase) -> None:
        self.__data: TypedDictEncrypterDatabase = data.copy()
        return

    def serialize(self) -> bytes:
        return cast(bytes, orjson_dumps(self.__data))

    @staticmethod
    def new() -> EncrypterDatabase:
        settings: TypedDictEncrypterDatabaseGlobalSettings = {
            'name': None}

        data: TypedDictEncrypterDatabase = {
            'folders': {},
            'passwords': [],
            'settings': settings,
            'tags': []}
        return EncrypterDatabase(data)

    @staticmethod
    def deserialize(serialized_data: bytes) -> EncrypterDatabase:
        data: TypedDictEncrypterDatabase = orjson_loads(serialized_data)
        return EncrypterDatabase(data)
