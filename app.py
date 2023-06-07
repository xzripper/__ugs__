from flask import Flask, render_template

from telethon import TelegramClient

from asyncio import new_event_loop, set_event_loop

from backend.parse_airraid import *
from backend.analyzer import analyze_rocket_alert, analyze_alert


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/alertinformer/')
def alertinformer():
    set_event_loop(new_event_loop())

    rocket_alerts = parse_rockets_alert(10)
    alerts = parse_alerts(20)

    analyzed_rocket_alerts = []
    analyzed_alerts = []

    for rocket_alert in rocket_alerts:
        _analyzed = analyze_rocket_alert(rocket_alert)

        if _analyzed is not None:
            analyzed_rocket_alerts.append(_analyzed)

    for alert in alerts:
        _analyzed = analyze_alert(alert)

        if _analyzed is not None:
            analyzed_alerts.append(_analyzed)

    return render_template('alertinformer.html', rocket_alerts=analyzed_rocket_alerts, alerts=analyzed_alerts)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
