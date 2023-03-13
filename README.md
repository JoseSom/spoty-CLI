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

# Client Credentials Flow
Las credenciales se ocuparan de la siguiente manera:

1. Al app solicita un token de acceso mandando 3 cosas: 
   1. client id
   2. client secret
   3. grant_type
2. El servicio de cuentas de spotify regresa el token de acceso con una expiracion
3. Con el token de acceso podemos enviar solicitudes a la API de Spotify 
4. La API nos regresa un objeto en formato JSON

### Request Authorization
1. Se envia una peticion **_POST_** a
```
    url: 'https://accounts.spotify.com/api/token'
```
2. Con los siguientes **_headers_**
```
    Authorization: Basic <base64 encoded client_id:client_secret>
    Content-Type:  application/x-www-form-urlencoded
```
3. Y con el siguiente body
```
    grant_type: 'client_credentials'
```

