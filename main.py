import os
from slackclient import SlackClient
slack_client = SlackClient(os.environ.get('SLACK_TOKEN', None))
slack_client.api_call("api.test")
