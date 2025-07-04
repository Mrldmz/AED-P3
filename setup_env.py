#!/usr/bin/env python3
"""
Script para configurar el entorno de desarrollo del proyecto AED-P3
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Ejecuta un comando y maneja errores"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e.stderr}")
        return None

def setup_environment():
    """Configura el entorno virtual y las dependencias"""
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    print("🚀 Configurando entorno para AED-P3")
    print("=" * 50)
    
    # Verificar si Python está disponible
    python_cmd = "python" if sys.platform == "win32" else "python3"
    
    # Crear entorno virtual
    venv_path = project_root / "venv"
    if not venv_path.exists():
        run_command(f"{python_cmd} -m venv venv", "Creando entorno virtual")
    else:
        print("✅ Entorno virtual ya existe")
    
    # Activar entorno virtual y instalar dependencias
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Actualizar pip
    run_command(f"{pip_cmd} install --upgrade pip", "Actualizando pip")
    
    # Instalar dependencias
    run_command(f"{pip_cmd} install -r requirements.txt", "Instalando dependencias")
    
    print("\n🎉 ¡Configuración completada!")
    print("\nPara activar el entorno virtual:")
    if sys.platform == "win32":
        print("  venv\\Scripts\\activate")
    else:
        print("  source venv/bin/activate")
    
    print("\nPara ejecutar Jupyter:")
    print("  jupyter lab")
    print("  # o")
    print("  jupyter notebook")

if __name__ == "__main__":
    setup_environment()
