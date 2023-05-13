import datetime
import configparser
import requests
import whois

# Read configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Telegram API credentials and chat ID
telegram_token = config['TELEGRAM']['token']
telegram_chat_id = config['TELEGRAM']['chat_id']

# List of TLD domains to monitor
tld_domains = config['DOMAINS']['tld_domains'].split(',')

# Check active status for each domain
today = datetime.datetime.now().date()
expiry_threshold = today + datetime.timedelta(days=30)

expiring_domains = []

for domain in tld_domains:
    domain_name = domain.strip()
    
    try:
        domain_info = whois.whois(domain_name)
    except Exception:
        continue
    
    active_until_date = domain_info.expiration_date
    
    if active_until_date is not None:
        if isinstance(active_until_date, list):
            active_until_date = active_until_date[0]
        active_until_date = active_until_date.date()
        days_to_expiry = (active_until_date - today).days
        
        if days_to_expiry <= 30:
            expiring_domains.append((domain_name, active_until_date, days_to_expiry))

# Send notification to Telegram if any domain is expiring
if expiring_domains:
    message = 'The following TLD domains are expiring soon:\n\n'
    
    for domain in expiring_domains:
        message += f'{domain[0]} - Active until: {domain[1].strftime("%Y-%m-%d")} ({domain[2]} days left)\n'
    
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {'chat_id': telegram_chat_id, 'text': message}
    requests.post(url, data=data)