import tkinter as tk
import serial
import time
import serial.tools.list_ports
import csv

#DHT pin 2
#LDR Pin A0
#UV Pin A1
#CO2 Pin A2

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

def findArduino(portsFound):
    commPort = 'None'
    numConnection = len(portsFound)
    
    for i in range(0,numConnection):
        port = foundPorts[i]
        strPort = str(port)
        
        if 'CH' in strPort: 
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])

    return commPort
            

foundPorts = get_ports()        
connectPort = findArduino(foundPorts)

if connectPort != 'None':
    arduino = serial.Serial(connectPort, baudrate=9600, timeout=1)
    print('Connected to ' + connectPort)
else:
    print('Connection Issue!')
    exit(404)

print('DONE')

# Abrir el archivo en modo 'append' para agregar datos
csv_file_path = 'datos.csv'

# Crear o abrir el archivo CSV
with open(csv_file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir la cabecera del archivo solo si está vacío o es la primera vez
    if file.tell() == 0:
        writer.writerow(["Temperatura (°C)", "Humedad (%)", "Nivel de luz (%)", "Nivel UV", "Nivel CO2"])

def convert_to_percentage(sensor_value):
    min_value = 0    # 0% de luz
    max_value = 750  # 100% de luz
    percentage = (sensor_value - min_value) / (max_value - min_value) * 100.0
    
    if percentage < 0:
        percentage = 0
    if percentage > 100:
        percentage = 100
    
    return round(percentage, 1)

# Función para actualizar los datos
def update_data():
    if arduino.in_waiting > 0:
        rawString = arduino.readline().decode('utf-8').strip()
        data = rawString.split(",")
        print(data)
        
        # Actualizar los datos en la interfaz gráfica
        temp_label.config(text=f"Temp: {data[0]} °C")
        humidity_label.config(text=f"Humidity: {data[1]} %")
        light_label.config(text=f"Light Level: {convert_to_percentage(int(data[2]))} %")
        uv_label.config(text=f"UV Level: {data[3]}")
        co2_label.config(text=f"CO2 Level: {data[4]}")

        # Guardar los datos en el archivo CSV
        with open(csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data[0], data[1], convert_to_percentage(int(data[2])), data[3], data[4]])
    
    root.after(1500, update_data)  # Actualiza cada 1.5 segundos

# Configuración de la ventana principal
root = tk.Tk()
root.title("Datos del Arduino")

root.geometry("250x300")
root.resizable(False, False)

# Etiquetas para mostrar los datos
temp_label = tk.Label(root, text="Temp: -- C", font=("Helvetica", 16))
temp_label.pack(pady=10)

humidity_label = tk.Label(root, text="Humidity: -- %", font=("Helvetica", 16))
humidity_label.pack(pady=10)

light_label = tk.Label(root, text="Light Level: --", font=("Helvetica", 16))
light_label.pack(pady=10)

uv_label = tk.Label(root, text="UV Level: --", font=("Helvetica", 16))
uv_label.pack(pady=10)

co2_label = tk.Label(root, text="CO2 Level: --", font=("Helvetica", 16))
co2_label.pack(pady=10)

# Inicia la actualización de datos
update_data()

# Ejecuta la interfaz gráfica
root.mainloop()
