from pyrogram import Client, InlineKeyboardButton, InlineKeyboardMarkup
import tgcrypto, os
from googlesearch import search 

def dl(input):
	search_input = input
	for song_url in search(search_input+'Lyrical YouTube', tld="co.in", num=1, stop=1, pause=1):
		command = f"youtube-dl -o '{input}.mp3' -f 'bestaudio[ext=m4a]' {song_url}"
		os.system(command)
		
welcome_msg = "Hello {} 👋\n\nI'm iSong Downloader Bot🎵\n\n**How to use me** ❓\nCommand : /song (song_name)\n\nExample : `/song let me love you`\nExample2: `/song Baby by Justin Bieber`"

app = Client("iSongDL_Bot", api_id=938340, api_hash="4c47ceee0c51daa3e6608dd728c6148d", bot_token="1624907624:AAHe4LwnAC7sLbiyWQJq-5l6uq4BchytHe4")

@app.on_message(Filters.command(['start', 'help']))

def download(client, message):
	name = message.from_user.first_name
	message.reply_text(f"{welcome_msg}".format(name))
	
@app.on_message(Filters.command(['song']))

def download(client, message):
	cmd = message.text[6:]
	msg = message.reply_text(f"__Searching For__ **{cmd}** __on YouTube.com__")
	dl(cmd)
	msg.edit(f"__Uploading__ **{cmd}.mp3** __To Telegram__")
	file = cmd + '.mp3'
	message.reply_audio(file, caption=f"🎵 Song - {cmd}\n\nUploaded by @iSongDL_bot")
	
app.run()
