import requests
import time
from dotenv import load_dotenv
import os


def send_msg(txt):

    api_token = os.environ.get("bot_token")
    chat_id = os.environ.get("chat_id")
    send_req = "https://api.telegram.org/bot"+api_token + \
        "/sendMessage?chat_id="+chat_id+"&parse_mode=Markdown&text="+txt
    wait = 0
    snd_flag = False
    while wait < 30:
        try:
            resp = requests.get(send_req)
            wait = 31
            snd_flag = True
        except:
            print("waiting for internet connection")
            time.sleep(10)
            wait += 10
    if snd_flag:
        if resp.json()['ok'] == True:
            print(f"the message has been send successfully to the channel")
        else:
            print(f"seems there is an issue with your request")
    else:
        print(f"please try again after sometime...!!")


if __name__ == "__main__":
    load_dotenv()
    usr_inp = input("enter your message: ")
    send_msg(usr_inp)
