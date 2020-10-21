import logging
from flask import Flask
app = Flask(__name__)


import re
import random

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/newroute/<prompt>')
def ask(prompt): 
    answer_list = {
    '.*hello.*|.*hi.*|wh*at*.*s+.*u+p+': [
        'Hello! How can I help you?',
        'Hello! Ask me questions about Duke Basketball!'
        ],
    '(.*)?are you(.*)?':[
        'This is an auto chatbox. Ask me questions about Duke Basketball!',
        'Don not ask tricky questions to a machine.',
        'Leave me alone plz'
        ],
    '(.*)?you do(.*)?': [
        'Ask me questions about Duke Basketball',
        'I am here to help answer Duke Basketball realted questions~'
        ],
    '(who|name).*(coach)':[
        'Mike Krzyzewski'
        ],
    '.*how long.*m*i*k*e*':[
        '40 years.'
        ],
    '.*where.*':[
        'Cameron Indoor Stadium'
        ],
    '.*mascot.*':[
        'Blue Devil'
        ],
    'k.*ville':[
        'A phenomenon that occurs before major men basketball games at Duke University. In simplest terms, it is the line for undergraduate students wishing to gain access to the designated tenting games.'
        ]
        }

    default = [
    'Hmmmm, sorry I am not sure what you are asking for!'
    ]

    matched = 0
    for pattern in answer_list:
        if re.search(pattern,prompt.lower()):
            matched = 1
            ans = random.choice(answer_list[pattern])
            pass
        if matched == 0:
            ans = random.choice(default)
            pass
        pass
    return print(f'prompt: {prompt}\nanswer: {ans}',sep='\n')

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)



