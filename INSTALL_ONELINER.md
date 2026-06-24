# 🚀 Instalación de Una Línea - Fote CLI

## Windows (PowerShell)

### Instalación Completa (Recomendado)
```powershell
irm https://raw.githubusercontent.com/765g/Fote/master/fote.py | Out-File -FilePath "$env:USERPROFILE\fote.py" -Encoding UTF8; python "$env:USERPROFILE\fote.py" --help; Write-Host "`nFote instalado! Usa: python $env:USERPROFILE\fote.py -s" -ForegroundColor Green
```

### Instalación con Alias (Más Fácil)
```powershell
curl -o "$env:USERPROFILE\fote.py" https://raw.githubusercontent.com/765g/Fote/master/fote.py; if (!(Test-Path $PROFILE)) { New-Item -Path $PROFILE -ItemType File -Force }; Add-Content -Path $PROFILE -Value "`nfunction fote { python $env:USERPROFILE\fote.py @args }"; . $PROFILE; Write-Host "Fote instalado! Usa: fote -s" -ForegroundColor Green
```

Después de instalar con alias, usa:
```powershell
fote -s
```

---

## Linux / macOS (Bash/Zsh)

### Instalación Completa
```bash
curl -o ~/fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py && chmod +x ~/fote.py && echo "alias fote='python3 ~/fote.py'" >> ~/.bashrc && source ~/.bashrc && echo "Fote instalado! Usa: fote -s"
```

### Para Zsh (macOS)
```bash
curl -o ~/fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py && chmod +x ~/fote.py && echo "alias fote='python3 ~/fote.py'" >> ~/.zshrc && source ~/.zshrc && echo "Fote instalado! Usa: fote -s"
```

---

## 📦 Instalación Manual (Si lo anterior no funciona)

### Paso 1: Descargar
```bash
# Windows PowerShell
curl -o fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py

# Linux/macOS
wget https://raw.githubusercontent.com/765g/Fote/master/fote.py
# o
curl -O https://raw.githubusercontent.com/765g/Fote/master/fote.py
```

### Paso 2: Instalar Dependencias
```bash
pip install requests
```

### Paso 3: Ejecutar
```bash
python fote.py -s
```

---

## ✨ Uso Rápido

Después de instalar:

```bash
# Escoger modelo y chatear
fote -s

# Mensaje rápido
fote "explica machine learning"

# Con modelo específico
fote -m codestral "escribe código python"

# Modo interactivo
fote -i

# Ver modelos disponibles
fote -l

# Ayuda
fote -h
```

---

## 🔧 Requisitos

- **Python 3.8+** (Python 3.7 o superior)
- **pip** (viene con Python)
- **Internet** (para descargar y usar la API)

### Verificar Python:
```bash
python --version
# o
python3 --version
```

### Instalar Python:
- **Windows:** https://python.org/downloads
- **macOS:** `brew install python3` o desde python.org
- **Linux:** `sudo apt install python3 python3-pip` (Ubuntu/Debian)

---

## 📋 Lo Que Hace el Comando

1. Descarga `fote.py` desde GitHub
2. Lo guarda en tu carpeta de usuario
3. Crea un alias `fote` para ejecutarlo fácilmente
4. Instala la dependencia `requests` (si no está)
5. ¡Listo para usar!

---

## 🎯 COMANDO MÁS SIMPLE (Copiar y Pegar)

### Windows:
```powershell
curl -o "$env:USERPROFILE\fote.py" https://raw.githubusercontent.com/765g/Fote/master/fote.py; python "$env:USERPROFILE\fote.py" -s
```

### Linux/macOS:
```bash
curl -o ~/fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py && python3 ~/fote.py -s
```

---

## 🆘 Solución de Problemas

### "python no encontrado"
Usa `python3` en lugar de `python`:
```bash
python3 fote.py -s
```

### "requests no encontrado"
```bash
pip install requests
# o
pip3 install requests
```

### "comando no reconocido"
Reinicia tu terminal después de la instalación.

### Desinstalar
```bash
# Eliminar archivo
rm ~/fote.py  # Linux/macOS
del %USERPROFILE%\fote.py  # Windows

# Eliminar alias
# Edita ~/.bashrc o ~/.zshrc y elimina la línea del alias
```

---

**Repositorio:** https://github.com/765g/Fote  
**Autor:** 765g  
**Versión:** 1.0.0
