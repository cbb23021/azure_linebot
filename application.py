"""
Object detection and image description on LINE bot
"""
from datetime import datetime, timezone, timedelta
import os
import re
import json
import requests
from flask import Flask, request, abort
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FlexSendMessage,
    ImageMessage,
)
from imgur_python import Imgur
from PIL import Image, ImageDraw, ImageFont
import time

app = Flask(__name__)
LINE_SECRET = "d2abd6336bb6578a321bcb9e9070cd4f"]
LINE_TOKEN = "kE9Z0tufekB1YcCXp2y/UbwhO7O5Nw+bKrEpuxHVWXuS03iHFlccd0YFQnMtLMsOBibZCj0nozVc9P1W6BZRNT0r22ZkgocgLfrotK3T9CadyKPeVApvWh/yzm6NWBYQf4u22rG4KhU1Ph8VDQt2uQdB04t89/1O/w1cDnyilFU="
LINE_BOT = LineBotApi(LINE_TOKEN)
HANDLER = WebhookHandler(LINE_SECRET)

@app.route("/callback", methods=["POST"])
def callback():
    # X-Line-Signature: 數位簽章
    signature = request.headers["X-Line-Signature"]
    print(signature)
    body = request.get_data(as_text=True)
    print(body)
    try:
        HANDLER.handle(body, signature)
    except InvalidSignatureError:
        print("Check the channel secret/access token.")
        abort(400)
    return "OK"


@app.route("/")
def hello():
    "hello world"
    return "Hello World!!!!!"