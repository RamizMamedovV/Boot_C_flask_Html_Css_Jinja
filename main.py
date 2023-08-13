from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return 'Hello!'

@app.route('/bye/')
def say_bye():
    return 'Bye!'

@app.route('/Amina/')
def say_Amına():
    return 'Hello Amişkam!'

@app.route('/Amin/')
def say_Amin():
    return 'Hello Aminçik!'

@app.route('/<name>/')      # при вводе любого текста воспринимает как name
def say_name(name = 'noname'):
    return f'Hello-> {name}!'

@app.route('/Amin1/') # Одна View может декорироваться разными декораторами
@app.route('/Amin2/')
@app.route('/Amin3/')
def say_Amin1():
    return 'Hello Aminçik!'

if __name__ == '__main__':
    app.run()