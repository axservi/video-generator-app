# Video Generator App - NimVideo Desktop

Aplicación de escritorio (.exe) para generar videos realistas con avatares para redes sociales usando la tecnología de NimVideo.

## Características

✨ **Interfaz Gráfica Moderna**
- Diseño intuitivo y responsivo
- Tema oscuro/claro
- Previsualización en tiempo real

🎥 **Generación de Videos**
- Integración con API de NimVideo
- Sincronización de labios automática
- Múltiples avatares disponibles
- Exportación en múltiples formatos

📝 **Gestión de Proyectos**
- Guardar y cargar proyectos
- Historial de videos generados
- Templates y presets predefinidos
- Biblioteca de efectos

⚙️ **Configuración Avanzada**
- Calidad de video (720p, 1080p, 4K)
- Velocidad de fotogramas customizable
- Voces y idiomas múltiples
- Efectos y transiciones

## Requisitos

- Windows 10/11
- Python 3.9+
- 2GB RAM mínimo
- Conexión a Internet
- API Key de NimVideo

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Construcción del .exe

```bash
python build.py
```

El ejecutable estará en la carpeta `dist/`

## Estructura del Proyecto

```
video-generator-app/
├── main.py
├── build.py
├── requirements.txt
├── config/
│   ├── settings.json
│   ├── presets.json
│   └── themes.json
├── ui/
│   ├── main_window.py
│   ├── editor_panel.py
│   └── styles.py
├── api/
│   ├── nimvideo_client.py
│   ├── auth.py
│   └── models.py
├── core/
│   ├── video_processor.py
│   ├── project_manager.py
│   └── export_manager.py
└── utils/
    ├── logger.py
    ├── validators.py
    └── constants.py
```

## Licencia

MIT License
