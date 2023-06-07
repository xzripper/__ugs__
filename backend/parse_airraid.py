from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest

from backend.tg import *

from backend.sources import *



def parse_rockets_alert(max_parse):
    out = []

    with TelegramClient(SESSION, API_ID, API_HASH) as client:
        for source in ROCKETS:
            for rocket_inf in client.iter_messages(source, max_parse):
                out.append(rocket_inf.text)

    return list(reversed(out))

def parse_alerts(max_parse):
    out = []

    with TelegramClient(SESSION, API_ID, API_HASH) as client:
        for source in ALERT:
            for alert_inf in client.iter_messages(source, max_parse):
                out.append(alert_inf.text)

    return list(reversed(out))
