# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from traceback import format_exception as tb_format_exception
from typing import TYPE_CHECKING

# Type checking
if TYPE_CHECKING:
    # Standard imports
    from typing import Optional

    # Local imports
    from .custom_types import (
        LiteralExceptionType,
        LiteralPlatform)


def get_platform() -> LiteralPlatform:
    from sys import platform as sys_platform

    if sys_platform.startswith('linux'):
        return 'L'  # Linux

    if sys_platform == 'win32':
        return 'W'  # Windows

    if sys_platform == 'darwin':
        return 'M'  # macOS
    return 'U'  # Unknown


class Platform:
    platform: LiteralPlatform = get_platform()


class CustomException(Exception):
    __slots__ = (
        '__exception_type', '__description', '__exception')

    def __init__(
            self,
            exception_type: LiteralExceptionType,
            description: Optional[str] = None,
            exception: Optional[Exception] = None) \
            -> None:
        self.__exception_type: LiteralExceptionType = exception_type
        self.__description: Optional[str] = description
        self.__exception: Optional[Exception] = exception
        return

    def __str__(self) -> str:
        error_data: list[str] = [self.__exception_type]

        if self.__description is not None:
            error_data.append(f': {self.__description}')

        if self.__exception is not None:
            exception_stack_trace: str = ''.join(tb_format_exception(self.__exception))
            error_data.append(f'\n\n{exception_stack_trace}')
        return ''.join(error_data)

    def __repr__(self) -> str:
        description: str = 'NONE' if self.__description is None else self.__description
        exception: str = 'NONE' if self.__exception is None else str(type(self.__exception))

        representation: str = \
            f'Exception Type: {self.__exception_type}\n' \
            f'Description: {description}\n' \
            f'Exception: {exception}'
        return representation
