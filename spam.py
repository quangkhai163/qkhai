from pyrogram import Client, filters
import random
import asyncio

api_id = 22916903
api_hash = "c448d258290ecf3e5971b7445ffaebc9"
OWNER_ID = 5976243149

app = Client("funny_bot", api_id=api_id, api_hash=api_hash)

funny_insults_template = [
    "địt con mẹ m🤓☝️ {user}",
    "địt con mẹ m bại não à em {user}",
    "ai cho m chạy 😏 {user}",
    "sủa tiếp đi em {user}",
    "loại m đem so với chó nó còn hơn m {user}",
    "m không có mom à em {user}",
    "chạy đâu rồi th ngu {user}",
    "địt cả dòng nhà m {user}",
    "địt con mẹ m tật não à em {user}",
    "suar lên cho cha nghe coi {user}",
    "méc mẹ đi em {user}",
    "ảo ửa với cha à {user}",
    "cha nhây để m đột tử đó con {user}",
    "nhanh đi con chậm quá {user}",
    "gái mẹ m đâu r em {user}",
    "sủa đi {user}",
    "hăng lên {user}",
    "tật ngôn à con me m {user}",
    "đâu rồi th kid {user}",
    "anh địt cả dòng nhà m đó em {user}",
    "ngu lồn {user}",
    "chó nó còn khôn hơn m {user}",
    "chạy là anh chịch chết gái mẹ m đó {user}",
    "nhanh em hiếu ơi war 11 nè {user}",
    "speed lewn em {user}",
    "nhanh anh đợi {user}",
    "nhanh đi em địt mẹ m {user}",
    "chơi chết con gái mẹ m đó {user}",
    "ngôn đâu em {user}",
    "tật ngôn à {user}",
    "cha chơi chết cả dòng tổ nhà m đó!! {user}"
]

spamming_chats = {}

@app.on_message(filters.command("war") & filters.user(OWNER_ID))
async def start_war(client, message):
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) < 2 or not args[1].startswith("@"):
        await message.reply("❌ Bạn phải dùng cú pháp: /war @username")
        return

    target_user = args[1]

    if chat_id in spamming_chats and spamming_chats[chat_id]:
        await message.reply("⚠ War đang diễn ra.")
        return

    spamming_chats[chat_id] = True
    await message.reply(f"🔥 Bắt đầu war {target_user} — dùng /stop để dừng.")

    while spamming_chats[chat_id]:
        try:
            text = random.choice(funny_insults_template).format(user=target_user)
            await client.send_message(chat_id, text)
            await asyncio.sleep(0.1)
        except Exception as e:
            print(f"Lỗi gửi tin nhắn: {e}")
            await asyncio.sleep(1)

@app.on_message(filters.command("stop") & filters.user(OWNER_ID))
async def stop_war(client, message):
    chat_id = message.chat.id
    spamming_chats[chat_id] = False
    await message.reply("🛑 Đã dừng war.")

@app.on_message(filters.command("clear") & filters.user(OWNER_ID))
async def clear_my_messages(client, message):
    chat_id = message.chat.id
    await message.reply("🧹 Đang dọn dẹp...")

    deleted = 0
    async for msg in app.iter_history(chat_id, limit=1000):
        if msg.from_user and msg.from_user.id == OWNER_ID:
            try:
                await msg.delete()
                deleted += 1
            except Exception as e:
                print(f"Không thể xóa tin nhắn: {e}")
    await client.send_message(chat_id, f"✅ Đã xóa {deleted} tin nhắn.")

app.run()