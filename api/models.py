#!/usr/bin/env python3
"""
Modelos de datos para la API de NimVideo
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Avatar(BaseModel):
    """Modelo de Avatar"""
    id: str
    name: str
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None


class Voice(BaseModel):
    """Modelo de Voz"""
    id: str
    name: str
    language: str
    gender: Optional[str] = None


class VideoConfig(BaseModel):
    """Configuración de Video"""
    width: int = 1080
    height: int = 1080
    fps: int = 30
    duration: int = 60
    quality: str = 'HIGH'


class VideoProject(BaseModel):
    """Proyecto de Video"""
    id: str
    name: str
    description: Optional[str] = None
    text: str
    avatar: Avatar
    voice: Voice
    config: VideoConfig
    created_at: datetime
    modified_at: datetime
    status: str = 'draft'


class GeneratedVideo(BaseModel):
    """Video Generado"""
    id: str
    project_id: str
    video_url: Optional[str] = None
    status: str  # 'processing', 'completed', 'failed'
    created_at: datetime
    completed_at: Optional[datetime] = None
