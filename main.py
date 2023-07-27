from flask import Flask
from chatgpt_bot import ChatGPTBot


app = Flask(__name__)


@app.route('/')
def hello_world(text):
    return "Welcome"

@app.route('/create/<text>')
def save_input(text):
    #return text
    bot.create_prompt(prompt=text)
    return "saved successfully"

@app.route('/search/<int:index>')
def searchByInput(index):
    #return text
    return bot.get_response(index)



@app.route('/update/<int:index>/<newtext>')
def updatePromot(index,newtext):
    #return text
    
    return bot.update_prompt(index,newtext)

bot = ChatGPTBot(api_key='Your_api_key')


if __name__ == '__main__':
    app.run(debug=True)
