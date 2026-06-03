#!/usr/bin/env python3
"""
Ventana principal de la aplicación
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QMenuBar, QMenu, QStatusBar, QSplitter, QPushButton,
    QLabel, QMessageBox
)
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QIcon, QFont, QColor

from ui.editor_panel import EditorPanel
from ui.preview_panel import PreviewPanel
from ui.styles import load_stylesheet
from utils.constants import APP_NAME, APP_VERSION, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT


class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación
    """
    
    def __init__(self, config, logger):
        super().__init__()
        self.config = config
        self.logger = logger
        
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.resize(1400, 900)
        
        # Aplicar estilos
        self.setStyleSheet(load_stylesheet(self.config.get('theme', 'dark')))
        
        # Crear UI
        self._create_menu_bar()
        self._create_central_widget()
        self._create_status_bar()
        
        self.logger.info(f"Ventana principal creada: {self.size()}")
    
    def _create_menu_bar(self):
        """
        Crea la barra de menú
        """
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu('&Archivo')
        
        new_action = file_menu.addAction('&Nuevo Proyecto')
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_project)
        
        open_action = file_menu.addAction('&Abrir Proyecto')
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_project)
        
        save_action = file_menu.addAction('&Guardar')
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_project)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction('&Salir')
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        
        # Menú Editar
        edit_menu = menubar.addMenu('&Editar')
        
        undo_action = edit_menu.addAction('&Deshacer')
        undo_action.setShortcut('Ctrl+Z')
        
        redo_action = edit_menu.addAction('&Rehacer')
        redo_action.setShortcut('Ctrl+Y')
        
        # Menú Ver
        view_menu = menubar.addMenu('&Ver')
        
        theme_action = view_menu.addAction('&Cambiar Tema')
        theme_action.triggered.connect(self.toggle_theme)
        
        # Menú Ayuda
        help_menu = menubar.addMenu('A&yuda')
        
        about_action = help_menu.addAction('&Acerca de')
        about_action.triggered.connect(self.show_about)
    
    def _create_central_widget(self):
        """
        Crea el widget central con paneles
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Panel de edición
        self.editor_panel = EditorPanel(self.config, self.logger)
        
        # Panel de previsualización
        self.preview_panel = PreviewPanel(self.config, self.logger)
        
        # Splitter para redimensionar
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.editor_panel)
        splitter.addWidget(self.preview_panel)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([700, 700])
        
        layout.addWidget(splitter)
    
    def _create_status_bar(self):
        """
        Crea la barra de estado
        """
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        status_label = QLabel('Listo')
        self.status_bar.addWidget(status_label)
        self.status_label = status_label
    
    def new_project(self):
        """Crea un nuevo proyecto"""
        self.logger.info("Nuevo proyecto")
        self.status_label.setText('Nuevo proyecto creado')
    
    def open_project(self):
        """Abre un proyecto existente"""
        self.logger.info("Abrir proyecto")
        self.status_label.setText('Abriendo proyecto...')
    
    def save_project(self):
        """Guarda el proyecto actual"""
        self.logger.info("Guardar proyecto")
        self.status_label.setText('Proyecto guardado')
    
    def toggle_theme(self):
        """Cambia el tema de la aplicación"""
        current_theme = self.config.get('theme', 'dark')
        new_theme = 'light' if current_theme == 'dark' else 'dark'
        self.config.set('theme', new_theme)
        self.setStyleSheet(load_stylesheet(new_theme))
        self.logger.info(f"Tema cambiado a: {new_theme}")
    
    def show_about(self):
        """Muestra el diálogo Acerca de"""
        QMessageBox.about(
            self,
            f'Acerca de {APP_NAME}',
            f'{APP_NAME} v{APP_VERSION}\n\n'
            'Aplicación de escritorio para generar videos realistas\n'
            'con avatares usando tecnología NimVideo.\n\n'
            '© 2024. Todos los derechos reservados.'
        )
