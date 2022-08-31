# -*- coding: utf-8 -*-

# Local imports
from .common_utils import Platform
from .cryptography_utils import (
    CharacterSets,
    secure_encrypt,
    secure_random_string)
from .custom_types import LiteralPlatform
from .file_operations import (
    SecureOpen,
    SecureWriter)


__package__ = 'encrypter'
__title__ = 'Encrypter'
__description__ = 'Secure offline password vault using modern cryptographically secure hashing and encryption ' \
                  'algorithms'
__author__ = 'VoidTwo'
__license__ = 'AGPL-3.0-only'
__version__ = '0.0.3-alpha'

__all__ = (
    'CharacterSets',
    'LiteralPlatform',
    'Platform',
    'secure_encrypt',
    'secure_random_string',
    'SecureOpen',
    'SecureWriter')
