import pandas as pd
import asyncio
import os
import logging
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

if not api_id or not api_hash:
    raise ValueError("Please set TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables in the .env file.")

client = TelegramClient('bot', api_id, api_hash)

channel_username = os.getenv('CHANNEL_NAME')

async def main():
    try:
        channel = await client.get_entity(channel_username)
        
        limit = 100
        offset_id = 0
        all_messages = []

        logging.info("Starting to fetch messages from channel: %s", channel_username)
        
        while True:
            try:
                messages = await client.get_messages(channel, limit=limit, offset_id=offset_id)
                if not messages:
                    break
                
                for message in messages:
                    if message.text:
                        all_messages.append((message.date, message.text))
                
                offset_id = messages[-1].id
                logging.info("Fetched %d messages, total collected: %d", len(messages), len(all_messages))
                
                await asyncio.sleep(1)
            
            except FloodWaitError as e:
                logging.warning("Rate limit hit, sleeping for %d seconds", e.seconds)
                await asyncio.sleep(e.seconds)

        data = {
            "date": [msg[0] for msg in all_messages],
            "content": [msg[1] for msg in all_messages]
        }
        df = pd.DataFrame(data)
        
        output_file = 'exports/listing-raw-data.csv'
        df.to_csv(output_file, index=False)
        logging.info("Messages saved to %s", output_file)
    
    except Exception as e:
        logging.error("An error occurred: %s", e)

with client:
    client.loop.run_until_complete(main())
