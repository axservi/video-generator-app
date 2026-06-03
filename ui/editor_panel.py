#!/usr/bin/env python3
"""
Panel de edición de la aplicación
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QTextEdit, QPushButton, QComboBox, QSpinBox, QGroupBox,
    QFormLayout, QSlider, QCheckBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class EditorPanel(QWidget):
    """
    Panel izquierdo para edición de video
    """
    
    video_updated = pyqtSignal()
    
    def __init__(self, config, logger):
        super().__init__()
        self.config = config
        self.logger = logger
        
        self._create_ui()
    
    def _create_ui(self):
        """
        Crea la interfaz del panel de edición
        """
        layout = QVBoxLayout(self)
        
        # Título
        title = QLabel('EDITOR DE VIDEO')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        layout.addSpacing(10)
        
        # Sección: Configuración de Texto
        text_group = QGroupBox('Configuración de Texto')
        text_layout = QFormLayout()
        
        self.text_input = QTextEdit()
        self.text_input.setMaximumHeight(100)
        self.text_input.setPlaceholderText('Ingresa el texto para el video...')
        self.text_input.textChanged.connect(self.on_text_changed)
        text_layout.addRow('Contenido:', self.text_input)
        
        self.language_combo = QComboBox()
        self.language_combo.addItems(['Español', 'English', 'Français', 'Deutsch'])
        text_layout.addRow('Idioma:', self.language_combo)
        
        self.voice_combo = QComboBox()
        self.voice_combo.addItems(['Voz 1', 'Voz 2', 'Voz 3', 'Voz 4'])
        text_layout.addRow('Voz:', self.voice_combo)
        
        text_group.setLayout(text_layout)
        layout.addWidget(text_group)
        
        # Sección: Avatar
        avatar_group = QGroupBox('Configuración de Avatar')
        avatar_layout = QFormLayout()
        
        self.avatar_combo = QComboBox()
        self.avatar_combo.addItems(['Avatar 1', 'Avatar 2', 'Avatar 3', 'Avatar 4'])
        self.avatar_combo.currentTextChanged.connect(self.on_avatar_changed)
        avatar_layout.addRow('Avatar:', self.avatar_combo)
        
        self.background_combo = QComboBox()
        self.background_combo.addItems(['Fondo 1', 'Fondo 2', 'Fondo 3', 'Personalizado'])
        avatar_layout.addRow('Fondo:', self.background_combo)
        
        avatar_group.setLayout(avatar_layout)
        layout.addWidget(avatar_group)
        
        # Sección: Configuración de Video
        video_group = QGroupBox('Configuración de Video')
        video_layout = QFormLayout()
        
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(['720p', '1080p', '4K'])
        self.quality_combo.setCurrentText('1080p')
        video_layout.addRow('Calidad:', self.quality_combo)
        
        self.fps_spin = QSpinBox()
        self.fps_spin.setValue(30)
        self.fps_spin.setMinimum(24)
        self.fps_spin.setMaximum(60)
        video_layout.addRow('FPS:', self.fps_spin)
        
        self.duration_spin = QSpinBox()
        self.duration_spin.setValue(60)
        self.duration_spin.setMinimum(5)
        self.duration_spin.setMaximum(300)
        self.duration_spin.setSuffix(' seg')
        video_layout.addRow('Duración:', self.duration_spin)
        
        video_group.setLayout(video_layout)
        layout.addWidget(video_group)
        
        # Sección: Efectos
        effects_group = QGroupBox('Efectos')
        effects_layout = QFormLayout()
        
        self.lip_sync_check = QCheckBox('Sincronización de Labios')
        self.lip_sync_check.setChecked(True)
        effects_layout.addRow(self.lip_sync_check)
        
        self.music_check = QCheckBox('Agregar Música')
        effects_layout.addRow(self.music_check)
        
        effects_group.setLayout(effects_layout)
        layout.addWidget(effects_group)
        
        # Botones de acción
        layout.addSpacing(20)
        
        button_layout = QHBoxLayout()
        
        generate_btn = QPushButton('▶️ Generar Video')
        generate_btn.setMinimumHeight(40)
        generate_btn.clicked.connect(self.generate_video)
        button_layout.addWidget(generate_btn)
        
        export_btn = QPushButton('💾 Exportar')
        export_btn.setMinimumHeight(40)
        export_btn.clicked.connect(self.export_video)
        button_layout.addWidget(export_btn)
        
        layout.addLayout(button_layout)
        
        # Expandir al final
        layout.addStretch()
    
    def on_text_changed(self):
        """Se ejecuta cuando cambia el texto"""
        self.logger.debug(f"Texto cambiado")
        self.video_updated.emit()
    
    def on_avatar_changed(self, avatar):
        """Se ejecuta cuando cambia el avatar"""
        self.logger.debug(f"Avatar cambiado: {avatar}")
        self.video_updated.emit()
    
    def generate_video(self):
        """Genera el video"""
        self.logger.info("Generando video...")
        print("Generando video con los parámetros actuales...")
    
    def export_video(self):
        """Exporta el video"""
        self.logger.info("Exportando video...")
        print("Exportando video...")
