#!/usr/bin/env python3
"""
Panel de previsualizacion mejorado con controles avanzados
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QSlider, QProgressBar, QTabWidget, QFrame, QSpinBox,
    QComboBox, QCheckBox, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap


class PreviewPanel(QWidget):
    """
    Panel derecho para previsualizacion de video con controles avanzados
    """
    
    def __init__(self, config, logger):
        super().__init__()
        self.config = config
        self.logger = logger
        self.is_playing = False
        
        self._create_ui()
    
    def _create_ui(self):
        """
        Crea la interfaz del panel de previsualizacion
        """
        layout = QVBoxLayout(self)
        
        # Título
        title = QLabel('📺 PREVISUALIZACION')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        layout.addSpacing(5)
        
        # Tabs para diferentes vistas
        tabs = QTabWidget()
        
        # TAB 1: Previsualizacion del video
        tab1 = self._create_video_preview_tab()
        tabs.addTab(tab1, "🎬 Video")
        
        # TAB 2: Línea de tiempo
        tab2 = self._create_timeline_tab()
        tabs.addTab(tab2, "📊 Línea de Tiempo")
        
        # TAB 3: Información del proyecto
        tab3 = self._create_info_tab()
        tabs.addTab(tab3, "ℹ️ Info")
        
        # TAB 4: Historial de renderizado
        tab4 = self._create_render_history_tab()
        tabs.addTab(tab4, "📜 Historial")
        
        layout.addWidget(tabs)
    
    def _create_video_preview_tab(self):
        """TAB 1: Previsualizacion del video"""
        widget = QWidget()
        main_layout = QVBoxLayout(widget)
        
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
        
        self.video_label = QLabel('Sin previsualizacion')
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setMinimumHeight(300)
        self.video_label.setStyleSheet('color: #888888; font-size: 16px;')
        video_layout.addWidget(self.video_label)
        
        main_layout.addWidget(video_frame, 1)
        
        # Controles de reproducción
        controls_layout = QHBoxLayout()
        
        self.play_btn = QPushButton('▶')
        self.play_btn.setMaximumWidth(50)
        self.play_btn.setMinimumHeight(40)
        self.play_btn.clicked.connect(self.toggle_playback)
        controls_layout.addWidget(self.play_btn)
        
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setRange(0, 100)
        self.progress_slider.setValue(0)
        controls_layout.addWidget(self.progress_slider)
        
        self.time_label = QLabel('0:00 / 1:00')
        self.time_label.setMaximumWidth(80)
        self.time_label.setStyleSheet('font-family: monospace;')
        controls_layout.addWidget(self.time_label)
        
        main_layout.addLayout(controls_layout)
        
        # Volumen y velocidad
        secondary_controls = QHBoxLayout()
        
        volume_label = QLabel('Volumen:')
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(100)
        self.volume_slider.setMaximumWidth(100)
        secondary_controls.addWidget(volume_label)
        secondary_controls.addWidget(self.volume_slider)
        
        speed_label = QLabel('Velocidad:')
        self.speed_combo = QComboBox()
        self.speed_combo.addItems(['0.5x', '0.75x', '1.0x', '1.25x', '1.5x', '2.0x'])
        self.speed_combo.setCurrentText('1.0x')
        self.speed_combo.setMaximumWidth(80)
        secondary_controls.addWidget(speed_label)
        secondary_controls.addWidget(self.speed_combo)
        
        secondary_controls.addStretch()
        
        main_layout.addLayout(secondary_controls)
        
        # Progress bar para generación
        self.generation_progress = QProgressBar()
        self.generation_progress.setValue(0)
        self.generation_progress.setVisible(False)
        main_layout.addWidget(self.generation_progress)
        
        # Información del video
        info_layout = QHBoxLayout()
        
        self.info_label = QLabel('Estado: Listo')
        self.info_label.setStyleSheet('color: #888888; font-size: 11px;')
        info_layout.addWidget(self.info_label)
        
        info_layout.addStretch()
        
        self.size_label = QLabel('Tamaño: --')
        self.size_label.setStyleSheet('color: #888888; font-size: 11px;')
        info_layout.addWidget(self.size_label)
        
        main_layout.addLayout(info_layout)
        
        return widget
    
    def _create_timeline_tab(self):
        """TAB 2: Línea de tiempo"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        title = QLabel('Línea de Tiempo del Proyecto')
        title_font = QFont()
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Simulación de línea de tiempo
        timeline_frame = QFrame()
        timeline_frame.setStyleSheet(
            'QFrame { '
            'background-color: #2d2d2d; '
            'border: 1px solid #3d3d3d; '
            'border-radius: 4px; '
            'padding: 10px; '
            '}'
        )
        timeline_layout = QVBoxLayout(timeline_frame)
        
        markers = [
            '00:00 - Intro (Fade In)',
            '00:05 - Avatar Aparece',
            '00:10 - Voz Comienza',
            '00:15 - Expresiones Dinámicas',
            '00:30 - Música de Fondo',
            '00:45 - Transición de Salida',
        ]
        
        for marker in markers:
            marker_label = QLabel(marker)
            marker_label.setStyleSheet('color: #00aaff; font-size: 10px;')
            timeline_layout.addWidget(marker_label)
        
        layout.addWidget(timeline_frame)
        layout.addStretch()
        
        return widget
    
    def _create_info_tab(self):
        """TAB 3: Información del proyecto"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        title = QLabel('Información del Proyecto')
        title_font = QFont()
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        info_frame = QFrame()
        info_frame.setStyleSheet(
            'QFrame { '
            'background-color: #2d2d2d; '
            'border: 1px solid #3d3d3d; '
            'border-radius: 4px; '
            'padding: 10px; '
            '}'
        )
        info_layout = QVBoxLayout(info_frame)
        
        info_items = [
            ('Resolución:', '1920 x 1080'),
            ('FPS:', '30'),
            ('Duración:', '60 segundos'),
            ('Bitrate:', '5000 kbps'),
            ('Tamaño Estimado:', '37.5 MB'),
            ('Formato:', 'MP4 (H.264)'),
            ('Codec de Voz:', 'Neuronal'),
            ('Filtro Aplicado:', 'Cinematic'),
        ]
        
        for label, value in info_items:
            item_layout = QHBoxLayout()
            label_widget = QLabel(label)
            label_widget.setStyleSheet('color: #cccccc; font-weight: bold;')
            label_widget.setMaximumWidth(150)
            
            value_widget = QLabel(value)
            value_widget.setStyleSheet('color: #00aaff;')
            
            item_layout.addWidget(label_widget)
            item_layout.addWidget(value_widget)
            item_layout.addStretch()
            
            info_layout.addLayout(item_layout)
        
        layout.addWidget(info_frame)
        layout.addStretch()
        
        return widget
    
    def _create_render_history_tab(self):
        """TAB 4: Historial de renderizado"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        title = QLabel('Historial de Renderizado')
        title_font = QFont()
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        self.history_list = QListWidget()
        self.history_list.setStyleSheet(
            'QListWidget { '
            'background-color: #2d2d2d; '
            'color: #cccccc; '
            'border: 1px solid #3d3d3d; '
            '}'
        )
        
        # Elementos simulados de historial
        history_items = [
            '✓ 2026-06-04 00:30 - Renderizado completado (45s)',
            '✓ 2026-06-04 00:15 - Renderizado completado (30s)',
            '⏳ 2026-06-04 00:05 - Renderizado en progreso...',
            '✗ 2026-06-03 23:45 - Error en renderizado',
            '✓ 2026-06-03 23:30 - Renderizado completado (60s)',
        ]
        
        for item_text in history_items:
            item = QListWidgetItem(item_text)
            self.history_list.addItem(item)
        
        layout.addWidget(self.history_list)
        
        # Botones de acción
        button_layout = QHBoxLayout()
        
        clear_btn = QPushButton('Limpiar Historial')
        clear_btn.clicked.connect(self.clear_history)
        button_layout.addWidget(clear_btn)
        
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        return widget
    
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
        """Muestra una previsualizacion"""
        if isinstance(pixmap, QPixmap):
            scaled = pixmap.scaledToWidth(self.video_label.width())
            self.video_label.setPixmap(scaled)
        else:
            self.video_label.setText('Previsualizacion')
    
    def clear_history(self):
        """Limpia el historial"""
        self.history_list.clear()
        self.logger.info("Historial de renderizado limpiado")
