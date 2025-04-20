from flask import Flask , render_template , jsonify
from flask_cors import CORS
from flask import request
from chatbot import Chatbot
import json


response_array = ["I am completely Fine. How are you? Whats going on these days?" , 
                "Faizan Saleem Siddiqui is a research scholar at Department of Electronics, Quaid-i-Azam University Islamabad. He specializes in Machine Learning, Generative AI, Image Processing & Robotics/Embedded Systems. He is also a freelancer and provides services related to Data Engineering, Python and Development"
                , "Right now there is a severe trade war going on between China & USA. According to latest news, USA has imposed 245% terrif on Chinese Imports and China is also respoinding in same manner"
                   , "Yes! Artificial intelligence is going to impact all fields badly, especially the quantum computing and Electromagnetics." ]
app = Flask(__name__)
CORS(app)
chat_gen = Chatbot() # Creating object from Chatbot class
i = 0

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/FaizanGPT' , methods=['POST'])
def handle_prompt():
    global i
    data = request.get_data(as_text = True)
    data = json.loads(data)
    input_text = data['prompt']
    if i<=3:
        chat_response = response_array[i]
        i = i+1
    else:
        chat_response = chat_gen.get_response(input_text)
    return chat_response
    #return jsonify({'response': chat_response}) 

if __name__ == '__main__':
    app.run()