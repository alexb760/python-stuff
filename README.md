# bvc-acciones-colombia

## Objetivo:
Descargar y procesar de manera simple usando python las acciones de Colombia mediante su API.

## Restricciones:
1. API no es de uso publico.
2. API tiene restriccion de numero de intentos por dia.
3. API tiene un rango limite de fechas de 6 meses.

## Pasos:
1. Obteniendo la API. solo es necesesario usar cualquier herramienta de desarrollador en el explorador
   y rastrear el llamado cuando exportamos data desde la página de la bvc.
2. Obteniendo el listado de acciones objetivo desde la página de la bvc, copy-paste (no encontré ninguna API)
4. Mediante la API obtenida en el paso (1) descargar los historicos por cada activo. en este caso desde 2020 - 2021
5. Usando Pandas unir en un solo archivo de excel los 4 archivos (2020 a 2021 = 4 periodos de 6 meses) 
   de excel generdos en el paso (4).
6. Usando pandas tomar todos los detalles consolidados por accion generados en el paso (5) extraer:
   fecha, nombre activo, y precio cierre hacer un pivote tomando como indice la fecha y columna el nombre del actiovo
   pasarlo a excel para luego aplicar posteriores analisis y así elaborar nuestro portafolio de inversion.

## Requerimientos Técnicos:
1. Python 3.7
### Librerias:
    1. pandas 1.3.5 ´pip install pandas´
    2. xlrd 2.0.1 ´pip install xlrd´ (desde la bvc se descarga en formato xls old excel version)
    3. requests 2.26.0 ´pip install requests´
    4. dateutil 2.8.2 ´pip install dateutil´

## Ejecutando los scripts:
### Descargando historico de los activos en un periodo de 2 años (2020 a 2021)
   ´´shell
        python get-stoks.py
   ´´
### Consolidando los detalles de todos los activos consolidados y pivoteando la información.
  ´´shell
      python pivote_tables_data.py
  ´´

## Lo siguiente:
1. usuando pandas y numpy realizar el analisis de los diferentes portafolios que podemos realizar y sus rentabilidades esperadas.
## Warning:
 Bajo ningún motivo consideramos esto como un consejo financiero. primero la información viene de datos históricos y nadie puede
 predecir el futuro

## Lo siguiente:
1. usuando pandas y numpy realizar el analisis de los diferentes portafolios que podemos realizar y sus rentabilidades esperadas.
## Warning:
 Bajo ningún motivo consideramos esto como un consejo financiero. primero la información viene de datos históricos y nadie puede
 predecir el futuro.
