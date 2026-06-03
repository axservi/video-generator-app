#!/usr/bin/env python3
"""
Constantes globales de la aplicación
"""

from enum import Enum
from pathlib import Path

# Directorio del proyecto
PROJECT_ROOT = Path(__file__).parent.parent

# Calidades de video
class VideoQuality(Enum):
    """Opciones de calidad de video"""
    LOW = (480, 480)        # 480p
    MEDIUM = (720, 720)     # 720p
    HIGH = (1080, 1080)     # 1080p
    ULTRA = (1440, 1440)    # 4K

# Formatos de exportación
class ExportFormat(Enum):
    """Formatos de exportación soportados"""
    MP4 = 'mp4'
    AVI = 'avi'
    MOV = 'mov'
    WEBM = 'webm'

# Velocidades de fotogramas
class FrameRate(Enum):
    """Velocidades de fotogramas disponibles"""
    FPS_24 = 24
    FPS_30 = 30
    FPS_60 = 60

# Idiomas soportados
LANGUAGES = [
    ('es', 'Español'),
    ('en', 'English'),
    ('fr', 'Français'),
    ('de', 'Deutsch'),
    ('pt', 'Português'),
    ('it', 'Italiano'),
]

# Configuración de API
NIMVIDEO_API_BASE_URL = "https://api.nimvideo.com/v1"
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Configuración de UI
APP_NAME = "Video Generator App"
APP_VERSION = "1.0.0"
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 800

# Temas
THEMES = ['dark', 'light']
DEFAULT_THEME = 'dark'

# Límites
MAX_VIDEO_DURATION = 300  # 5 minutos en segundos
MIN_VIDEO_DURATION = 5
MAX_PROJECT_SIZE = 1024 * 1024 * 100  # 100 MB
