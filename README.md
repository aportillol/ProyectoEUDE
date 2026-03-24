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

## ⚖️ Disclaimer y Descargo de Responsabilidad
1. Propósito Estrictamente Académico
Este repositorio y el código, modelos y análisis de datos que contiene han sido desarrollados con fines exclusiva y estrictamente académicos y de investigación. Este proyecto forma parte de las actividades prácticas y de estudio en el ámbito del Big Data y Business Analytics. No tiene fines comerciales, ni pretende servir como asesoramiento financiero, empresarial o legal para la toma de decisiones en entornos reales de producción.

2. Origen y Gobernabilidad de los Datos
Todos los análisis realizados en este proyecto se basan en el cruce de información proveniente de fuentes públicas, abiertas y encuestas de dominio público. Se ha aplicado un marco estricto de gobernabilidad del dato, garantizando que no se ha utilizado, expuesto ni procesado Información de Identificación Personal (PII) o datos confidenciales privados protegidos por normativas de privacidad (como el RGPD). Cualquier coincidencia con datos no públicos es puramente accidental.

3. Gobernanza Agéntica y Modelos de Inteligencia Artificial
En las fases donde se aplican agentes de Inteligencia Artificial o modelos del lenguaje (LLMs) para el procesamiento o análisis de la información, se ha actuado bajo los principios de la gobernanza agéntica. Las conclusiones generadas por estos modelos están sujetas a los sesgos inherentes de los datos de entrenamiento y a los márgenes de error probabilísticos propios de la IA. Los resultados deben interpretarse como ejercicios de exploración analítica y no como verdades absolutas.

4. Exención de Responsabilidad Institucional
Las opiniones, metodologías, interpretaciones de datos y conclusiones expresadas en este repositorio son de exclusiva responsabilidad del autor. Este proyecto es independiente y no representa la postura oficial, metodológica o académica de EUDE Business School, su equipo directivo, claustro de profesores o tutores. La institución y su personal quedan exentos de cualquier responsabilidad legal, ética o comercial derivada del uso, réplica o interpretación que terceros hagan de este repositorio.
