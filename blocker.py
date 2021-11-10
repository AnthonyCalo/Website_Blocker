import time
from datetime import datetime as dt

host_path= r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
temp_path="hosts"

block_list=["www.youtube.com", "youtube.com", "chess.com", "www.chess.com"]

while True:
    #this is the window you want site blocked
    if((dt(dt.now().year,dt.now().month, dt.now().day,8))< dt.now() < (dt(dt.now().year,dt.now().month, dt.now().day,22))):
        print("working hour")
        print("DT.now()", dt.now())
        with open(host_path, 'r+') as file:
            content=file.read()
            print(content)
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
                file.truncate()

        print("fun hours")
        print("DT.now()", dt.now())
    #recheck time every hour
    time.sleep(3600)
