import hashlib
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from uconra.error import MailError
import re
from uconra.smtp_mail import SMTP_Mail

class Register:
    """
     # Use case Example

    register = Register()

    print(register.userEmail('cody@gmail.com'))
    print(register.userPassword('flex'))
    print(register.userKey('flex'))
    """
    def __init__(self):
        pass
    # create and check user email function
    def userEmail(self, email):
        """
        :param email:
        :return:
        """
        self.email = email
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', self.email):
            print("Okay")
        else:
            try:
                raise MailError('Invalid email input')
            except MailError as e:
                print(f'Error: {e}')
            finally:
                print('MailError')
        return str(self.email)

    # Create and hash user passerword function
    def userPassword(self, password):
        """
        :param password:
        :return:
        """
        self.password = password
        self.phPassword = PasswordHasher()
        self.hashed_argonPassword = self.phPassword.hash(self.password)
        return self.hashed_argonPassword

    # Create and hash user key function
    def userKey(self, key):
        """
        :param key:
        :return:
        """
        self.key = key
        self.phKey = PasswordHasher()
        self.hashed_argonKey = self.phKey.hash(self.key)
        return self.hashed_argonKey

    def hash_encryption(self, encryption):
        self.encryption = encryption
        self.emcrypt_data = hashlib.sha256(encryption.encode())
        self.encrypted_data = self.emcrypt_data.hexdigest()
        return self.encrypted_data





if __name__ == '__main__':
   Register()

   hash = Register()
   encryption = hash.hash_encryption('thato')

   hash1 = Register()
   encryption1 = hash.hash_encryption('thato')

   print(encryption)
   print(encryption1)









