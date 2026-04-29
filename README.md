# Curso de Geomática y Sostenibilidad

Material base para introducir conceptos de geomática, análisis espacial, fuentes de datos geoespaciales y visualización de datos energéticos.

Profesor: Junior Antonio Calvo Montañez

## Estructura del proyecto

- `modules/module01.ipynb`: introducción a geometrías, CRS, análisis vectorial y mapas temáticos.
- `modules/module02.ipynb`: fuentes de datos geomáticos, servicios OGC y consumo de información geoespacial.
- `modules/module03.ipynb`: análisis de redes, radiación solar, PSH y producción fotovoltaica estimada.
- `docker/fastapi-qgis/data/`: datos usados por el contenedor QGIS.
- `docker/fastapi-qgis/output/`: resultados generados por los algoritmos.
- `docker/fastapi-qgis/project/`: proyectos QGIS usados como contexto de análisis.
- `compose.yaml`: definición del servicio Docker `fastapi-qgis`.

## Instalación del entorno Python

Se recomienda usar `conda`.

```bash
conda create -n GyS-env python=3.12.3
conda activate GyS-env
pip install -r requirements.txt
pip install ipykernel pygments
```

## Uso del contenedor QGIS

El proyecto usa un contenedor llamado `fastapi-qgis` para ejecutar herramientas de QGIS, GDAL y GRASS desde los notebooks.

Levantar el servicio:

```bash
docker compose up -d
```

Entrar al contenedor:

```bash
docker exec -it fastapi-qgis bash
```

Saber que Python tiene QGIS instalado en la imagen:

```bash
docker exec -it fastapi-qgis python3
```

Ver paquetes instalados:

```bash
docker exec -it fastapi-qgis dpkg -l
```

Listar todos los algoritmos desde `qgis_process`:

```bash
docker exec -it fastapi-qgis qgis_process list
```

Ver los parámetros de un algoritmo:

```bash
docker exec -it fastapi-qgis qgis_process help native:shortestpathpointtopoint
```

Cargar `grassprovider` en `qgis_process`:

```bash
docker exec -it fastapi-qgis qgis_process plugins
docker exec -it fastapi-qgis qgis_process plugins enable grassprovider
docker exec -it fastapi-qgis qgis_process list | findstr grass
```

Nota: en Linux o macOS, si `findstr` no está disponible, se puede usar:

```bash
docker exec -it fastapi-qgis qgis_process list | grep grass
```

## Módulo 01: introducción a la geomática

El notebook `module01.ipynb` está organizado como una introducción progresiva:

1. Geometrías básicas con `shapely`: puntos, líneas, polígonos y geometrías múltiples.
2. Mapas, proyecciones y sistemas de referencia (CRS): medición de áreas y distancias, grados y reproyección.
3. Lectura y análisis vectorial con `geopandas`: áreas, perímetros, centroides, buffers, intersecciones y clips.
4. Aplicación temática: energía y sostenibilidad mediante mapas coropléticos y visualizaciones interactivas.

## Módulo 02: fuentes de datos geomáticos

El notebook `module02.ipynb` introduce el acceso a información geoespacial mediante servicios y catálogos:

- WMS: visualización de mapas rasterizados desde servidores.
- WFS: consulta y descarga de entidades vectoriales.
- CSW: búsqueda de metadatos geoespaciales.
- Lectura, exploración y visualización de datos obtenidos desde servicios externos.

## Módulo 03: redes y radiación solar

El notebook `module03.ipynb` trabaja con dos aplicaciones geomáticas:

1. Análisis de redes:
   Se usa `native:shortestpathpointtopoint` para calcular la ruta más corta entre dos puntos sobre una red vectorial. El resultado se guarda como `ruta.gpkg`.

2. Radiación solar:
   Se parte de un DEM para calcular pendiente, orientación, insolación y radiación global diaria con algoritmos de GRASS desde `qgis_process`.

3. PSH y producción solar:
   A partir del raster `radiacion_global_diaria.tif`, se calculan las Horas Sol Pico y una producción fotovoltaica diaria estimada.

Resultados principales del módulo:

- `docker/fastapi-qgis/output/ruta.gpkg`
- `docker/fastapi-qgis/output/radiacion_solar/slope.tif`
- `docker/fastapi-qgis/output/radiacion_solar/aspect.tif`
- `docker/fastapi-qgis/output/radiacion_solar/insolacion.tif`
- `docker/fastapi-qgis/output/radiacion_solar/radiacion_global_diaria.tif`

## Datos sobre energía de Our World in Data

La práctica del módulo 1 usa el archivo público:

- Fuente: https://github.com/owid/energy-data
- CSV usado en el notebook:
  `https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv`

Es un dataset no geoespacial: una tabla con indicadores por países y por año. Para hacer mapas, se une esa tabla con la capa espacial `world.gpkg`.

### Columnas de uso en el Módulo 01

El notebook trabaja con estas variables:

- `country`: nombre del país.
- `year`: año del registro.
- `coal_production`: producción de carbón.
- `gas_production`: producción de gas.
- `oil_production`: producción de petróleo.

En este ejercicio, estas variables se interpretan en `TWh`.

## Dependencias principales

- `numpy`
- `pandas`
- `geopandas`
- `matplotlib`
- `plotly`
- `nbformat`
- `mapclassify`
- `rasterio`
- `fastapi`
- `pydantic`
- `pydantic-settings`
