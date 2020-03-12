import requests
import json
import random

USERNAME = "18328307505"
PASSWORD = "zxfzyz"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.132 Safari/537.36 "
}

login_data = {
    "userName": USERNAME,
    "password": PASSWORD
}

login_url = "http://volunteer.cd120.com/hx_volunteer/sys/sysuser/login"  # post
active_url = "http://volunteer.cd120.com/hx_volunteer/sys/active/getActiveList"  # get
select_url = "http://volunteer.cd120.com/hx_volunteer/sys/activeSchedule/saveActiveSchedule"  # get

if __name__ == '__main__':
    session = requests.session()
    session.post(login_url, headers=header, data=login_data)
    active_list = json.loads(session.get(active_url).text)

    active_id_list = []
    title_list = []
    cnt = 0
    for active in active_list:
        cnt += 1
        print("{}: {}".format(cnt, active["title"]))
        active_id_list.append(active["id"])
        title_list.append(active["title"])

    op = int(input("请输入你想申请的服务编号:"))
    active_id = active_id_list[op - 1]
    title = title_list[op - 1]
    active_date = input("请输入你想选择的日期，格式如2020-03-01: ")
    time = random.random()
    params = {
        "activeDate": active_date,
        "time": time,
        "activeId": active_id,
        "title": title,
        "timeType": "false"
    }

    times = input("请输入你想选的时间段(0 8:00-10:00, 1 10:00-12:00, 2 12:00-14:00,"
                  " 3 14:00-16:00)，例如01选择前两个时间段，注意没有空格: ")
    for time in times:
        params["time" + time] = 2

    input("等待12:00过后敲一下回车开始抢")

    session.get(select_url, params=params)
    print("应该抢成功了！")