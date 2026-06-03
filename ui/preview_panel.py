#!/usr/bin/env python3
"""
Panel de previsualización de la aplicación
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QSlider, QProgressBar, QTabWidget
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtWidgets import QFrame


class PreviewPanel(QWidget):
    """
    Panel derecho para previsualización de video
    """
    
    def __init__(self, config, logger):
        super().__init__()
        self.config = config
        self.logger = logger
        self.is_playing = False
        
        self._create_ui()
    
    def _create_ui(self):
        """
        Crea la interfaz del panel de previsualización
        """
        layout = QVBoxLayout(self)
        
        # Título
        title = QLabel('PREVISUALIZACIÓN')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        layout.addSpacing(10)
        
        # Área de video
        video_frame = QFrame()
        video_frame.setStyleSheet(
            'QFrame { '
            'background-color: #000000; '
            'border: 2px solid #333333; '
            'border-radius: 8px; '
            '}'
        )
        video_layout = QVBoxLayout(video_frame)
        
        self.video_label = QLabel('Sin previsualización')
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setMinimumHeight(300)
        self.video_label.setStyleSheet('color: #888888;')
        video_layout.addWidget(self.video_label)
        
        layout.addWidget(video_frame, 1)
        
        # Controles de reproducción
        controls_layout = QHBoxLayout()
        
        self.play_btn = QPushButton('▶')
        self.play_btn.setMaximumWidth(50)
        self.play_btn.clicked.connect(self.toggle_playback)
        controls_layout.addWidget(self.play_btn)
        
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setRange(0, 100)
        self.progress_slider.setValue(0)
        controls_layout.addWidget(self.progress_slider)
        
        self.time_label = QLabel('0:00 / 1:00')
        self.time_label.setMaximumWidth(80)
        controls_layout.addWidget(self.time_label)
        
        layout.addLayout(controls_layout)
        
        # Progress bar para generación
        self.generation_progress = QProgressBar()
        self.generation_progress.setValue(0)
        self.generation_progress.setVisible(False)
        layout.addWidget(self.generation_progress)
        
        # Información del video
        info_layout = QHBoxLayout()
        
        self.info_label = QLabel('Estado: Listo')
        self.info_label.setStyleSheet('color: #888888; font-size: 11px;')
        info_layout.addWidget(self.info_label)
        
        info_layout.addStretch()
        
        self.size_label = QLabel('Tamaño: --')
        self.size_label.setStyleSheet('color: #888888; font-size: 11px;')
        info_layout.addWidget(self.size_label)
        
        layout.addLayout(info_layout)
    
    def toggle_playback(self):
        """Alterna reproducción/pausa"""
        self.is_playing = not self.is_playing
        self.play_btn.setText('⏸' if self.is_playing else '▶')
        self.logger.info(f"Reproducción: {'pausada' if not self.is_playing else 'iniciada'}")
    
    def show_generating(self):
        """Muestra que se está generando"""
        self.generation_progress.setVisible(True)
        self.info_label.setText('Estado: Generando...')
    
    def show_preview(self, pixmap):
        """Muestra una previsualización"""
        if isinstance(pixmap, QPixmap):
            scaled = pixmap.scaledToWidth(self.video_label.width())
            self.video_label.setPixmap(scaled)
        else:
            self.video_label.setText('Previsualización')
