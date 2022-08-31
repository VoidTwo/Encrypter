# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from typing import TYPE_CHECKING

# 3rd party imports
from orjson import (
    dumps as orjson_dumps,
    JSONDecodeError,
    JSONEncodeError,
    loads as orjson_loads)

# Local imports
from .common_utils import CustomException

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
        serialized_data: bytes

        try:
            serialized_data = orjson_dumps(self.__data)
        except JSONEncodeError:
            raise CustomException('ERROR', 'Data serialization failed')
        return serialized_data

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
        data: TypedDictEncrypterDatabase

        try:
            data = orjson_loads(serialized_data)
        except JSONDecodeError:
            raise CustomException('ERROR', 'Data deserialization failed')
        return EncrypterDatabase(data)
