import os
import time
import datetime
from pyrogram import Client
from config import API_ID, API_HASH

# Function to check bot's activity status
def check_bot_status(user_client, bot_username):
    try:
        # Send '/start' message to the bot
        snt = user_client.send_message(bot_username, '/start')
        time.sleep(15)  # Wait for 15 seconds for response

        # Get the last message from the bot
        msg = user_client.get_history(bot_username, 1)[0]

        # Compare the sent message ID with the last message ID from the bot
        if snt.message_id == msg.message_id:
            return False  # Bot is inactive
        else:
            return True  # Bot is active
    except Exception as e:
        print(f"Error checking status for @{bot_username}: {e}")
        return False  # Bot is inactive (error occurred)

# Function to update status every 1 hour
def update_status(user_client, update_channel, status_message_ids, edit_text):
    try:
        # Update status message in the channel or group
        for status_message_id in status_message_ids:
            user_client.edit_message_text(int(update_channel), status_message_id, edit_text)
            time.sleep(5)  # Wait for 5 seconds before updating the next message
        print("[INFO] Status updated successfully.")
    except Exception as e:
        print(f"Error updating status message: {e}")

# Main function
def main():
    try:
        # Get environment variable values
        user_session_string = os.environ.get("BQAP-GEAJeLaW5zShFphAkcsPn1yau3TXAXGhGCqp2zzm_lu2Pi-GmfiGN7G-7YM3KSRLFoS-YHNEGX9F13-rJm9zJr9LUuoICsbzxe7bUvfsXxSnoUaF5bIxHP3SilzWBJ3-vLgW0AANsUNGSgJbR6vyG1iyT5_Racc3CosPz8SznpLTaKq6x6w4s08-xO03btFljAhnDxjPSiXfgaodwNLzOfu42I2AiiFdwU_GwnOCmaitlrM6fqoxYL--8-2ppmmOzWU2IF1ZAgAAjLOwepxwFVCZTkW3lkbR24D8Aj3rdT0w26ch7WZ86Dr7UDPFV3khlm6337h_m99uKbHUttX-2CHIwAAAAByE1_bAA")
        bot_usernames_str = os.environ.get("ArabUltraUbot ArabV2Ubot supernovaxubot DayforuMusic_bot ArabxRobot AfterGankUbot SASProtectV1_Bot SonixUbot OnedayXUbot RoyalUbot MydamnUbot fsubprem_1bot DomiUbot")
        update_channel = os.environ.get("-1001837260549")
        status_message_ids_str = os.environ.get("43")
        api_id=API_ID,
        api_hash=API_HASH,

        # Inisialisasi klien Pyrogram dengan kunci API
        user_client = Client(session_name=str(user_session_string), api_id=api_id, api_hash=api_hash)


        with user_client:
            while True:
                print("[INFO] Starting bot status check...")

                # Split bot_usernames_str string into a list of bot_usernames
                bot_usernames = bot_usernames_str.split() if bot_usernames_str else []

                # Prepare the edit text to be updated in the channel/group
                edit_text = f"🤖 Bot Status Updates 🤖\n\nLast Checked: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

                # Check activity status for each bot
                for bot_username in bot_usernames:
                    print(f"[INFO] Checking status for @{bot_username}")
                    if check_bot_status(user_client, bot_username):
                        edit_text += f"\n\n🟢 @{bot_username} is Active"
                    else:
                        edit_text += f"\n\n🔴 @{bot_username} is Inactive"

                # Add the last update time to the edit text
                edit_text += f"\n\nLast Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

                # Split status_message_ids_str string into a list of status_message_ids
                status_message_ids = [int(i.strip()) for i in status_message_ids_str.split(' ')] if status_message_ids_str else []

                # Update status in the channel/group
                update_status(user_client, update_channel, status_message_ids, edit_text)

                # Wait for 1 hour before checking status again
                time.sleep(3600)  # 1 hour = 3600 seconds
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
