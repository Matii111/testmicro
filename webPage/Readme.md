# Funcionamiento de la pagina
## Backend
La pagina levanta el servidor de manera local con express, de la misma manera con el frontend.

El servidor al estar ejecutado de manera local genera conflictos con CORS al realizar peticiones locales por lo que como middleware se utiliza un proxy que omite estos requisitos. Este middleware deberia ser removido en produccion.

La pagina es ejecutada de manera local y redireccionada con nginx para su acceso publico, posteriormente se utiliza ngrok para su acceso externo.
## Frontend
Este frontend esta construido en HTML sin frameworks por temas de rendimiento y ahorro de memoria.
# TODO
- Al recibir los datos con el backend crear script para enviarlos cada 24 horas a alguna base de datos o metodo de respaldo.
- Mejorar la interfaz visual (frontend).
- Separar datos recibidos para dos interfaces distintas, separando por arduinos 1 y 2.
- Script que lea los datos cada 10 segundos.