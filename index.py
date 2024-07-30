from flask import Flask, Blueprint, redirect, render_template, url_for, request
from Controller.Cine import cine_blue
from Controller.Pelicula import pelicula_blue
from Controller.API import api_blue
from Controller.ChatBot.ChatBot import chat_blue


app = Flask(__name__)

app.config['BASE_URL'] = 'http://127.0.0.1:5000'

app.register_blueprint(cine_blue)
app.register_blueprint(pelicula_blue)
app.register_blueprint(api_blue)
app.register_blueprint(chat_blue)

@app.context_processor
def inject_base_url():
    return dict(base_url=app.config['BASE_URL'])



@app.route("/")
def index():
    return render_template("base/index.html")




if __name__ =="__main__":
  
    app.run(debug = True)

