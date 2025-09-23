# Import các lớp cần thiết từ thư viện PyQt6
import os
import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QScreen
from source import Window

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STYLESHEET_PATH = os.path.join(BASE_DIR, '..', 'assets', 'stylesheets', 'main.css')

# Khởi tạo ứng dụng và hiển thị cửa sổ
if __name__ == "__main__":
    # Tạo một instance của QApplication
    app = QApplication(sys.argv)
    
    # Return information about device's monitor
    main_screen: QScreen = app.primaryScreen()

    # Return size of monitor by attribute: 'geometry'.
    screen_geometry = main_screen.geometry()

    # Access width & height 
    monitor_width = screen_geometry.width()
    monitor_height = screen_geometry.height()
    
    # Tạo và hiển thị cửa sổ chính
    window = Window.Main(monitor_width= monitor_width, 
                         monitor_height= monitor_height)
    window.show()
    
    # Main event loop
    sys.exit(app.exec())
'''   
my-python-app/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   └── widgets/
│   │       ├── __init__.py
│   │       └── custom_button.py
│   ├── logic/
│   │   ├── __init__.py
│   │   └── data_manager.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── assets/
│   ├── images/
│   │   ├── icon.png
│   │   └── background.jpg
│   └── data/
│       └── config.json
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_logic.py
├── venv/
├── requirements.txt
├── README.md
└── setup.py
'''