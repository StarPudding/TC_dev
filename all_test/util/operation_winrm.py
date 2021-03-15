import winrm


class OperationWINRM:
    def __init__(self, ip=None, username=None, password=None):
        self.winrm = winrm.Session(ip + ':5985', auth=(username, password))

    def do_cmd(self, cmd):
        out1 = self.winrm.run_cmd(cmd)
        print(cmd)
        str_out = out1.std_out.decode('gbk', errors='ignore')
        str_out = str_out + out1.std_err.decode('gbk', errors='ignore')
        print(str_out)
        # str(out1.std_err, encoding='unicode')
        return str_out

