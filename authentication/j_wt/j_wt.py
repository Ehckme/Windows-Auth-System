import jwt
import datetime
from config import Config

class JWT:
    def __init__(self):
        pass

    def generate_jwt_token(self, email=None):
        self.email = email
        payload_data = {
            'email': f'{self.email}',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        token = jwt.encode(
            payload=payload_data,
            key=Config.FLASK_SECRET_KEY,

        )
        self.token = token
        return self.token

    def decode_jwt_token(self, encoded_token):
        self.encoded_token = encoded_token

        decode_payload_data = jwt.decode(
            jwt=self.encoded_token,
            options={"verify_signature": True},
            key=Config.FLASK_SECRET_KEY,
            algorithms=["HS256"],
        )
        self.decoded_payload_data = decode_payload_data
        return self.decoded_payload_data

if __name__ == '__main__':

    token = JWT()

    login_token = token.generate_jwt_token('cody@gmail.com')

    print(f"encoded jwt token : {login_token}")

    decode_login_token = token.decode_jwt_token(login_token)

    print(decode_login_token['email'])

    print(f"decoded jwt token : {decode_login_token}")
