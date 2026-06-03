#!/usr/bin/env python3
"""
Video Generator App - Main Entry Point
Aplicación de escritorio para generar videos realistas con NimVideo
"""

import sys
import os
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from ui.main_window import MainWindow
from utils.logger import setup_logger
from config.config_manager import ConfigManager


def setup_application():
    """
    Configura la aplicación principal
    """
    app = QApplication(sys.argv)
    
    # Setup logger
    logger = setup_logger()
    logger.info("Iniciando Video Generator App...")
    
    # Load config
    config = ConfigManager()
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create main window
    window = MainWindow(config, logger)
    window.show()
    
    logger.info("Aplicación cargada correctamente")
    
    return app, window


if __name__ == '__main__':
    try:
        app, window = setup_application()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error crítico: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
