# keylogger
Bu proje, Python kullanarak klavye tuş basımlarını kaydeden ve her cümle tamamlandığında (Enter tuşuna basıldığında veya log uzunluğu belirli bir değeri aştığında) bu logları bir Telegram botu aracılığıyla gönderir.

## Nasıl Çalışır?

- **Tuş Dinleme:** Proje, `pynput` kütüphanesini kullanarak kullanıcının tüm klavye tuş basımlarını dinler.
- **Log Biriktirme:** Her basılan tuş, bir log değişkeninde toplanır.
- **Telegram'a Gönderim:** Enter tuşuna basıldığında ya da log belirli bir uzunluğa ulaştığında, toplanan log, Telegram botu aracılığıyla hedef Chat ID’ye gönderilir.

## Özellikler

- **Normal Tuşlar:** Harfler, sayılar, noktalama işaretleri vs. düzgün bir şekilde loglanır.
- **Özel Tuşlar:** Space, Enter, Backspace, Tab, ESC, Shift, Ctrl, Alt, CapsLock, NumLock, Delete, Ok tuşları, Windows tuşu, F1-F12 gibi tuşlar tanımlanır.
- **NumPad Desteği:** NumPad üzerindeki tuşlar (0-9, *, -, +, /, . ve Enter) de doğru şekilde algılanır.
- **Telegram Entegrasyonu:** Belirlenen tetikleyiciye ulaşıldığında log, Telegram botu aracılığıyla gönderilir.
- **Hata Yönetimi:** Hatalar terminalde yazdırılır.

## Gereksinimler

- Python 3.6 veya üzeri
- `pynput` kütüphanesi
- `requests` kütüphanesi
- Bir Telegram hesabı

## Telegram Botu Oluşturma ve Chat ID Alma

1. **Telegram Botu Oluşturma:**
    - Telegram uygulamasında @BotFather ile iletişime geçin.
    - `/newbot` komutunu gönderin.
    - Botunuz için bir ad ve kullanıcı adı belirleyin.
    - BotFather size bir **bot token** verecektir. Bu token'ı bir yere not edin.
2. **Chat ID Alma:**
    - Oluşturduğunuz botu kişisel sohbetinize veya bir gruba ekleyin.
    - Botunuza bir mesaj gönderin (örneğin, `/start`).
    - Aşağıdaki URL'yi tarayıcınızda açın (bot token'ınızı ekleyin):
        
        ```
      
        https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
        
        ```
        
    - Dönen JSON verisinde `"chat": {"id": ...}` alanını bulun. Bu, chat ID'nizdir.

---

## Kullanım

1. **Projeyi Klonlayın:**
    
    ```
    
    git clone https://github.com/bilgenurt/keylogger.git
    cd keylogger
    
    ```
    
2. **`btkeylogger.py` Dosyasını Düzenleyin:**
    
    Dosya içinde aşağıdaki ayarları kendi bilgilerinizle değiştirin:
    
    - `BOT_TOKEN` : BotFather'dan aldığınız Telegram bot token'ı.
    - `CHAT_ID` : `getUpdates` komutuyla aldığınız chat ID.
3. **Betiği Çalıştırın:**
    
    Terminal veya VS Code entegre terminalinde aşağıdaki komutu çalıştırın:
    
    ```
    python keylogger.py
    ```
    
4. **Çalıştırıldığında:**
    - Terminalde "Keylogger başlatıldı..." mesajı görünecektir.
    - Klavye tuşlarına bastıkça log birikmeye başlayacaktır.
    - Enter tuşuna basıldığında veya log uzunluğu belirli bir değere (örneğin, 20 karakter) ulaştığında, log Telegram üzerinden gönderilecektir.
