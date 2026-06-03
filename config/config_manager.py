#!/usr/bin/env python3
"""
Gestor de configuración de la aplicación
"""

import json
from pathlib import Path
from typing import Any, Dict
from utils.constants import DEFAULT_THEME, APP_VERSION


class ConfigManager:
    """
    Gestiona las configuraciones de la aplicación
    """
    
    def __init__(self):
        self.config_dir = Path('config')
        self.config_dir.mkdir(exist_ok=True)
        
        self.settings_file = self.config_dir / 'settings.json'
        self.presets_file = self.config_dir / 'presets.json'
        
        self.settings = self._load_settings()
        self.presets = self._load_presets()
    
    def _load_settings(self) -> Dict[str, Any]:
        """
        Carga las configuraciones desde archivo
        """
        default_settings = {
            'app_version': APP_VERSION,
            'theme': DEFAULT_THEME,
            'api_key': '',
            'auto_save': True,
            'auto_save_interval': 300,
            'last_project': None,
            'recent_projects': [],
            'quality': 'HIGH',
            'fps': 30,
            'language': 'es',
        }
        
        if self.settings_file.exists():
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    default_settings.update(loaded)
            except Exception as e:
                print(f"Error loading settings: {e}")
        
        return default_settings
    
    def _load_presets(self) -> Dict[str, Any]:
        """
        Carga los presets de video
        """
        default_presets = {
            'presets': [
                {
                    'name': 'YouTube',
                    'width': 1920,
                    'height': 1080,
                    'fps': 30,
                    'duration': 60,
                },
                {
                    'name': 'TikTok',
                    'width': 1080,
                    'height': 1920,
                    'fps': 30,
                    'duration': 60,
                },
                {
                    'name': 'Instagram',
                    'width': 1080,
                    'height': 1080,
                    'fps': 24,
                    'duration': 60,
                },
                {
                    'name': 'Twitter',
                    'width': 1200,
                    'height': 675,
                    'fps': 24,
                    'duration': 60,
                },
            ]
        }
        
        if self.presets_file.exists():
            try:
                with open(self.presets_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading presets: {e}")
        
        return default_presets
    
    def save_settings(self) -> None:
        """
        Guarda las configuraciones en archivo
        """
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Obtiene un valor de configuración
        """
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Establece un valor de configuración
        """
        self.settings[key] = value
        self.save_settings()
