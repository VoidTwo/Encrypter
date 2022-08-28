# -*- coding: utf-8 -*-

# Local imports
from .common_utils import Platform
from .custom_types import LiteralPlatform
from .file_operations import SecureOpen


__package__ = 'encrypter'
__title__ = 'Encrypter'
__description__ = 'Secure offline password vault using modern cryptographically secure hashing and encryption ' \
                  'algorithms'
__author__ = 'VoidTwo'
__license__ = 'AGPL-3.0-only'
__version__ = '0.0.1-alpha'

__all__ = (
    'LiteralPlatform',
    'Platform',
    'SecureOpen')
