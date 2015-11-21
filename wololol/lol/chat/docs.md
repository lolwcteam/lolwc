Modulo Python LoL Chat  
--
by Mateo de Mayo

La forma de utilizar el chat es la siguiente
- (DEPRECATED)Instalar las dependencias necesarias con pip  

        - $ sudo pip install xmltodict 
        $ sudo pip install git+https://github.com/ArchipelProject/xmpppy  
- Colocar la librería xmpp modificada en la carpeta a usar
aspectos modificados:
	auth.py, clase Bind, metodo Bind, luego del segundo "if isResultNode(resp):" se agregó esta linea
		self._owner.Summoner = resp.getTag("session").getTagData("summoner_name")#Agregada
- Colocar los archivos Cliente.py y Friend.py en la carpeta a utilizar


    import Cliente
    cliente = Cliente.Cliente("usuario", "contraseña", "las")

- Una vez hecho esto ya tenemos nuestro objeto de cliente funcionando que ya tendrá toda la lista de amigos conectados, con su información y demás


Modificar el estado del cliente
--
Tan simple como

    cliente.propiedad = "nuevo valor"
Está es una lista de las propiedades posibles y sus descripciones (Todas son de tipo str)

#**Generales**  
- server#servidor  
- user#usuario  
- password#contraseña  
- connected#True si esta conectado  
 -connection#El objeto xmpp de coneccion  
 -roster#La lista de contactos  

#**(No tocar)Contactos**  
- friends = []  

#**(No tocar)Buzon**  
- buzon = []#Lista de mensajes sin leer  

#**(No tocar salvo statusChat)Del roster**  
- jid #Jabber ID del conectado  
- statusChat = "dnd" #chat, dnd (do not disturb) y away  
- name = "BanerSjK"#Nombre de invocador  

#**De roster.getStatus()**  
- profileIcon#Número de icono de invocado  
- level #Level  
- wins #?Victorias en general (de normal, ranked, todo?)  
- leaves #Cantidad de abandonos  
- odinWins #?Cantidad de victorias en Odin? 3v3?  
- odinLeaves #?Cantidad de abandonos en Odin  
- queueType= None #?INDEFINIDO siempre da None  
- rankedLosses #?INDEFINIDO siempre da 0  
- rankedRating #?INDEFINIDO siempre da 0  
- tier #?Alguna liga quizás la del elo más alto (DIAMOND, BRONZE, etc)  
- rankedSoloRestricted #?INDEFINIDO generalmente false  
- championMasteryScore #Mastery Champ Score  
- statusMsg #Mensaje de estado  
- rankedLeagueName #Nombre de la liga, Leona Urfriders, etc  
- rankedLeagueDivision #Division de la anterior I, IV, V  
- rankedLeagueTier #Liga solo queue, BRONZE, GOLD  
- rankedLeagueQueue #? suele decir RANKED_SOLO_5x5  
- rankedWins #Victorias en ranked  
- skinname #si inGame, el champ jugado  
- gameQueueType #?Generalmente dice NORMAL  
- gameStatus #inGame, outOfGame, champSelect, hostingNormalGame  
- timeStamp #?si inGame, timestamp de cuando empezo, si no INDEFINIDO  

Obtener información de contactos
--

    cliente.friends

Es la lista que tiene a todos los objetos de tipo amigo, dentro de cada uno encontramos las mismas propiedades que en el roster.getStatus() del cliente, para llamar a alguna por ejemplo:

    cliente.friends[2].statusMsg

Saber si hay mensajes nuevos
--

Para eso hay que chequear constantemente la variable buzon, que es una lista organizada de la siguiente forma

    buzon = [
            ("Nombre del Emisor1","Mensaje del emisor1"),
            ("Nombre del Emisor2","Mensaje del emisor2"),
            ]

buzon[0]: Mensaje más antiguo no leído  
buzon[0][0]: Emisor del mensaje más antiguo no leído  
buzon[0][1]: Texto del mensaje más antiguo no leído

Lo que hay que hacer una vez que se comprueban los mensajes y se hace lo que se quiere con ellos es limpiar el buzon con
**cliente.cleanBuzon()**

Enviar un mensaje
--
    cliente.send("42651", "Hola como andas?")

- **send(to, msg)**

    Envía un mensaje a un usuario **conectado**
    - to - str - ID del usuario a enviar
    - msg - str - Mensaje a enviar
    - return:
        - True - si el contacto está conectado
        - False - si no lo está
