#!/usr/bin/env python3
"""
Cliente para la API de NimVideo
"""

import requests
import json
from typing import Dict, Any, Optional
from utils.constants import NIMVIDEO_API_BASE_URL, REQUEST_TIMEOUT, MAX_RETRIES
from utils.validators import Validator


class NimVideoClient:
    """
    Cliente para interactuar con la API de NimVideo
    """
    
    def __init__(self, api_key: str, logger=None):
        """
        Inicializa el cliente de NimVideo
        
        Args:
            api_key: Clave API de NimVideo
            logger: Logger de la aplicación
        """
        if not Validator.validate_api_key(api_key):
            raise ValueError("API Key inválida")
        
        self.api_key = api_key
        self.base_url = NIMVIDEO_API_BASE_URL
        self.logger = logger
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        retries: int = 0
    ) -> Dict[str, Any]:
        """
        Realiza una solicitud HTTP a la API
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
            elif method.upper() == 'POST':
                response = self.session.post(url, json=data, timeout=REQUEST_TIMEOUT)
            elif method.upper() == 'PUT':
                response = self.session.put(url, json=data, timeout=REQUEST_TIMEOUT)
            elif method.upper() == 'DELETE':
                response = self.session.delete(url, timeout=REQUEST_TIMEOUT)
            else:
                raise ValueError(f"Método HTTP no soportado: {method}")
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            if retries < MAX_RETRIES:
                self.logger.warning(f"Reintentando ({retries+1}/{MAX_RETRIES})...")
                return self._make_request(method, endpoint, data, retries + 1)
            
            self.logger.error(f"Error en solicitud: {e}")
            raise
    
    def create_video(self, text: str, avatar: str, **kwargs) -> Dict[str, Any]:
        """
        Crea un nuevo video
        """
        payload = {
            'text': text,
            'avatar': avatar,
            **kwargs
        }
        
        self.logger.info(f"Creando video: {text[:50]}...")
        return self._make_request('POST', '/videos', payload)
    
    def get_avatars(self) -> Dict[str, Any]:
        """
        Obtiene la lista de avatares disponibles
        """
        self.logger.info("Obteniendo lista de avatares")
        return self._make_request('GET', '/avatars')
    
    def get_voices(self, language: str = 'es') -> Dict[str, Any]:
        """
        Obtiene las voces disponibles para un idioma
        """
        self.logger.info(f"Obteniendo voces para {language}")
        return self._make_request('GET', f'/voices?language={language}')
    
    def get_video_status(self, video_id: str) -> Dict[str, Any]:
        """
        Obtiene el estado de un video
        """
        return self._make_request('GET', f'/videos/{video_id}')
    
    def export_video(self, video_id: str, format: str = 'mp4') -> Dict[str, Any]:
        """
        Exporta un video en el formato especificado
        """
        self.logger.info(f"Exportando video {video_id} en formato {format}")
        return self._make_request('POST', f'/videos/{video_id}/export', {'format': format})
