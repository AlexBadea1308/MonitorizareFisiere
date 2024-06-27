import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QLineEdit, QFileDialog, QGridLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal

class DatabaseToolsWindow(QMainWindow):
    def __init__(self, directory, db_file, main_window):
        super().__init__()
        self.directory = directory
        self.db_file = db_file
        self.main_window = main_window
        self.setWindowTitle("Database Tools")
        self.setGeometry(100, 100, 800, 600)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: black;
            }
            QPushButton {
                background-color: blue;
                color: black;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
            }
            QLabel {
                color: white;
                font-size: 16px;
            }
            QLineEdit {
                background-color: white;
                color: black;
                font-size: 16px;
                padding: 5px;
                border-radius: 5px;
            }
            QTextEdit {
                background-color: black;
                color: green;
                font-size: 16px;
                border-radius: 5px;
            }
        """)
        
        layout = QVBoxLayout()

        self.view_events_button = QPushButton("Vizualizaeaza evenimente")
        self.view_events_button.clicked.connect(self.view_events)
        layout.addWidget(self.view_events_button)

        self.view_comments_button = QPushButton("Vizualizeaza comentarii")
        self.view_comments_button.clicked.connect(self.view_comments)
        layout.addWidget(self.view_comments_button)

        self.add_comment_button = QPushButton("Adauga comentariu")
        self.add_comment_button.clicked.connect(self.add_comment)
        layout.addWidget(self.add_comment_button)

        self.delete_events_button = QPushButton("Sterge eveniment")
        self.delete_events_button.clicked.connect(self.delete_events)
        layout.addWidget(self.delete_events_button)

        self.delete_comments_button = QPushButton("Sterge comentariu")
        self.delete_comments_button.clicked.connect(self.delete_comments)
        layout.addWidget(self.delete_comments_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close_window)
        layout.addWidget(self.exit_button)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def view_events(self):
        if os.path.isdir(self.directory) and os.path.isfile(self.db_file):
            self.run_script('view_events.sh', self.directory, self.db_file)
        else:
            QMessageBox.warning(self, "Error", "Directorul si baza de date nu sunt valide.")
    
    def view_comments(self):
        if os.path.isdir(self.directory) and os.path.isfile(self.db_file):
            self.run_script('view_comments.sh', self.directory, self.db_file)
        else:
            QMessageBox.warning(self, "Error", "Directorul si baza de date nu sunt valide.")

    def add_comment(self):
        self.add_comment_window = AddCommentWindow(self.directory, self.db_file)
        self.add_comment_window.comment_added.connect(self.on_comment_added)
        self.add_comment_window.show()

    def delete_events(self):
        self.delete_window = DeleteWindow(self.directory, self.db_file, "delete_events.sh", "Delete Event", "Event ID:")
        self.delete_window.action_performed.connect(self.on_action_performed)
        self.delete_window.show()

    def delete_comments(self):
        self.delete_window = DeleteWindow(self.directory, self.db_file, "delete_comments.sh", "Delete Comment", "Comment ID:")
        self.delete_window.action_performed.connect(self.on_action_performed)
        self.delete_window.show()

    def close_window(self):
        self.close()
        if self.main_window:
            self.main_window.show()

    def run_script(self, script_name, *args):
        self.output_text.append(f"Scriptul curent: {script_name}")
        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(script_dir, script_name)
        process = subprocess.Popen([script_path] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            self.output_text.append(stdout.decode())
        if stderr:
            self.output_text.append(stderr.decode())

    def on_comment_added(self, comment):
        self.output_text.append(f"Comentariu adaugat: {comment}")

    def on_action_performed(self, message):
        self.output_text.append(message)

class AddCommentWindow(QMainWindow):
    comment_added = pyqtSignal(str)

    def __init__(self, directory, db_file):
        super().__init__()
        self.directory = directory
        self.db_file = db_file
        self.setWindowTitle("Comentariu Adaugat")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        self.event_id_label = QLabel("EvenimentID:")
        grid_layout.addWidget(self.event_id_label, 0, 0)
        self.event_id_edit = QLineEdit()
        grid_layout.addWidget(self.event_id_edit, 0, 1)

        self.first_name_label = QLabel("Nume:")
        grid_layout.addWidget(self.first_name_label, 1, 0)
        self.first_name_edit = QLineEdit()
        grid_layout.addWidget(self.first_name_edit, 1, 1)

        self.last_name_label = QLabel("Prenume:")
        grid_layout.addWidget(self.last_name_label, 2, 0)
        self.last_name_edit = QLineEdit()
        grid_layout.addWidget(self.last_name_edit, 2, 1)

        self.comment_label = QLabel("COmentariu:")
        grid_layout.addWidget(self.comment_label, 3, 0)
        self.comment_edit = QLineEdit()
        grid_layout.addWidget(self.comment_edit, 3, 1)

        self.date_label = QLabel("Date:")
        grid_layout.addWidget(self.date_label, 4, 0)
        self.date_edit = QLineEdit()
        grid_layout.addWidget(self.date_edit, 4, 1)

        layout.addLayout(grid_layout)

        self.add_comment_button = QPushButton("Add Comment")
        self.add_comment_button.clicked.connect(self.add_comment)
        layout.addWidget(self.add_comment_button)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_comment(self):
        event_id = self.event_id_edit.text()
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        comment = self.comment_edit.text()
        date = self.date_edit.text()
        if event_id and first_name and last_name and comment and date:
            self.run_script('add_comment.sh', self.directory, self.db_file, event_id, first_name, last_name, comment, date)
        else:
            self.output_text.append("Completeaza toate campurile.")

    def run_script(self, script_name, *args):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(script_dir, script_name)
        process = subprocess.Popen([script_path] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            self.output_text.append(stdout.decode())
        if stderr:
            self.output_text.append(stderr.decode())
        if process.returncode == 0:
            self.comment_added.emit(f"Event ID: {args[2]}, Comment: {args[5]}")

class DeleteWindow(QMainWindow):
    action_performed = pyqtSignal(str)

    def __init__(self, directory, db_file, script_name, title, id_label_text):
        super().__init__()
        self.directory = directory
        self.db_file = db_file
        self.script_name = script_name
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        self.id_label = QLabel(id_label_text)
        grid_layout.addWidget(self.id_label, 0, 0)
        self.id_edit = QLineEdit()
        grid_layout.addWidget(self.id_edit, 0, 1)

        layout.addLayout(grid_layout)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_item)
        layout.addWidget(self.delete_button)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def delete_item(self):
        item_id = self.id_edit.text()
        if item_id:
            self.run_script(self.script_name, self.directory, self.db_file, item_id)
        else:
            self.output_text.append("Completeaza campul de ID.")

    def run_script(self, script_name, *args):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(script_dir, script_name)
        process = subprocess.Popen([script_path] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            self.output_text.append(stdout.decode())
        if stderr:
            self.output_text.append(stderr.decode())
        if process.returncode == 0:
            self.action_performed.emit(f"Ati sters cu succes! : {args[2]}")
