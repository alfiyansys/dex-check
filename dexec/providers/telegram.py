from dataclasses import dataclass

import requests

from dexec.notifications import NotificationProviderInterface


@dataclass
class TelegramNotificationProvider(NotificationProviderInterface):
    token: str
    chat_id: str
    base_url: str = 'https://api.telegram.org/botTELEGRAM_TOKEN/sendMessage'

    def __post_init__(self):
        self.base_url = self.base_url.replace("TELEGRAM_TOKEN", self.token)

    def send(self, msg: str) -> bool:
        data = {'chat_id': self.chat_id, 'text': msg}

        res = requests.post(url=self.base_url, data=data)
        if res.status_code != requests.codes.ok:
            return False

        return True
