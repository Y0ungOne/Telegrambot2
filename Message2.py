import telegram
import asyncio
import schedule
import pytz
import datetime
token = "6681938922:AAFRSj7tRd1F7LlIXsBTq-IZL-B0FMpEaTM" 
chat_id="6727996641"
bot = telegram.Bot(token = token)
public_chat_name="@T231110"

async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    text = "30분마다 메세지 전송, 11:00 pm ~ 06:00 am 출력 금지"

    if now.hour >= 23 or now.hour <= 6: # 11:00 pm ~ 06:00 am 메세지 출력 금지
        return
    await bot.sendMessage(public_chat_name,text="알람임")

async def run():
    while True:
        await job()
        await asyncio.sleep(1800) # 30분 단위로 메세지 전송
        


if __name__ == "__main__":
    asyncio.run(run())
    