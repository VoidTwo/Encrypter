# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from gc import collect as gc_collect
from itertools import (
    chain as itertools_chain,
    repeat as itertools_repeat)
from secrets import choice as secrets_choice
from typing import TYPE_CHECKING

# 3rd party imports
from cryptography.hazmat.primitives.ciphers.aead import AESSIV

# Type checking
if TYPE_CHECKING:
    # Standard imports
    from collections.abc import Sequence


class CharacterSets:
    __alpha: str = ''.join(map(chr, itertools_chain(
        range(65, 91), range(97, 123))))
    __alpha_numeric: str = ''.join(map(chr, itertools_chain(
        range(48, 58), range(65, 91), range(97, 123))))
    __alpha_numeric_symbols: str = ''.join(map(chr, range(33, 127)))

    def __init__(self) -> None:
        return

    @property
    def alpha(self) -> str:
        return self.__alpha

    @property
    def alpha_numeric(self) -> str:
        return self.__alpha_numeric

    @property
    def alpha_numeric_symbols(self) -> str:
        return self.__alpha_numeric_symbols


def secure_random_string(length: int, *, character_set: Sequence[str] = CharacterSets().alpha_numeric_symbols) -> str:
    return ''.join(map(secrets_choice, itertools_repeat(character_set, length)))


def secure_encrypt(data: bytes, key: bytes, nonce: bytes) -> bytes:
    ciphertext: bytes = AESSIV(key).encrypt(data, [nonce])

    del data
    del nonce
    del key

    gc_collect()
    return ciphertext
