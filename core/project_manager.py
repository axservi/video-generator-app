#!/usr/bin/env python3
"""
Gestor de proyectos
"""

import json
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime


class ProjectManager:
    """
    Gestiona los proyectos de video
    """
    
    def __init__(self, projects_dir: str = 'projects', logger=None):
        self.projects_dir = Path(projects_dir)
        self.projects_dir.mkdir(exist_ok=True)
        self.logger = logger
    
    def create_project(self, name: str, description: str = '') -> Dict[str, Any]:
        """
        Crea un nuevo proyecto
        """
        project_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        project = {
            'id': project_id,
            'name': name,
            'description': description,
            'created_at': datetime.now().isoformat(),
            'modified_at': datetime.now().isoformat(),
            'videos': [],
            'config': {}
        }
        
        self._save_project(project)
        self.logger.info(f"Proyecto creado: {name} ({project_id})")
        
        return project
    
    def load_project(self, project_id: str) -> Dict[str, Any]:
        """
        Carga un proyecto existente
        """
        project_file = self.projects_dir / f"{project_id}.json"
        
        if not project_file.exists():
            raise FileNotFoundError(f"Proyecto no encontrado: {project_id}")
        
        with open(project_file, 'r', encoding='utf-8') as f:
            project = json.load(f)
        
        self.logger.info(f"Proyecto cargado: {project['name']}")
        return project
    
    def save_project(self, project: Dict[str, Any]) -> None:
        """
        Guarda un proyecto
        """
        project['modified_at'] = datetime.now().isoformat()
        self._save_project(project)
        self.logger.info(f"Proyecto guardado: {project['name']}")
    
    def _save_project(self, project: Dict[str, Any]) -> None:
        """
        Guarda el proyecto en archivo
        """
        project_file = self.projects_dir / f"{project['id']}.json"
        
        with open(project_file, 'w', encoding='utf-8') as f:
            json.dump(project, f, indent=4, ensure_ascii=False)
    
    def list_projects(self) -> List[Dict[str, Any]]:
        """
        Lista todos los proyectos
        """
        projects = []
        
        for project_file in self.projects_dir.glob('*.json'):
            with open(project_file, 'r', encoding='utf-8') as f:
                projects.append(json.load(f))
        
        return sorted(projects, key=lambda p: p['modified_at'], reverse=True)
    
    def delete_project(self, project_id: str) -> None:
        """
        Elimina un proyecto
        """
        project_file = self.projects_dir / f"{project_id}.json"
        
        if project_file.exists():
            project_file.unlink()
            self.logger.info(f"Proyecto eliminado: {project_id}")
