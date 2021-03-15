import itsdangerous
from itsdangerous import SignatureExpired
from itsdangerous import BadSignature
# 获取/解析token用到的模块
from django.conf import settings

# 把settings中的一串字符串作为 secretkey

token_expires = 3600


class Token:
    # 获取/解析token的类
    tjss = itsdangerous.TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=token_expires)
    # 把settings中的一串字符串作为 secretkey
    # 设置一个失效时间

    @classmethod
    def create_token(cls, data):
        token = cls.tjss.dumps(data).decode()
        # data是根据什么获取的token,比如根据用户的用户名和密码
        return token

    @classmethod
    def check_token(cls, token):
        try:
            data = cls.tjss.loads(token)
            # 解析传过来的token,比如，解析成用户的用户名和密码
        except SignatureExpired:
            # 时间过期
            return '0'
        except BadSignature:
            # 错误token
            return '1'
        return data
