# -*- coding: utf-8 -*-

# Standard imports
from typing import (
    Any,
    Literal,
    Optional,
    Type,
    TypedDict)


LiteralFalse = Literal[False]
LiteralPlatform = Literal['L', 'W', 'M', 'U']

TypedDictEncrypterDatabaseSecret: Type = TypedDict(
    'TypedDictEncrypterDatabaseSecret', {
        'title': str,
        'comments': Optional[str],
        'description': Optional[str],
        'secret': str})

TypedDictEncrypterDatabaseGlobalSettings: Type = TypedDict(
    'TypedDictEncrypterDatabaseGlobalSettings', {
        'name': Optional[str]})

TypedDictEncrypterDatabase: Type = TypedDict(
    'TypedDictEncrypterDatabase', {
        'folders': dict[str, Any],
        'passwords': list[TypedDictEncrypterDatabaseSecret],
        'settings': TypedDictEncrypterDatabaseGlobalSettings,
        'tags': list[str]})
