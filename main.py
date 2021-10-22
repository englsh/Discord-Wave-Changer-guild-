import json,requests
settings = json.loads(open("settings.json","r").read())
STICKER_ID = settings['stickerID']
CHANNEL_ID = settings['channelID']
GUILD_ID = settings['guildID']
JOIN_ID = settings['joinID']
TOKEN = settings['token']
headers = {"authorization": TOKEN}
URL = f"https://ptb.discord.com/api/v9/channels/{CHANNEL_ID}/messages"
def main():
    data = {"content":"","message_reference":{"guild_id":GUILD_ID,"channel_id":CHANNEL_ID,"message_id":JOIN_ID},"sticker_ids":[STICKER_ID]}
    r = requests.post(URL,json=data,headers=headers)
    print(r.json())
if __name__ == '__main__':
    main()
