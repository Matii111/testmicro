# Funcionamiento de la pagina
## Backend
La pagina levanta el servidor de manera local con express, de la misma manera con el frontend.

El servidor al estar ejecutado de manera local genera conflictos con CORS al realizar peticiones locales por lo que como middleware se utiliza un proxy que omite estos requisitos. Este middleware deberia ser removido en produccion.

La pagina es ejecutada de manera local y redireccionada con nginx para su acceso publico, posteriormente se utiliza ngrok para su acceso externo.
## Frontend
Este frontend esta construido en HTML sin frameworks por temas de rendimiento y ahorro de memoria.

## Ejecucion 
### JSON location
```
cd /frontend/jsonFiles
python -m http.server 3000
```
### Backend - Static Frontend
```
cd /background/src
npm run start
```
# Funcionalidades
- Puede recibir valores en formato JSON desde un archivo desde misma ip local con distinto puerto.
- Dichos valores se almacenan cada 10 segundos de manera local y cada 1 hora se envian a la base de datos.
- Son almacenados en la base de datos en formato JSON.

# TODO
- ~~Al recibir los datos con el backend crear script para enviarlos cada 24 horas a alguna base de datos o metodo de respaldo.~~
- ~~Separar datos recibidos para dos interfaces distintas, separando por arduinos 1 y 2.~~
- ~~Script que lea los datos cada 10 segundos.~~
- Mejorar la interfaz visual (frontend).
- Crear llamada para pedir los valores guardados en backend y funcion para ejecutarlo con un boton.
