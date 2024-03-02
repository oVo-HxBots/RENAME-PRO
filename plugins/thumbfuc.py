from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("😔 __**𝚈𝙾𝚄 𝙳𝙾𝙽𝚃 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻**__")
	
	 
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("❌️ __**𝚈𝙾𝚄𝚁 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙴𝙻𝙴𝚃𝙴𝙳**__")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("✅️ __**𝚈𝙾𝚄𝚁 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝚂𝙰𝚅𝙴𝙳**__")
