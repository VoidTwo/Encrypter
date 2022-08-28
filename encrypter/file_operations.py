# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from os import (
    close as os_close,
    fdopen as os_fdopen,
    fstat as os_fstat,
    lstat as os_lstat,
    open as os_open)
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
    from .custom_types import LiteralFalse


def get_secure_open_properties() -> tuple[int, bool]:
    flags: int = 0
    no_follow: bool = False

    try:
        from os import O_EXLOCK
        flags |= O_EXLOCK
        del O_EXLOCK
    except ImportError:
        pass

    try:
        from os import O_NOFOLLOW
        flags |= O_NOFOLLOW
        no_follow = True
        del O_NOFOLLOW
    except ImportError:
        pass

    try:
        from os import O_RDONLY
        flags |= O_RDONLY
        del O_RDONLY
    except ImportError:
        pass

    if Platform.platform == 'W':
        from os import O_BINARY
        flags |= O_BINARY
        del O_BINARY
    return flags, no_follow


def symlink_testing(fd: int, filename: str, *, iterations: int = 10) -> bool:
    for _ in range(iterations):
        if os_fstat(fd).st_dev != os_lstat(filename).st_dev \
                or os_fstat(fd).st_ino != os_lstat(filename).st_ino:
            return True
    return False


class SecureOpen:
    __slots__ = (
        '__filename', '__file_descriptor', '__file',
        '__flags', '__no_follow')

    def __init__(self, filename: str = './encrypter.db') -> None:
        self.__filename: str = filename
        self.__file_descriptor: Optional[int] = None
        self.__file: Optional[BinaryIO] = None

        self.__flags: int
        self.__no_follow: bool
        self.__flags, self.__no_follow = get_secure_open_properties()
        return

    def __enter__(self) -> BinaryIO:
        if (self.__file_descriptor, self.__file) != (None, None):
            self.close()
            raise AssertionError('File is already open.')

        self.__file_descriptor = os_open(self.__filename, flags=self.__flags, mode=0o444)

        if not self.__no_follow:
            if symlink_testing(self.__file_descriptor, self.__filename):
                self.close()
                raise AssertionError(f'Symlink detected on file "{self.__filename}".')

        self.__file = os_fdopen(self.__file_descriptor, 'rb')
        return self.__file

    def __exit__(self, *_: Any) -> LiteralFalse:
        self.close()
        return False

    def close(self) -> None:
        if self.__file is not None and not self.__file.closed:
            self.__file.close()
            self.__file = None

        if self.__file_descriptor is not None:
            try:
                os_close(self.__file_descriptor)
            except OSError:
                pass

            self.__file_descriptor = None
        return
