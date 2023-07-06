import configparser
from typing import List, NamedTuple

from dexec.notifications import NotificationProviderInterface
from dexec.providers import TelegramNotificationProvider, ConsoleNotificationProvider


class Config(NamedTuple):
    domain_list: List
    notification_provider: NotificationProviderInterface
    reminder_days_threshold: int

    @staticmethod
    def parse_from_ini_file(filename: str):
        config = configparser.ConfigParser()
        config.read(filename)

        notification_provider_type = config.get('APP', 'notification_provider')

        notification_dict = {
            'telegram': TelegramNotificationProvider(
                token=config.get('TELEGRAM', 'token', fallback=None),
                chat_id=config.get('TELEGRAM', 'chat_id', fallback=None)
            ),
            'console': ConsoleNotificationProvider()
        }

        notification_provider = notification_dict.get(notification_provider_type, None)

        reminder_days_threshold = config.getint("DOMAINS", "reminder_day")
        domain_list = [
            domain.strip()
            for domain in config.get('DOMAINS', 'tld_domains').split(',')
        ]

        return Config(domain_list, notification_provider, reminder_days_threshold)
