# -*- coding: utf-8 -*-

# Standard imports
from gc import collect as gc_collect
from getpass import (
    getpass,
    GetPassWarning)
from sys import (
    exit as sys_exit,
    stderr)
from typing import TYPE_CHECKING

# Local imports
from .common_utils import CustomException
from .cryptography_utils import (
    secure_decrypt,
    secure_encrypt,
    secure_random_string)
from .data_modules import EncrypterDatabase
from .file_operations import (
    SecureOpen,
    SecureWriter)

# Type checking
if TYPE_CHECKING:
    # Standard imports
    from typing import BinaryIO


def main() -> None:
    f: BinaryIO
    encrypted_data: bytes

    with SecureOpen() as f:
        encrypted_data = f.read()

    nonce: bytes

    try:
        nonce = getpass('Master Password: ').encode('UTF-8')
    except GetPassWarning:
        raise CustomException('ERROR', 'Secure password input unavailable')
    except UnicodeEncodeError:
        raise CustomException('ERROR', 'Password must be UTF-8 encodable')

    key: bytes
    encrypter_database: EncrypterDatabase

    # 80 bytes: 512 bits AES SIV key and 16 bytes ciphertext tag
    if len(encrypted_data) < 81:
        key = secure_random_string(64).encode('ASCII')  # 512 bits
        encrypter_database = EncrypterDatabase.new()
    else:
        key = encrypted_data[:64]
        encrypter_database = EncrypterDatabase.deserialize(secure_decrypt(
            encrypted_data[64:], key, nonce))

    encrypted_data = b''.join((key, secure_encrypt(encrypter_database.serialize(), key, nonce)))
    gc_collect()

    with SecureWriter() as f:
        f.write(encrypted_data)
    return


if __name__ == '__main__':
    e: CustomException

    try:
        main()
    except CustomException as e:
        print(f'-- EXCEPTION --\n{repr(e)}', file=stderr)

    gc_collect()
    sys_exit(0)
