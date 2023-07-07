import os
from datetime import datetime, date
from typing import List, Tuple

from dexec import Config
from dexec.whois import get_expiration_date


def run():
    config_file_path = os.getenv("CONFIG_FILE", "config.ini")
    cfg = Config.parse_from_ini_file(config_file_path)
    notif_interface = cfg.notification_provider

    date_today = datetime.now().date()

    expiring_domains: List[Tuple[str, date, int]] = []
    for domain in cfg.domain_list:
        exp_date = get_expiration_date(domain.strip())
        if exp_date is None:
            continue

        days_before_expiry = (exp_date - date_today).days
        if days_before_expiry <= cfg.reminder_days_threshold:
            expiring_domains.append((domain, exp_date, days_before_expiry))

    message = 'The following TLD domains are expiring soon:\n\n'

    for domain_name, exp_date, days_before_expiry in expiring_domains:
        message += f'{domain_name} - Active until: {exp_date.strftime("%Y-%m-%d")} ({days_before_expiry} days left)\n'

    print(message)

    if notif_interface is not None:
        notif_interface.send(message)
