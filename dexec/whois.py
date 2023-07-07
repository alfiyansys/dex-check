import traceback
from datetime import datetime, date

from whois import parser, whois


def get_expiration_date(host: str) -> date | None:
    try:
        domain_info: parser.WhoisEntry = whois(host)
        exp_datetime: datetime.date = domain_info.get("expiration_date")
        if exp_datetime is not None:
            return exp_datetime.date()
    except parser.PywhoisError:
        traceback.print_exc()
    return None
