import os
import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QScreen


from config.settings import SCREEN_RATIO
# from config.themes import  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(BASE_DIR))
STYLESHEET_DIR = os.path.join(ROOT, 'assets', 'stylesheets')



class Main(QMainWindow): 
    def __init__(self, monitor_width, monitor_height): 
        
        super().__init__() 
        
        self.monitor_width = monitor_width 
        self.monitor_height = monitor_height

        # Calculate ratio center
        self.center_x = monitor_width//2
        self.center_y = monitor_height//2
        
        # Size of mainwindow
        self.main_gui_width = int(self.monitor_width * SCREEN_RATIO['width'])
        self.main_gui_height = int(self.monitor_height * SCREEN_RATIO['height'])
        
        
        
        # Setting attributes of mainwindow
        self.setGeometry(self.center_x - self.main_gui_width // 2 , 
                         self.center_y - self.main_gui_height // 2, 
                         self.main_gui_width, 
                         self.main_gui_height)
        
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.current_theme = "light"
        self.theme_button = QPushButton("Chuyển sang Theme Tối")
        self.theme_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_button)
        
        # Áp dụng theme mặc định
        self.apply_theme("light")
        
    def apply_theme(self, theme_name):
        """Tải và áp dụng stylesheet từ file CSS tương ứng."""
        file_path = os.path.join(STYLESHEET_DIR, f"{theme_name}_theme.css")
        try:
            with open(file_path, "r") as f:
                self.setStyleSheet(f.read())
            print(f"Stylesheet '{theme_name}' đã được áp dụng thành công.")
        except FileNotFoundError:
            print(f"Lỗi: Không tìm thấy file stylesheet tại đường dẫn: {file_path}")

    def toggle_theme(self):
        """Chuyển đổi giữa theme sáng và tối."""
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.apply_theme("dark")
            self.theme_button.setText("Chuyển sang Theme Sáng")
        else:
            self.current_theme = "light"
            self.apply_theme("light")
            self.theme_button.setText("Chuyển sang Theme Tối")
