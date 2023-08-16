import sys
import subprocess
import threading
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

with open("log.txt", "w") as f:
    f.write("")

app = QApplication(sys.argv)
window = QMainWindow()
webview = QWebEngineView()
window.setCentralWidget(webview)
window.setWindowTitle("MdlEdit For Goldsrc")
webview.load(QUrl("http://127.0.0.1:5000/"))
window.show()

flask_process = None  # Flask subprocess'i tutmak için değişken

def start_flash_server():
    global flask_process
    cmd = f'python flash_server.py'
    flask_process = subprocess.Popen(['python', 'flash_server.py'])

flash_server_thread = threading.Thread(target=start_flash_server)
flash_server_thread.start()

def stop_flash_server():
    if flask_process:
        flask_process.terminate()
        flask_process.wait()

app.aboutToQuit.connect(stop_flash_server)  # PyQt5 kapanırken Flask sunucusunu durdur

sys.exit(app.exec_())
