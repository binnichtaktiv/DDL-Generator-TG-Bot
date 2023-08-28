import telebot
import re
import time
import requests

TOKEN = "6536016456:AAHripTlVqChSqcJF5vPIlFBYaMk_-68zD4"
bot = telebot.TeleBot(TOKEN, threaded=False)

def get_ddl_from_location(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 ... (Ihr User-Agent)',
        'Referer': url  
    }
    
    data = {
        'op': 'download2',
        'id': url.split('/')[-1],
    }

    response = requests.post(url, headers=headers, data=data, allow_redirects=False)
    ddl_link = response.headers.get('location')
    return ddl_link

def create_direct_download_link(link):
    if "sharepoint.com" in link and "?e=" in link:
        return link.split("?e=")[0] + "?download=1"
    elif "onedrive.live.com/embed" in link:
        return link.replace("/embed?", "/download?")
    return "Unsupported link type"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, "Hi! I can convert Userscloud, SharePoint, and normal personal OneDrive download links to direct download links. Just send me your link! If you use a 'normal' personal OneDrive account then do a right-click on the file and click 'embed' then generate HTML code. Copy the code and send it. If you don't have that option (SharePoint account) then click on share and copy the link and send it to me\n\nMade by @binnichtaktiv\nhttps://binnichtaktiv.github.io")    
    except Exception as e:
        print("Error sending message:", e)

@bot.message_handler(func=lambda m: True)
def process_link(message):
    try:
        iframe_match = re.search(r'iframe src="([^"]+)"', message.text)
        if iframe_match:
            url = iframe_match.group(1)
        else:
            url = message.text
        
        if "userscloud.com" in url:
            ddl = get_ddl_from_location(url)
            if ddl:
                ddl_encoded = ddl.replace(" ", "%20")
                bot.reply_to(message, ddl_encoded)
            else:
                bot.reply_to(message, "Couldn't retrieve the direct download link...🚫 Please check the link and try again.")
        elif "sharepoint.com" in url or "onedrive.live.com" in url:
            ddl_link = create_direct_download_link(url)
            bot.reply_to(message, ddl_link)
        else:
            bot.reply_to(message, "Please provide a valid link.😡")
    except Exception as e:
        print("Error processing message:", e)

while True:
    try:
        bot.polling(none_stop=True, interval=3)
    except Exception as e:
        print("Bot crashed. Restarting...")
        time.sleep(10)
