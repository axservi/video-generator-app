#!/usr/bin/env python3
"""
Sistema de logging para la aplicación
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


def setup_logger(name='VideoGeneratorApp', log_level=logging.INFO):
    """
    Configura el logger de la aplicación
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Crear directorio de logs si no existe
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)
    
    # Formato de logs
    log_format = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para archivo
    log_file = logs_dir / f'app_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    
    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    return logger
