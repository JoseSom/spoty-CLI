# Reto

Desarrolla un programa en Python que, utilizando la **API** de Spotify, busque y muestre las 10 
canciones más populares de un artista específico. El programa debe solicitar al usuario el nombre 
del artista y mostrar en la consola el título de las canciones y su popularidad en Spotify (_medida en 
una escala de 0 a 100_).

Después de mostrar las canciones más populares del artista, se debe pedir al usuario que 
seleccione una de las canciones mostradas e ingresar un número del 1 al 10. El programa debe 
guardar la información de la canción seleccionada en una lista o diccionario y mostrarla en la 
consola. Luego, el programa debe permitir al usuario seleccionar otra canción, la cual se agrega a 
la lista o diccionario junto con la anterior.

Una vez que el usuario haya seleccionado al menos dos canciones, el programa debe calcular y 
mostrar la duración total de la lista de reproducción.

# Variables de entorno

Se agregan las variables de entorno en un archivo .env el cual es ignorado por git cuando se agrega a su archivo _**.gitignore**_ por temas de seguridad . Para el funcionamiento tienen que agregarse estas dos variables:
```
CLIENT_ID="Tu client id"
CLIENT_SECRET="Tu client secret"
```
Los valores de estas variables se obtienen de tu **_dashboard_** en spotify: https://developer.spotify.com/


Para la lectura de estas variables se importa la libreria de _python-dotenv_ la cual se instala con:
```
pip install python-dotenv
```

En caso de no funcionar puedes ocupar:
```
python -m pip install python-dotenv

python3 -m pip install nv
```

Para hacer request ocuparemos **_Requests_** siendo esta una libreria HTTP
```
pip install requests
```

