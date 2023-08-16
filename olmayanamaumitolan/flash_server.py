from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_function')
def run_function():
    # Bu kısımda yapılacak işlemleri gerçekleştirebilirsiniz
    return "Python fonksiyonu çalıştırıldı!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
