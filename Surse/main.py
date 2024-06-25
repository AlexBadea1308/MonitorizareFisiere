import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from monitor_window import MonitorWindow
from database_meniu import DatabaseToolsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meniu Monitorizare")
        self.setGeometry(100, 100, 300, 400)
        
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
        """)

        layout = QVBoxLayout()

        self.monitor_button = QPushButton("Monitorizare un director")
        self.monitor_button.clicked.connect(self.select_directory)
        layout.addWidget(self.monitor_button)

        self.monitor_recursive_button = QPushButton("Monitorizare un director si subdirectoarele sale")
        self.monitor_recursive_button.clicked.connect(self.select_directory_recursive)
        layout.addWidget(self.monitor_recursive_button)

        self.send_email_button = QPushButton("Monitorizare + notificare email")
        self.send_email_button.clicked.connect(self.select_directory_email)
        layout.addWidget(self.send_email_button)

        self.create_db_button = QPushButton("Creare baza de date")
        self.create_db_button.clicked.connect(self.create_database)
        layout.addWidget(self.create_db_button)

        self.load_db_button = QPushButton("Monitorizare + stocare in baza de date")
        self.load_db_button.clicked.connect(self.load_in_database)
        layout.addWidget(self.load_db_button)

        self.generate_report_button = QPushButton("Generare raport")
        self.generate_report_button.clicked.connect(self.generate_report)
        layout.addWidget(self.generate_report_button)

        self.database_tools_button = QPushButton("Database Tools")
        self.database_tools_button.clicked.connect(self.open_database_menu)
        layout.addWidget(self.database_tools_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecteaza un director")
        if directory:
            self.monitor_directory(directory, recursive=False)

    def select_directory_recursive(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecteaza un director")
        if directory:
            self.monitor_directory(directory, recursive=True)

    def select_directory_email(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecteaza un director")
        if directory:
            self.monitor_directory(directory, send_email=True)

    def create_database(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecteaza un director pentru monitorizare")
        if directory:
            db_file, _ = QFileDialog.getSaveFileName(self, "Selecteaza un fisier pentru baza de date", "", "Database Files (*.db)")
            if db_file:
                self.run_script('create_database.sh', directory, db_file)

    def load_in_database(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecteaza un director")
        db_file, _ = QFileDialog.getOpenFileName(self, "Selecteaza un fisier pentru baza de date", "", "Database Files (*.db)")
        if directory and db_file:
            self.run_script('load_in_database.sh', directory, db_file)

    def generate_report(self):
        specific_directory = QFileDialog.getExistingDirectory(self, "Selecteaza directorul pentru generarea raportului")
        if specific_directory:
            self.run_script('generate_raport.sh', specific_directory)

    def monitor_directory(self, directory, recursive=False, send_email=False):
        self.monitor_window = MonitorWindow()
        self.monitor_window.show()
        script_dir = os.path.dirname(os.path.realpath(__file__))
        if send_email:
            self.monitor_window.start_monitoring(os.path.join(script_dir, 'send_mail.sh'), directory)
        elif recursive:
            self.monitor_window.start_monitoring(os.path.join(script_dir, 'monitor_recursive.sh'), directory)
        else:
            self.monitor_window.start_monitoring(os.path.join(script_dir, 'monitor.sh'), directory)

    def run_script(self, script_name, *args):
        self.monitor_window = MonitorWindow()
        self.monitor_window.show()
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.monitor_window.start_monitoring(os.path.join(script_dir, script_name), *args)

    def open_database_menu(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecteaza un director")
        db_file, _ = QFileDialog.getOpenFileName(self, "Selecteaza un fisier pentru baza de date", "", "Database Files (*.db)")
        if directory and db_file:
            self.database_menu_window = DatabaseToolsWindow(directory, db_file, self)
            self.database_menu_window.show()
            self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
