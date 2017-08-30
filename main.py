import os

from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import slackweb

app = Flask(__name__)

slack = slackweb.Slack(url=os.environ.get('SLACK_WEBHOOK', None))
twilio_clint = Client()

@app.route('/twilio', methods=['POST'])
def twilio_post():
    from_phone = request.form['From']
    message = from_phone + ' ' + request.form['Body']
    slack.notify(channel="#harvey-shelters",
                 text=message, username="shelterbot",
                 icon_emoji=':house:')

    response = MessagingResponse()
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
