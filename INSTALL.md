# Installation Guide

## Prerequisites
- Windows 10/11
- Python 3.9 or higher
- 2GB RAM minimum
- Internet connection
- NimVideo API Key

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/axservi/video-generator-app.git
cd video-generator-app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
python main.py
```

## Building EXE

### 1. Install PyInstaller
```bash
pip install PyInstaller
```

### 2. Build Executable
```bash
python build.py
```

The executable will be in: `dist/VideoGeneratorApp.exe`

## First Run

1. Get your NimVideo API Key
2. Open the application
3. Go to Menu > Preferences > API
4. Enter your API Key
5. Create a new project and start generating videos!
