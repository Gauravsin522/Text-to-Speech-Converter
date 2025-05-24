# Flask app
from text_to_speech.exception import TTSException 
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from text_to_speech.components.get_accent import get_accent_tld, get_accent_message
import sys
from text_to_speech.components.textTospeech import TTSapplication


app = Flask(__name__)

CORS(app)

@app.route('/')
@cross_origin
def home():
    try:
        accent_list = get_accent_message()
        return render_template("index.html",accent_list = accent_list)
    
    except Exception as e:
        raise TTSException(e,sys)