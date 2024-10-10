import tkinter as tk
from PIL import Image, ImageTk
import serial
import time
import serial.tools.list_ports

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
    arduino = serial.Serial(connectPort,baudrate = 9600, timeout=1)
    print('conectado a' + connectPort)

else:
    print('error de conexion!')
    exit(404)

print('OK')

# Configura el puerto y la velocidad de baudios
#arduino = serial.Serial('COM5', 9600)  # Cambia 'COM5' por el puerto correcto en tu sistema
#time.sleep(2)  # Espera a que el puerto se inicialice

# Configuración de la ventana principal
root = tk.Tk()
root.title("Estacion meteorológicas")

# Función para redimensionar imágenes
def resize_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size, Image.Resampling.LANCZOS)  # Cambiado a LANCZOS
    return ImageTk.PhotoImage(image)

def convert_to_percentage(sensor_value):
    # Convertir el valor del sensor a porcentaje
    min_value = 0    # 0% de luz
    max_value = 850  # 100% de luz
    percentage = (sensor_value - min_value) / (max_value - min_value) * 100.0
    
    # Asegurarse de que el porcentaje esté en el rango de 0 a 100
    if percentage < 0:
        percentage = 0
    if percentage > 100:
        percentage = 100
    
    return round(percentage, 1)

# Cargar y redimensionar imágenes de emojis
images = {
    "cold": resize_image("cold.png", (50, 50)),
    "hot": resize_image("hot.jfif", (50, 50)),
    "happy": resize_image("happy.png", (50, 50)),
    "cloud": resize_image("cloud.png", (50, 50)),
    "rain": resize_image("rain.png", (50, 50)),
    "moon": resize_image("moon.png", (50, 50)),
    "sun": resize_image("sun.png", (50, 50)),
    "low_uv": resize_image("low_uv.jpg", (50, 50)),
    "high_uv": resize_image("high_uv.jpg", (50, 50)),
    "green": resize_image("green.png", (50, 50)),
    "yellow": resize_image("yellow.png", (50, 50)),
    "red": resize_image("red.png", (50, 50))
}

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

# Mantener referencias a las imágenes
temp_label.image = images["cold"]
humidity_label.image = images["cloud"]
light_label.image = images["moon"]
uv_label.image = images["low_uv"]
co2_label.image = images["green"]

# Función para actualizar los datos
def update_data():
    if arduino.in_waiting > 0:
        rawString = arduino.readline().decode('utf-8').strip()
        data = rawString.split(",")
        print(data)
        
        temp = float(data[0])
        humidity = float(data[1])
        light = int(data[2])
        uv = int(data[3])
        co2 = int(data[4])
        
        # Actualiza la etiqueta de temperatura con el emoji correspondiente
        if temp < 10:
            temp_label.config(text=f"Temp: {temp} C", image=images["cold"], compound='right')
        elif temp > 27:
            temp_label.config(text=f"Temp: {temp} C", image=images["hot"], compound='right')
        else:
            temp_label.config(text=f"Temp: {temp} C", image=images["happy"], compound='right')
        
        # Actualiza la etiqueta de humedad con el emoji correspondiente
        if humidity < 30:
            humidity_label.config(text=f"Humidity: {humidity} %", image=images["cloud"], compound='right')
        else:
            humidity_label.config(text=f"Humidity: {humidity} %", image=images["rain"], compound='right')
        
        # Actualiza la etiqueta de luz con el emoji correspondiente
        light = convert_to_percentage(light)
        if light < 20:
            light_label.config(text=f"Light Level: {light} %", image=images["moon"], compound='right')
        else:
            light_label.config(text=f"Light Level: {light} %", image=images["sun"], compound='right')
        
        # Actualiza la etiqueta de UV con el emoji correspondiente
        if uv < 50:
            uv_label.config(text=f"UV Level: {uv}", image=images["low_uv"], compound='right')
        else:
            uv_label.config(text=f"UV Level: {uv}", image=images["high_uv"], compound='right')
        
        # Actualiza la etiqueta de CO2 con el emoji correspondiente
        if co2 < 70:
            co2_label.config(text=f"CO2 Level: {co2}", image=images["green"], compound='right')
        elif co2 < 100:
            co2_label.config(text=f"CO2 Level: {co2}", image=images["yellow"], compound='right')
        else:
            co2_label.config(text=f"CO2 Level: {co2}", image=images["red"], compound='right')
    
    root.after(1000, update_data)  # Actualiza cada segundo

# Inicia la actualización de datos
update_data()

# Ejecuta la interfaz gráfica
root.mainloop()
