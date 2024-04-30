import os
import time
import datetime
from pyrogram import Client

# Fungsi untuk memeriksa status keaktifan bot
def check_bot_status(user_client, bot_username):
    try:
        # Kirim pesan '/start' ke bot
        snt = user_client.send_message(bot_username, '/start')
        time.sleep(15)  # Tunggu 15 detik untuk tanggapan

        # Dapatkan pesan terakhir dari bot
        msg = user_client.get_history(bot_username, 1)[0]

        # Bandingkan ID pesan yang dikirim dengan ID pesan terakhir dari bot
        if snt.message_id == msg.message_id:
            return False  # Bot tidak aktif
        else:
            return True  # Bot aktif
    except Exception as e:
        print(f"Error checking status for @{bot_username}: {e}")
        return False  # Bot tidak aktif (terjadi kesalahan)

# Fungsi untuk memperbarui status setiap 1 jam
def update_status(user_client, update_channel, status_message_ids, edit_text):
    try:
        # Perbarui pesan status di saluran atau grup
        for status_message_id in status_message_ids:
            user_client.edit_message_text(int(update_channel), status_message_id, edit_text)
            time.sleep(5)  # Tunggu 5 detik sebelum memperbarui pesan selanjutnya
        print("[INFO] Status updated successfully.")
    except Exception as e:
        print(f"Error updating status message: {e}")

# Fungsi utama
def main():
    try:
        # Ambil nilai environment variables
        user_session_string = os.environ.get("PYROGRAM_SESSION")
        bot_usernames_str = os.environ.get("BOT_USERNAMES")
        update_channel = os.environ.get("UPDATE_CHANNEL")
        status_message_ids_str = os.environ.get("STATUS_MESSAGE_IDS")

        # Inisialisasi klien Pyrogram
        user_client = Client(session_name=str(user_session_string))

        with user_client:
            while True:
                print("[INFO] Starting bot status check...")

                # Split string bot_usernames_str menjadi list bot_usernames
                bot_usernames = bot_usernames_str.split() if bot_usernames_str else []

                # Siapkan teks edit yang akan diperbarui di saluran/grup
                edit_text = f"🤖 Bot Status Updates 🤖\n\nLast Checked: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

                # Periksa status keaktifan setiap bot
                for bot_username in bot_usernames:
                    print(f"[INFO] Checking status for @{bot_username}")
                    if check_bot_status(user_client, bot_username):
                        edit_text += f"\n\n🟢 @{bot_username} is Active"
                    else:
                        edit_text += f"\n\n🔴 @{bot_username} is Inactive"

                # Tambahkan waktu terakhir pembaruan ke teks edit
                edit_text += f"\n\nLast Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

                # Split string status_message_ids_str menjadi list status_message_ids
                status_message_ids = [int(i.strip()) for i in status_message_ids_str.split(' ')] if status_message_ids_str else []

                # Perbarui status di saluran/grup
                update_status(user_client, update_channel, status_message_ids, edit_text)

                # Tunggu 1 jam sebelum memeriksa status lagi
                time.sleep(3600)  # 1 jam = 3600 detik
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
