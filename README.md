# AED-P3
Proyecto final del ramo Análisis Exploratorio de datos

## 🚀 Configuración del Entorno

### Opción 1: Configuración Automática
Ejecuta el script de configuración automática:
```bash
python setup_env.py
```

### Opción 2: Configuración Manual

1. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual:**
   ```bash
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 📁 Estructura del Proyecto
```
AED-P3/
├── data/                           # Datos del proyecto
│   ├── online_shoppers_intention.csv
│   └── scaled.csv
├── main.ipynb                      # Notebook principal
├── requirements.txt                # Dependencias Python
├── .env                           # Variables de entorno
├── setup_env.py                   # Script de configuración
└── README.md                      # Este archivo
```

## 🔧 Variables de Entorno
El archivo `.env` contiene configuraciones del proyecto como:
- Rutas de datos
- Configuración de visualización
- Parámetros de análisis
- Configuración de Jupyter

## 📊 Ejecución
1. Activa el entorno virtual
2. Ejecuta Jupyter:
   ```bash
   jupyter lab
   # o
   jupyter notebook
   ```
3. Abre `main.ipynb`

## 📦 Dependencias Principales
- **pandas**: Manipulación de datos
- **numpy**: Computación numérica
- **matplotlib/seaborn**: Visualización
- **scikit-learn**: Machine Learning
- **imbalanced-learn**: Manejo de datos desbalanceados
