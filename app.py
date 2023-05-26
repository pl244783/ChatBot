from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

class ExcludeFilter(logging.Filter):
    def filter(self, record):
        message = record.getMessage()
        return "GET /static/" not in message
    
logger = logging.getLogger()
handler = logging.FileHandler('static/logFile.html', 'w')
handler.setLevel(logging.INFO)
handler.addFilter(ExcludeFilter())
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, threaded=True, debug=True)

#MAKE C: the logo NOW!!!