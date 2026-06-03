#!/usr/bin/env python3
"""
Estilos CSS para la aplicación
"""

DARK_THEME = """
QMainWindow {
    background-color: #1e1e1e;
    color: #ffffff;
}

QMenuBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border-bottom: 1px solid #3d3d3d;
}

QMenuBar::item:selected {
    background-color: #3d3d3d;
}

QMenu {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #3d3d3d;
}

QMenu::item:selected {
    background-color: #4d4d4d;
}

QStatusBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border-top: 1px solid #3d3d3d;
}

QGroupBox {
    color: #ffffff;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    margin-top: 8px;
    padding-top: 8px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

QLineEdit, QTextEdit {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    padding: 5px;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #0078d4;
}

QComboBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    padding: 5px;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #2d2d2d;
    color: #ffffff;
    selection-background-color: #0078d4;
}

QSpinBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    padding: 5px;
}

QCheckBox {
    color: #ffffff;
}

QCheckBox::indicator {
    border: 1px solid #3d3d3d;
    border-radius: 3px;
    width: 18px;
    height: 18px;
}

QCheckBox::indicator:checked {
    background-color: #0078d4;
    border: 1px solid #0078d4;
}

QPushButton {
    background-color: #0078d4;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1084d7;
}

QPushButton:pressed {
    background-color: #006cc1;
}

QSlider::groove:horizontal {
    background-color: #3d3d3d;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #0078d4;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QProgressBar {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #0078d4;
}

QLabel {
    color: #ffffff;
}

QSplitter::handle {
    background-color: #2d2d2d;
}
"""

LIGHT_THEME = """
QMainWindow {
    background-color: #ffffff;
    color: #000000;
}

QMenuBar {
    background-color: #f5f5f5;
    color: #000000;
    border-bottom: 1px solid #e0e0e0;
}

QMenuBar::item:selected {
    background-color: #e0e0e0;
}

QMenu {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #e0e0e0;
}

QMenu::item:selected {
    background-color: #f0f0f0;
}

QStatusBar {
    background-color: #f5f5f5;
    color: #000000;
    border-top: 1px solid #e0e0e0;
}

QGroupBox {
    color: #000000;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    margin-top: 8px;
    padding-top: 8px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

QLineEdit, QTextEdit {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    padding: 5px;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #0078d4;
}

QComboBox {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    padding: 5px;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #000000;
    selection-background-color: #0078d4;
}

QSpinBox {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    padding: 5px;
}

QCheckBox {
    color: #000000;
}

QCheckBox::indicator {
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    width: 18px;
    height: 18px;
}

QCheckBox::indicator:checked {
    background-color: #0078d4;
    border: 1px solid #0078d4;
}

QPushButton {
    background-color: #0078d4;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1084d7;
}

QPushButton:pressed {
    background-color: #006cc1;
}

QSlider::groove:horizontal {
    background-color: #e0e0e0;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #0078d4;
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QProgressBar {
    background-color: #f5f5f5;
    color: #000000;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #0078d4;
}

QLabel {
    color: #000000;
}

QSplitter::handle {
    background-color: #f5f5f5;
}
"""


def load_stylesheet(theme: str = 'dark') -> str:
    """
    Carga el stylesheet según el tema especificado
    """
    if theme.lower() == 'light':
        return LIGHT_THEME
    return DARK_THEME
