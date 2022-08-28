# -*- coding: utf-8 -*-

# Standard imports
from typing import TYPE_CHECKING

# Local imports
from .file_operations import SecureOpen

# Type checking
if TYPE_CHECKING:
    # Standard imports
    from typing import BinaryIO


def main() -> None:
    f: BinaryIO

    with SecureOpen() as f:
        pass
    return


if __name__ == '__main__':
    main()
