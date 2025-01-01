import logging
from typing import Annotated

import typer
import requests
from requests.exceptions import RequestException

from pinger.dotenv import load_dotenv


class Bot:
    def __init__(self, owner_id: int, token: str):
        self.owner_id = owner_id
        self.token = token

    def get_me(self):
        url = f"https://api.telegram.org/bot{self.token}/getMe"
        response = requests.get(url)
        return response.json()

    def send_message(self, chat_id: int, text: str):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text
        }
        response = requests.post(url, data=data)
        return response.json()


def main(
        url: Annotated[str, typer.Argument(...)],
        bot_owner_id: Annotated[int, typer.Argument(envvar=["BOT_OWNER_ID"])],
        bot_token: Annotated[str, typer.Argument(envvar=["BOT_TOKEN"])],
        send_ok: Annotated[bool, typer.Option("--send-ok")] = False,
):
    bot = Bot(owner_id=bot_owner_id, token=bot_token)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            if send_ok:
                bot.send_message(bot_owner_id, f"✅ {url} is up!")
        else:
            bot.send_message(bot_owner_id,
                             f"🚨{url} is down! Status code: {response.status_code}. Text: {response.text}")
    except RequestException as e:
        bot.send_message(bot_owner_id, f"🚨{url} is down! Exception: {str(e)}")


if __name__ == '__main__':
    load_dotenv()
    typer.run(main)
