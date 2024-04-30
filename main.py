import os
import pytz
import time
import datetime

from pyrogram import Client

user_session_string = os.environ.get("1BVtsOH8Bu4qrcA63aC7Nymd0B9nb0BpfQe_PabeQXNeBciIBtpHQ6YSaeUv2lZpNNOrp2PW1RGcxWJ7YBJoEhyHwI8z97ILIcCGjsr2V9u40cQkdCGUDsj35En345lY7V0f9t7SedTFv5IsxhWV-A2HbVlQh84k-Axy8Q5eqdAcmJLV7iU6Btnt4JSbx-Aa_IgPyLH2uZS4MxRLNqq2sK9wWa-w_6wr50W0XUq3MyMfqFVtMGomybbHRzcql1JchLNfLvWQIIJ0Z4YyPZRC7b_s9ZNbFwkOICHS5wuujh_oY7FJxGWt4S_jDPt3nzxtSdSSRr2QAUlQkKkWCkSJAtOOinOhCmZk=")
bots_str = os.environ.get("ArabUltraUbot ArabV2Ubot supernovaxubot DayforuMusic_bot ArabxRobot AfterGankUbot SASProtectV1_Bot SonixUbot OnedayXUbot RoyalUbot MydamnUbot fsubprem_1bot DomiUbot")
bots = bots_str.split() if bots_str else []
update_channel = os.environ.get("-1001837260549")
status_message_ids_str = os.environ.get("44")
status_message_ids = [int(i.strip()) for i in status_message_ids_str.split(' ')] if status_message_ids_str else []
api_id = int(os.environ.get(29737623))
api_hash = os.environ.get("71a4bb6501593f225cdab4d4b368a830")
user_client = Client(session_name=str(user_session_string), api_id=api_id, api_hash=api_hash)

def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"🔰SI ARAB STATUS BOT🔰\n\n__( All bots are checked automatically if any correction report it )__\n\n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"𝙱𝙾𝚃 𝙽𝙰𝙼𝙴    {bot} \n𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @{bot}\n𝚂𝚃𝙰𝚃𝚄𝚂 ❌\n\n"
                    #user_client.send_message("me", f"@{bot} was down")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"𝙱𝙾𝚃 𝙽𝙰𝙼𝙴    {bot} \n𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @{bot}\n𝚂𝚃𝙰𝚃𝚄𝚂 ✅\n\n"
                user_client.read_history(bot)

            time_now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
            formatted_time = time_now.strftime("%d %B %Y %I:%M %p")

            edit_text += f"**Updated on {formatted_time} (IST)**"

            for status_message_id in status_message_ids:
                user_client.edit_message_text(int(update_channel), status_message_id, edit_text)
                time.sleep(5)
            print(f"[INFO] everything done! sleeping for 3 hours...")

            time.sleep(864000)

if __name__ == "__main__":
   main()
