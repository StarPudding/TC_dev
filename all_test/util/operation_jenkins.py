import jenkins


class OperationJenkins:
    def __init__(self, url, username, password):
        self.server = jenkins.Jenkins(url=url, username=username, password=password)

    def do_job(self, job_name):
        self.server.build_job(job_name)
