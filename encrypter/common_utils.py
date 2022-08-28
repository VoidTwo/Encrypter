# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard imports
from typing import TYPE_CHECKING

# Type checking
if TYPE_CHECKING:
    # Standard imports
    from typing import Optional

    # Local imports
    from .custom_types import LiteralPlatform


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
    __platform: Optional[LiteralPlatform] = None

    def __init__(self) -> None:
        return

    @property
    def platform(self) -> LiteralPlatform:
        if self.__platform is None:
            self.__platform = get_platform()
        return self.__platform
