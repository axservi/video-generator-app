#!/usr/bin/env python3
"""
Panel de edición mejorado con más opciones
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QTextEdit, QPushButton, QComboBox, QSpinBox, QGroupBox,
    QFormLayout, QSlider, QCheckBox, QTabWidget, QListWidget,
    QListWidgetItem, QDoubleSpinBox, QColorDialog, QFileDialog
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QColor


class EditorPanel(QWidget):
    """
    Panel izquierdo para edición de video con múltiples opciones
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
        main_layout = QVBoxLayout(self)
        
        # Título
        title = QLabel('🎬 EDITOR DE VIDEO')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        main_layout.addSpacing(5)
        
        # Crear tabs para diferentes secciones
        tabs = QTabWidget()
        
        # TAB 1: Contenido de Texto
        tab1 = self._create_text_tab()
        tabs.addTab(tab1, "📝 Texto")
        
        # TAB 2: Avatar y Fondo
        tab2 = self._create_avatar_tab()
        tabs.addTab(tab2, "👤 Avatar")
        
        # TAB 3: Configuración de Video
        tab3 = self._create_video_config_tab()
        tabs.addTab(tab3, "🎥 Video")
        
        # TAB 4: Efectos y Transiciones
        tab4 = self._create_effects_tab()
        tabs.addTab(tab4, "✨ Efectos")
        
        # TAB 5: Audio y Música
        tab5 = self._create_audio_tab()
        tabs.addTab(tab5, "🎵 Audio")
        
        # TAB 6: Filtros y Color
        tab6 = self._create_filters_tab()
        tabs.addTab(tab6, "🎨 Filtros")
        
        main_layout.addWidget(tabs)
        
        # Botones de acción
        main_layout.addSpacing(10)
        button_layout = QHBoxLayout()
        
        generate_btn = QPushButton('▶️ Generar Video')
        generate_btn.setMinimumHeight(45)
        generate_btn.setStyleSheet("font-weight: bold; font-size: 11px;")
        generate_btn.clicked.connect(self.generate_video)
        button_layout.addWidget(generate_btn)
        
        export_btn = QPushButton('💾 Exportar')
        export_btn.setMinimumHeight(45)
        export_btn.setStyleSheet("font-weight: bold; font-size: 11px;")
        export_btn.clicked.connect(self.export_video)
        button_layout.addWidget(export_btn)
        
        main_layout.addLayout(button_layout)
    
    def _create_text_tab(self):
        """TAB 1: Contenido de texto"""
        widget = QWidget()
        layout = QFormLayout(widget)
        
        # Texto principal
        self.text_input = QTextEdit()
        self.text_input.setMaximumHeight(120)
        self.text_input.setPlaceholderText('Ingresa el texto para tu video...')
        self.text_input.textChanged.connect(self.on_text_changed)
        layout.addRow('Contenido:', self.text_input)
        
        # Idioma
        self.language_combo = QComboBox()
        self.language_combo.addItems(['Español', 'English', 'Français', 'Deutsch', 'Português', 'Italiano'])
        layout.addRow('Idioma:', self.language_combo)
        
        # Voz
        self.voice_combo = QComboBox()
        self.voice_combo.addItems(['Voz 1 (Clara)', 'Voz 2 (Profunda)', 'Voz 3 (Juvenil)', 'Voz 4 (Grave)'])
        layout.addRow('Voz:', self.voice_combo)
        
        # Velocidad de lectura
        self.speed_spin = QDoubleSpinBox()
        self.speed_spin.setValue(1.0)
        self.speed_spin.setMinimum(0.5)
        self.speed_spin.setMaximum(2.0)
        self.speed_spin.setSingleStep(0.1)
        layout.addRow('Velocidad:', self.speed_spin)
        
        # Pausas entre oraciones
        self.pause_spin = QSpinBox()
        self.pause_spin.setValue(500)
        self.pause_spin.setMinimum(100)
        self.pause_spin.setMaximum(5000)
        self.pause_spin.setSuffix(' ms')
        layout.addRow('Pausa entre frases:', self.pause_spin)
        
        return widget
    
    def _create_avatar_tab(self):
        """TAB 2: Avatar y Fondo"""
        widget = QWidget()
        layout = QFormLayout(widget)
        
        # Avatar
        self.avatar_combo = QComboBox()
        self.avatar_combo.addItems([
            'Avatar 1 - Mujer Profesional',
            'Avatar 2 - Hombre Ejecutivo',
            'Avatar 3 - Mujer Casual',
            'Avatar 4 - Hombre Casual',
            'Avatar 5 - Mujer Animada',
            'Avatar 6 - Hombre Deportista'
        ])
        self.avatar_combo.currentTextChanged.connect(self.on_avatar_changed)
        layout.addRow('Avatar:', self.avatar_combo)
        
        # Tamaño del avatar
        self.avatar_size = QSpinBox()
        self.avatar_size.setValue(100)
        self.avatar_size.setMinimum(50)
        self.avatar_size.setMaximum(150)
        self.avatar_size.setSuffix('%')
        layout.addRow('Tamaño Avatar:', self.avatar_size)
        
        # Posición del avatar
        self.avatar_position = QComboBox()
        self.avatar_position.addItems(['Centro', 'Izquierda', 'Derecha', 'Arriba', 'Abajo'])
        layout.addRow('Posición:', self.avatar_position)
        
        # Fondo
        self.background_combo = QComboBox()
        self.background_combo.addItems([
            'Fondo 1 - Blanco',
            'Fondo 2 - Gris',
            'Fondo 3 - Azul Gradiente',
            'Fondo 4 - Verde Oficina',
            'Fondo 5 - Morado Moderno',
            'Fondo 6 - Rojo Vibrante',
            'Personalizado'
        ])
        layout.addRow('Fondo:', self.background_combo)
        
        # Color personalizado
        self.color_btn = QPushButton('Elegir Color')
        self.color_btn.clicked.connect(self.choose_color)
        layout.addRow('Color Personalizado:', self.color_btn)
        
        # Blur de fondo
        self.blur_check = QCheckBox('Efecto Blur en Fondo')
        layout.addRow(self.blur_check)
        
        return widget
    
    def _create_video_config_tab(self):
        """TAB 3: Configuración de Video"""
        widget = QWidget()
        layout = QFormLayout(widget)
        
        # Presets sociales
        self.preset_combo = QComboBox()
        self.preset_combo.addItems([
            'YouTube (1920x1080)',
            'TikTok (1080x1920)',
            'Instagram (1080x1080)',
            'Twitter (1200x675)',
            'LinkedIn (1080x1080)',
            'Facebook (1200x630)',
            'Personalizado'
        ])
        self.preset_combo.currentTextChanged.connect(self.on_preset_changed)
        layout.addRow('Preset:', self.preset_combo)
        
        # Calidad
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(['480p (Bajo)', '720p (Estándar)', '1080p (HD)', '1440p (4K)', '2160p (8K)'])
        self.quality_combo.setCurrentText('1080p (HD)')
        layout.addRow('Calidad:', self.quality_combo)
        
        # FPS
        self.fps_spin = QSpinBox()
        self.fps_spin.setValue(30)
        self.fps_spin.setMinimum(24)
        self.fps_spin.setMaximum(60)
        self.fps_spin.setSuffix(' fps')
        layout.addRow('FPS:', self.fps_spin)
        
        # Duración
        self.duration_spin = QSpinBox()
        self.duration_spin.setValue(60)
        self.duration_spin.setMinimum(5)
        self.duration_spin.setMaximum(600)
        self.duration_spin.setSuffix(' seg')
        layout.addRow('Duración:', self.duration_spin)
        
        # Bitrate
        self.bitrate_spin = QSpinBox()
        self.bitrate_spin.setValue(5000)
        self.bitrate_spin.setMinimum(1000)
        self.bitrate_spin.setMaximum(50000)
        self.bitrate_spin.setSuffix(' kbps')
        layout.addRow('Bitrate:', self.bitrate_spin)
        
        return widget
    
    def _create_effects_tab(self):
        """TAB 4: Efectos y Transiciones"""
        widget = QWidget()
        layout = QFormLayout(widget)
        
        # Lip Sync
        self.lip_sync_check = QCheckBox('Sincronización de Labios')
        self.lip_sync_check.setChecked(True)
        layout.addRow(self.lip_sync_check)
        
        # Expresiones faciales
        self.expressions_check = QCheckBox('Expresiones Faciales Dinámicas')
        self.expressions_check.setChecked(True)
        layout.addRow(self.expressions_check)
        
        # Transición de entrada
        self.transition_in = QComboBox()
        self.transition_in.addItems(['Ninguna', 'Fade In', 'Slide In', 'Zoom In', 'Flip In'])
        layout.addRow('Transición Entrada:', self.transition_in)
        
        # Transición de salida
        self.transition_out = QComboBox()
        self.transition_out.addItems(['Ninguna', 'Fade Out', 'Slide Out', 'Zoom Out', 'Flip Out'])
        layout.addRow('Transición Salida:', self.transition_out)
        
        # Duración de transición
        self.transition_duration = QSpinBox()
        self.transition_duration.setValue(500)
        self.transition_duration.setMinimum(100)
        self.transition_duration.setMaximum(2000)
        self.transition_duration.setSuffix(' ms')
        layout.addRow('Duración Transición:', self.transition_duration)
        
        # Efecto de entrada de texto
        self.text_effect = QComboBox()
        self.text_effect.addItems(['Ninguno', 'Typewriter', 'Fade', 'Pop', 'Slide'])
        layout.addRow('Efecto Texto:', self.text_effect)
        
        return widget
    
    def _create_audio_tab(self):
        """TAB 5: Audio y Música"""
        widget = QWidget()
        layout = QFormLayout(widget)
        
        # Agregar música de fondo
        self.music_check = QCheckBox('Agregar Música de Fondo')
        layout.addRow(self.music_check)
        
        # Seleccionar música
        self.music_combo = QComboBox()
        self.music_combo.addItems([
            'Música 1 - Corporativa',
            'Música 2 - Energética',
            'Música 3 - Relajante',
            'Música 4 - Épica',
            'Música 5 - Uptempo',
            'Archivo Custom...'
        ])
        layout.addRow('Música:', self.music_combo)
        
        # Volumen de música
        self.music_volume = QSpinBox()
        self.music_volume.setValue(50)
        self.music_volume.setMinimum(0)
        self.music_volume.setMaximum(100)
        self.music_volume.setSuffix('%')
        layout.addRow('Volumen Música:', self.music_volume)
        
        # Volumen de voz
        self.voice_volume = QSpinBox()
        self.voice_volume.setValue(100)
        self.voice_volume.setMinimum(0)
        self.voice_volume.setMaximum(100)
        self.voice_volume.setSuffix('%')
        layout.addRow('Volumen Voz:', self.voice_volume)
        
        # Sonidos de efecto
        self.sfx_check = QCheckBox('Incluir Efectos de Sonido')
        layout.addRow(self.sfx_check)
        
        # Normalización de audio
        self.audio_normalize = QCheckBox('Normalizar Audio')
        self.audio_normalize.setChecked(True)
        layout.addRow(self.audio_normalize)
        
        return widget
    
    def _create_filters_tab(self):
        """TAB 6: Filtros y Color"""
        widget = QWidget()
        layout = QFormLayout(widget)
        
        # Filtro de color
        self.filter_combo = QComboBox()
        self.filter_combo.addItems([
            'Ninguno',
            'Blanco y Negro',
            'Sepia',
            'Cool',
            'Warm',
            'Vintage',
            'Neon',
            'Cinematic'
        ])
        layout.addRow('Filtro:', self.filter_combo)
        
        # Brillo
        self.brightness_slider = QSpinBox()
        self.brightness_slider.setValue(100)
        self.brightness_slider.setMinimum(50)
        self.brightness_slider.setMaximum(150)
        self.brightness_slider.setSuffix('%')
        layout.addRow('Brillo:', self.brightness_slider)
        
        # Contraste
        self.contrast_slider = QSpinBox()
        self.contrast_slider.setValue(100)
        self.contrast_slider.setMinimum(50)
        self.contrast_slider.setMaximum(150)
        self.contrast_slider.setSuffix('%')
        layout.addRow('Contraste:', self.contrast_slider)
        
        # Saturación
        self.saturation_slider = QSpinBox()
        self.saturation_slider.setValue(100)
        self.saturation_slider.setMinimum(0)
        self.saturation_slider.setMaximum(200)
        self.saturation_slider.setSuffix('%')
        layout.addRow('Saturación:', self.saturation_slider)
        
        # Nitidez
        self.sharpness_slider = QSpinBox()
        self.sharpness_slider.setValue(100)
        self.sharpness_slider.setMinimum(50)
        self.sharpness_slider.setMaximum(200)
        self.sharpness_slider.setSuffix('%')
        layout.addRow('Nitidez:', self.sharpness_slider)
        
        # Watermark
        self.watermark_check = QCheckBox('Agregar Marca de Agua')
        layout.addRow(self.watermark_check)
        
        return widget
    
    def on_text_changed(self):
        """Se ejecuta cuando cambia el texto"""
        self.logger.debug("Texto cambiado")
        self.video_updated.emit()
    
    def on_avatar_changed(self, avatar):
        """Se ejecuta cuando cambia el avatar"""
        self.logger.debug(f"Avatar cambiado: {avatar}")
        self.video_updated.emit()
    
    def on_preset_changed(self, preset):
        """Se ejecuta cuando cambia el preset"""
        self.logger.debug(f"Preset cambiado: {preset}")
    
    def choose_color(self):
        """Abre selector de color"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.logger.info(f"Color seleccionado: {color.name()}")
    
    def generate_video(self):
        """Genera el video"""
        self.logger.info("Generando video con configuración actual...")
        print("🎬 Generando video...")
    
    def export_video(self):
        """Exporta el video"""
        self.logger.info("Exportando video...")
        print("💾 Exportando video...")
