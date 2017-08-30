import os

from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from slackclient import SlackClient

app = Flask(__name__)

slack_client = SlackClient(os.environ.get('SLACK_TOKEN', None))
twilio_clint = Client()

@app.route('/twilio', methods=['POST'])
def twilio_post():
    response = MessagingResponse()
    request.form['From']
    message = request.form['Body']
    slack_client.api_call("chat.postMessage", channel="#harvey-shelters",
                          text=message, username="shelterbot",
                          icon_emoji=':house:')

    return Response(response.toxml(), mimetype="text/xml"), 200

if __name__ == '__main__':
    app.run(debug=True)
