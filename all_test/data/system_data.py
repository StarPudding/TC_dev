from all_test.setting.base import ZTDS_SYSTEM


class SystemData:
    def __init__(self):
        self.Remote_info = ZTDS_SYSTEM.get('REMOTE_INFO')

    def getRemoteIp(self):
        return self.Remote_info.get('ip')

    def getRemoteUsername(self):
        return self.Remote_info.get('username')

    def getRemotePassword(self):
        return self.Remote_info.get('password')