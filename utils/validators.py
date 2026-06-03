#!/usr/bin/env python3
"""
Validadores para inputs y configuraciones
"""

import re
from pathlib import Path


class Validator:
    """
    Clase para validaciones comunes
    """
    
    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        """
        Valida un API key de NimVideo
        """
        if not api_key or len(api_key) < 20:
            return False
        return re.match(r'^[a-zA-Z0-9_-]+$', api_key) is not None
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Valida una dirección de email
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_text(text: str, min_length: int = 1, max_length: int = 10000) -> bool:
        """
        Valida longitud de texto
        """
        return min_length <= len(text.strip()) <= max_length
    
    @staticmethod
    def validate_file_path(path: str) -> bool:
        """
        Valida que la ruta sea accesible
        """
        try:
            Path(path).resolve()
            return True
        except (OSError, ValueError):
            return False
    
    @staticmethod
    def validate_project_name(name: str) -> bool:
        """
        Valida nombre de proyecto
        """
        if not name or len(name) > 100:
            return False
        return re.match(r'^[a-zA-Z0-9_\- ]+$', name) is not None
