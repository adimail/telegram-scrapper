# telegram-scrapper

This script allows you to scrape messages from a Telegram channel and save them to a CSV file.

---

## Installation

Clone this repository to your local machine:

```shell
git clone https://github.com/adimail/telegram-scrapper.git
```

Install the required dependencies:

```shell
pip3 install -r requirements.txt
```

## Setting up .env file

Before running the script, you need to set up a `.env` file to store your Telegram API credentials and channel information.

Create a file named .env in the project directory. Refer the .env.example file for reference

Add the following lines to your the .env file:

```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
CHANNEL_NAME=your_channel_username
```

Replace your_api_id, your_api_hash, and your_channel_username with your actual Telegram API credentials and channel username.

## Running the Script

To run the script, simply execute the main.py file:

```shell
python main.py
```

> The script will start fetching messages from the specified Telegram channel and save them to a CSV file named listing-raw-data.csv in the exports directory.
