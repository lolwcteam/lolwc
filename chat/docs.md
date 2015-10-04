Modulo Python LoL Chat  
--
by Mateo de Mayo

La forma de utilizar el chat es la siguiente
- Instalar las dependencias necesarias con pip

    sudo pip install xmltodict
    sudo pip install git+https://github.com/ArchipelProject/xmpppy

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
- server = None#servidor  
- user = None#usuario  
- password = None#contraseña  
- connected = None#True si esta conectado  
 -connection = None#El objeto xmpp de coneccion  
 -roster = None#La lista de contactos  

#**(No tocar)Contactos**  
- friends = []  

#**(No tocar)Buzon**  
- buzon = []#Lista de mensajes sin leer  

#**(No tocar salvo statusChat)Del roster**  
- jid = None #Jabber ID del conectado  
- statusChat = "dnd" #chat, dnd (do not disturb) y away  
- name = "BanerSjK"#Nombre de invocador  

#**De roster.getStatus()**  
- profileIcon = None#Número de icono de invocado  
- level = None #Level  
- wins = None #?Victorias en general (de normal, ranked, todo?)  
- leaves = None #Cantidad de abandonos  
- odinWins = None #?Cantidad de victorias en Odin? 3v3?  
- odinLeaves = None #?Cantidad de abandonos en Odin  
- queueType= None #?INDEFINIDO siempre da None  
- rankedLosses = None #?INDEFINIDO siempre da 0  
- rankedRating = None #?INDEFINIDO siempre da 0  
- tier = None #?Alguna liga quizás la del elo más alto (DIAMOND, BRONZE, etc)  
- rankedSoloRestricted = None #?INDEFINIDO generalmente false  
- championMasteryScore = None #Mastery Champ Score  
- statusMsg = None #Mensaje de estado  
- rankedLeagueName = None #Nombre de la liga, Leona Urfriders, etc  
- rankedLeagueDivision = None #Division de la anterior I, IV, V  
- rankedLeagueTier = None #Liga solo queue, BRONZE, GOLD  
- rankedLeagueQueue = None #? suele decir RANKED_SOLO_5x5  
- rankedWins = None #Victorias en ranked  
- skinname = None #si inGame, el champ jugado  
- gameQueueType = None #?Generalmente dice NORMAL  
- gameStatus = None #inGame, outOfGame, champSelect, hostingNormalGame  
- timeStamp = None #?si inGame, timestamp de cuando empezo, si no INDEFINIDO  

Saber si hay mensajes nuevos
--

Para eso hay que chequear constantemente la variable buzon, que es una lista organizada de la siguiente forma

    buzon = [
            ("Nombre del Emisor1","Mensaje del emisor1"),
            ("Nombre del Emisor2","Mensaje del emisor2"),
            ]

buzon[0]: Mensaje más antiguo no leído  
buzon[0][0]: Emisor del mensaje más antiguo no leído  
buzon[0][1]: Mensaje del mensaje más antiguo no leído

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
