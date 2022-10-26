from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)

@app.route('/')
def page_index():
    candidates = get_all()
    return f'<pre>{candidates}</pre>'

@app.route('/candidates/<int:pk>')
def page_candidate(pk):
    return get_by_pk(pk)

@app.route('/skills/<skill>')
def page_skill(skill):
    return get_by_skill(skill)

app.run(host='127.0.0.1', port=5000)