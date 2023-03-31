import os
from jenkins import Jenkins
import requests


class JenkinsContest:
    def __init__(self):
        # jenkins的IP地址
        self.jenkins_url = "http://127.0.0.1:8080/"
        # jenkins用户名和密码
        self.server = Jenkins(self.jenkins_url, username='admin', password='3cfd0cad3a3d458ba084cebe3a7df733')
    def jenkins_content_info(self):
        result_job = self.server.get_jobs()
        jobs_name = result_job[0]["name"]
        job_name = jobs_name
        job_url = self.server.get_job_info(job_name)['url']
        job_last_number = self.server.get_job_info(job_name)['lastBuild']['number']
        report_url = job_url + str(job_last_number) + '/allure'
        return result_job, jobs_name, job_name, job_url, job_last_number, report_url

class Send_DingTalk(JenkinsContest):
    def __init__(self):
        super().__init__()
        self.result_job, self.jobs_name, self.job_name, self.job_url, self.job_last_number, self.report_url = self.jenkins_content_info()

    def push_message(self):
        content = {}
        file_path = os.path.dirname(os.getcwd()) + '/allure-report/export/prometheusData.txt'
        f = open(file_path)
        for line in f.readlines():
            launch_name = line.strip('\n').split(' ')[0]
            num = line.strip('\n').split(' ')[1]
            content.update({launch_name: num})
        f.close()
        passed_num = content['launch_status_passed']  # 通过数量
        failed_num = content['launch_status_failed']  # 失败数量
        broken_num = content['launch_status_broken']  # 阻塞数量
        skipped_num = content['launch_status_skipped']  # 跳过数量
        case_num = content['launch_retries_run']  # 总数量
        """
        钉钉消息发送，通过webhook发送消息
        """
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=38fa3ddfc67f5f28217470ca3212539139b094eb1fbfabde8fa1ad84aaaa95d4"
        # 这里一定要注意！！！content:内容要包含钉钉的关键字，不然会一直报错不通过！！！
        # 这里一定要注意！！！content:内容要包含钉钉的关键字，不然会一直报错不通过！！！
        # 这里一定要注意！！！content:内容要包含钉钉的关键字，不然会一直报错不通过！！！!

        content = {
            "msgtype": "text",
            "text": {
                "content": "测试阶段接口自动化脚本执行结果：\n运行总数" + case_num
                           + "\n通过数量：" + passed_num
                           + "\n失败数量：" + failed_num
                           + "\n阻塞数量：" + broken_num
                           + "\n跳过数量：" + skipped_num
                           + "\n构建地址：\n" + self.job_url
                           + "\n报告地址：" + self.report_url
            }
        }

        response = requests.post(url=webhook, json=content, verify=False)

        if response.json()['errmsg'] != "ok":
            return response.text

        return response


if __name__ == '__main__':
    Send_DingTalk().push_message()
