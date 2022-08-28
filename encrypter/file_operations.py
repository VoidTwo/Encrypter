# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from os import (
    fdopen as os_fdopen,
    fstat as os_fstat,
    lstat as os_lstat,
    open as os_open)
from sys import exit as sys_exit
from typing import TYPE_CHECKING

# Local imports
from .common_utils import Platform

# Type checking
if TYPE_CHECKING:
    # Standard imports
    from typing import (
        Any,
        BinaryIO,
        Optional)

    # Local imports
    from .custom_types import (
        LiteralFalse,
        LiteralPlatform)


def get_secure_open_flags() -> int:
    platform: LiteralPlatform = Platform().platform
    flags: int = 0

    try:
        from os import O_EXLOCK
        flags |= O_EXLOCK
        del O_EXLOCK
    except ImportError:
        pass

    try:
        from os import O_NOFOLLOW
        flags |= O_NOFOLLOW
        del O_NOFOLLOW
    except ImportError:
        pass

    try:
        from os import O_RDONLY
        flags |= O_RDONLY
        del O_RDONLY
    except ImportError:
        pass

    if platform == 'W':
        from os import O_BINARY
        flags |= O_BINARY
        del O_BINARY
    return flags


class SecureOpen:
    __flags: int = get_secure_open_flags()

    __slots__ = (
        '__filename', '__file')

    def __init__(self, filename: str = 'encrypter.db') -> None:
        self.__filename: str = filename
        self.__file: Optional[BinaryIO] = None
        return

    def __enter__(self) -> BinaryIO:
        if self.__file is not None:
            raise AssertionError('File is already open.')

        fd: int = os_open(self.__filename, flags=self.__flags, mode=0o444)

        # Best we can do to prevent opening symlinks
        if os_fstat(fd).st_dev != os_lstat(self.__filename).st_dev:
            sys_exit(1)

        if os_fstat(fd).st_ino != os_lstat(self.__filename).st_ino:
            sys_exit(1)

        self.__file = os_fdopen(fd, 'rb')
        return self.__file

    def __exit__(self, *_: Any) -> LiteralFalse:
        if not self.__file.closed:
            self.__file.close()
        return False
