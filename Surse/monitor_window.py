import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, QProcess

class MonitorThread(QThread):
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)
    
    def __init__(self, script, args, parent=None):
        super().__init__(parent)
        self.script = script
        self.args = args
        self.process = None

    def run(self):
        if os.path.exists(self.script):
            self.process = QProcess()
            self.process.setProcessChannelMode(QProcess.MergedChannels)
            self.process.readyReadStandardOutput.connect(self.handle_output)
            self.process.readyReadStandardError.connect(self.handle_error)
            self.process.finished.connect(self.process_finished)
            self.process.start(self.script, self.args)
            self.process.waitForFinished(-1)
        else:
            self.output_signal.emit(f"Scriptul {self.script} nu a fost gasit!")

    def handle_output(self):
        data = self.process.readAllStandardOutput()
        text = data.data().decode()
        self.output_signal.emit(text)

    def handle_error(self):
        data = self.process.readAllStandardError()
        text = data.data().decode()
        self.error_signal.emit(text)

    def process_finished(self):
        self.output_signal.emit("Procesul s-a terminat.")

class MonitorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitorizare in timp real")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setStyleSheet("background-color: black; color: green;")
        self.setCentralWidget(self.text_edit)

        self.monitor_thread = None

    def start_monitoring(self, script, *args):
        self.monitor_thread = MonitorThread(script, args)
        self.monitor_thread.output_signal.connect(self.append_text)
        self.monitor_thread.error_signal.connect(self.append_text)
        self.monitor_thread.start()

    def append_text(self, text):
        self.text_edit.append(text)
        self.text_edit.verticalScrollBar().setValue(self.text_edit.verticalScrollBar().maximum())


