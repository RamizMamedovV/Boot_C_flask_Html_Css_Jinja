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

@app.route('/test/')        # """ многострочгая"""
def say_test():
    html = """
    <h1>Hello Ra</h1>
    <br>
    <br>
    <p>Text</p>
    """
    return html

@app.route('/test1/')           # 'однострочная запись'
def say_test1():
    name = 'Ra'
    html = f'<h1>Hello {name}</h1><br><br><p>Text</p>'
    return html

if __name__ == '__main__':
    app.run()