from utilits import scan
from rich.progress import track
from rich.console import Console
import time

def typerwrite_effect(text):
    for _ in track(range(10), description = "Подключемся к Пентагону"):
        time.sleep(0.1)
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.03)
    print()

def menu():
    console = Console()
    logo = """" 
 _____  _     ___  ___        _____             _ 
|  _  || |    |  \/  |       |  __ \           | |
| | | || |__  | .  . | _   _ | |  \/  ___    __| |
| | | || '_ \ | |\/| || | | || | __  / _ \  / _` |
\ \_/ /| | | || |  | || |_| || |_\ \| (_) || (_| |
 \___/ |_| |_|\_|  |_/ \__, | \____/ \___/  \__,_|
                        __/ |                     
                       |___/                      """""

    console.print("[bold cyan]", end="")
    typerwrite_effect(logo)
    console.print("[bold cyan]")
    print("1. utilits")
    podmenu = int(input("Введите номер функции: "))
    if(podmenu == 1):
        podmenu_scan()
        

def podmenu_scan():
    array = list(input("Введите команду в формате: <IP> <flag> <ports>\n").split())
    if(array[1]=="help"):
        print("Инструкции")
    if(array[1] == "Ss"):
        scan(array[0],array[2])
