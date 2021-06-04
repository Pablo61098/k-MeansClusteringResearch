- El archivo variables_seleccionadas.csv tiene los valores para las 42 variables
seleccionadas. Además, se puso ceros en los valores no existentes de cantidades.
Este proceso se hizo con Weka (con el filter ReplaceMissingValueUserInput), 
a partir del dataset original.
- Se usa script.py para poner los datos como se describen en el mismo. Toma como
entrada el archivo variables_seleccionadas.csv y da como salida el archivo
datos_sin_normalizar.csv.
- Luego en Weka se procede a hacer la normalizacion de este archivo, dando como
salida el archivo datos_normalizados.csv. Se usa el filter Normalize.

