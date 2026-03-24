# ProyectoEUDE

Análisis integral del negocio de EUDE (escuela de negocios) y los servicios que ofrece. Este proyecto establece la base de experimentación, procesamiento de datos y modelado para los objetivos descritos.

## Estructura del Proyecto

* `data/`: Contiene los conjuntos de datos del proyecto (`raw` para originales, `processed` para datos limpios, `external` para fuentes de terceros).
* `notebooks/`: Cuadernos de Jupyter para la exploración de datos, análisis exploratorio (EDA) y prototipos iniciales.
* `src/`: Código fuente del proyecto con la lógica de procesamiento, visualización y modelado.
* `tests/`: Pruebas automatizadas del código en `src/`.

## Configuración del Entorno de Desarrollo

1. **Clonar el repositorio:**
   Si existe un repositorio en Git, clónalo en tu entorno local.

2. **Crear un entorno virtual de Python:**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`

4. **Instalar dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar variables de entorno:**
   - Copiar el archivo `.env.example` a `.env`
   - Ajustar los valores en `.env` según corresponda para tu entorno local.

## Convenciones

- Usar `notebooks/` sólo para experimentación.
- Cualquier función o clase consolidada debe ser movida a `src/`.
