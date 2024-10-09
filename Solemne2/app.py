from flask import Flask, request
import csv
import os

app = Flask(__name__)

# Ruta donde se guardarán los datos en la microSD
csv_file_path = 'datos.csv'

# Ruta para recibir los datos
@app.route('/datos', methods=['POST'])
def recibir_datos():
    data = request.json

    # Extraer los datos recibidos
    temperatura = data['temperature']
    humedad = data['humidity']
    luz = data['light']
    uv = data['uv']
    co2 = data['co2']

    # Guardar los datos en el archivo CSV
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([temperatura, humedad, luz, uv, co2])

    return "Datos recibidos y guardados", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
