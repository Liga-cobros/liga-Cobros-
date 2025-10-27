# Sistema Flask principal - simplificado
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Sistema Liga Chaves Online'

if __name__ == '__main__':
    app.run(debug=True)