from flask import Blueprint, render_template, jsonify, request, url_for
import os
from dotenv import load_dotenv, dotenv_values
#from ControllerBase import ControllerBase

chat_blue = Blueprint('chatbot', __name__,template_folder='Controller', url_prefix='/chatbot')

class ChatBot:

    def __init__(self):
        #load_dotenv()
        pass
    
    @chat_blue.route("/")
    def index():
        return 'None'

    #def listarRutas(self):
    @chat_blue.route("/key", methods = ['GET'])
    def getKey():
        listado = {            
            'key' : dotenv_values(".env").get("API_KEY")
        }

        return jsonify(listado)