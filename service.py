from utilits import scan

def menu():
    print("""" 
 _____  _     ___  ___        _____             _ 
|  _  || |    |  \/  |       |  __ \           | |
| | | || |__  | .  . | _   _ | |  \/  ___    __| |
| | | || '_ \ | |\/| || | | || | __  / _ \  / _` |
\ \_/ /| | | || |  | || |_| || |_\ \| (_) || (_| |
 \___/ |_| |_|\_|  |_/ \__, | \____/ \___/  \__,_|
                        __/ |                     
                       |___/                      """"")

    print("(1) utilits")
    podmenu = int(input())
    if(podmenu == 1): 
        print("Введите IP и port или диапозон портов")
        ip = str(input("IP: "))
        port = list(input("port: ").split("/"))
        for i in port:
            scan(ip,i)
