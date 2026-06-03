#!/usr/bin/env python3
"""
Script para empaquetar la aplicación como .exe
Usa PyInstaller para crear un ejecutable standalone
"""

import os
import sys
import shutil
from pathlib import Path

try:
    import PyInstaller.__main__
except ImportError:
    print("PyInstaller no está instalado. Instálalo con: pip install PyInstaller")
    sys.exit(1)


def build_exe():
    """
    Construye el ejecutable .exe
    """
    project_root = Path(__file__).parent
    
    print("🔨 Construyendo Video Generator App...")
    print(f"📁 Directorio: {project_root}")
    
    # Limpiar directorios previos
    for dir_name in ['build', 'dist']:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"🗑️  Limpiando {dir_name}/")
            shutil.rmtree(dir_path)
    
    # Especificaciones de PyInstaller
    specs = [
        str(project_root / 'main.py'),
        '--name=VideoGeneratorApp',
        '--onefile',
        '--windowed',
        f'--icon={project_root / "assets" / "icon.ico"}',
        '--add-data=config:config',
        '--add-data=assets:assets',
        '--collect-all=PyQt5',
        '--hidden-import=PyQt5',
        '--hidden-import=cv2',
        '--clean',
        f'--distpath={project_root / "dist"}',
        f'--buildpath={project_root / "build"}',
    ]
    
    print("\n🚀 Ejecutando PyInstaller...\n")
    
    try:
        PyInstaller.__main__.run(specs)
        
        exe_path = project_root / 'dist' / 'VideoGeneratorApp.exe'
        
        if exe_path.exists():
            print(f"\n✅ ¡Éxito! Ejecutable creado en:")
            print(f"   {exe_path}")
            print(f"\n📊 Tamaño: {exe_path.stat().st_size / (1024*1024):.2f} MB")
            return True
        else:
            print("\n❌ Error: El ejecutable no se creó correctamente")
            return False
            
    except Exception as e:
        print(f"\n❌ Error durante la compilación: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = build_exe()
    sys.exit(0 if success else 1)
