#URLS
**PERFIL por nombre (te debería detectar la región)-** lolwc.com/profile/las/sadjockerking
**PERFIL por id -** lolwc.com/profile/las/id=426174
**PERFIL profile/league/history/runes/masteries -** lolwc.com/profile/las/sadjockerking/history
este no es obligatorio, pero si se quisiese acceder directamente a una sección, poniendo la url funcionaría
**CHAT -** lolwc.com/chat/las
**CHAT por contacto (abre el chat con ese contacto) -** lolwc.com/chat/las/groll
**STATIC -** lolwc.com/static
- runes
	- todas: lolwc.com/static/runes
	- especifica: lolwc.com/static/runes=234
- items
	- todos: lolwc.com/static/items
	- especifico: lolwc.com/static/items=523
- spells: lolwc.com/static/spells
- champs
	- todos: lolwc.com/static/champs
	- especifico: lolwc.com/static/champs/riven

#NOMBRES E INFORMACIÓN POR PÁGINA
se muestran elementos que debe haber necesariamente en cada página, si es necesario algunas propiedades y descripción también

##NAV
- logo de la página
- alerta del servidor
- botón perfil
- botón chat
- botón static
- cuadro de busqueda
- combobox para seleccionar server de busqueda
- botón para buscar
- botón para loguearse

##FOOTER
- logo de riot
- informaciono de que no estamos relacionados a riot
- botones facebook-twitter-google+

##PERFIL
*summoner info*: "summonerInfo"
- (#)imagen baner del champion mas usado (id del champ): mostPlayedChampBanerImg
- imagen del summoner: summonerImg
- nombre del summoner: summonerName
- (#)imagen de la liga actual del sumoner: summonerLeagueImg
- liga actual del sumoner (ej:Silver): summonerLeague
- division actual del summoner(ej:IV): summonerDivision
- server del summoner: summonerServer
- prom kills en ranked: summonerKills
- prom deaths en ranked: summonerDeaths
- prom assists en ranked: summonerAssists
- kda: summonerKdaRatio
- porcentaje de victorias en ranked: summonerWinrate

*most played champ info*: "mostPlayedChampInfo"
- imagen (id del champ): mostPlayedChampId
- nombre: mostPlayedChampName
- cantidad de jugada: mostPlayedChampMatchesCount
- cantidad de victorias: mostPlayedChampMatchesWinCount
- cantidad de derrotas: mostPlayedChampMatchesLoseCount
- kda: mostPlayedChampKdaRatio
- prom kills: mostPlayedChampKills
- prom deaths: mostPlayedChampDeaths
- prom asssists: mostPlayedChampAssist
- prom creeps: mostPlayedChampCs
- prom gold: mostPlayedChampGold

*free week champs*: "freeWeekChamps"
lista de
- (#)imagen del champ: freeChamp1
- Ip del champ: freeChamp
- (#)link del champ en static (lolwc.com/static/champs/riven)
- (#)precio ip
- (#)precio rp


*skin sales*: "skinSales"(#)
lista de
- imagen del skin
- rp del skin
- link al champ en static

*champ sales*: "champSales"(#)
lista de
- imagen del champ
- rp del champ
- link al champ en static

*featured games*: "featuredGames"
lista de 5
- tipo de juego
- tiempo transcurrido
- (#)comando para ver el game (https://developer.riotgames.com/docs/spectating-games)
- nombre 1 azul
- (#)imagenChamp 1 azul
- nombre 2 azul
- (#)imagenChamp 2 azul
- nombre 3 azul
- (#)imagenChamp 3 azul
- nombre 4 azul
- (#)imagenChamp 4 azul
- nombre 5 azul
- (#)imagenChamp 5 azul
- nombre 1 rojo
- (#)imagenChamp 1 rojo
- nombre 2 rojo
- (#)imagenChamp 2 rojo
- nombre 3 rojo
- (#)imagenChamp 3 rojo
- nombre 4 rojo
- (#)imagenChamp 4 rojo
- nombre 5 rojo
- (#)imagenChamp 5 rojo

###profile
- (#)Icono liga individu/dobles
- nombre liga i/d: leagueSoloQName
- tier de liga i/d: leagueSoloQTier
- division liga i/d: leagueSoloQDivision
- lp i/d: leagueSoloQLp
- (#)Icono liga 5v5:
- nombre liga 5v5: leagueTeamName
- tier de liga 5v5: leagueTeamTier
- division 5v5: leagueTeamDivision
- lp 5v5: leagueTeamLp
- (#)Icono liga 3v3:
- nombre liga 3v3: league3v3Name
- tier de liga 3v3: league3v3Tier
- division 3v3: league3v3Division
- lp 3v3: league3v3Lp

###league
- (#)icono de liga: summonerLeagueTabImg
- nombre de liga: summonerLeagueTabName (montaurfs de oriana)
- rank de liga: summonerLeagueTabRank (Silver)
- division de liga: summonerLeagueTabDivision (IV)
- lista de en P: summonerLeagueTabPList
	- rank de sumoner en la liga: summonerLeagueTabPListRank
	- change (fijarse en lolking): summonerLeagueTabPListChange
	- nombre de summoner: summonerLeagueTabPListName
	- icono de summoner: summonerLeagueTabPListImg
	- isReciente: summonerLeagueTabPListIsRecent
	- isEnRacha: summonerLeagueTabPListIsOnFire
	- wins: summonerLeagueTabPListWins
	- lista de partidas para promo: summonerLeagueTabPPromo
		- Tiene una lista de largo de la cantidad de partidas que tiene que jugar, con el string "1" si la gano, "0", si la perdio, o "N" si no la jugo
- lista de el resto: summonerLeagueTabList
	- rank de sumoner en la liga: summonerLeagueTabListRank
	- change: summonerLeagueTabListChange
	- nombre de sumoner: summonerLeagueTabListName
	- icono de sumoner: summonerLeagueTabListImg
	- isRecienteenliga: summonerLeagueTabListIsRecent
	- isEnRacha: summonerLeagueTabListIsOnFire
	- wins: summonerLeagueTabListWins
	- puntos(LP): summonerLeagueTabPListLP

###history: "history"
lista de
- victoria o derrota: isWin
- id del campeón: champId
- (#)imagen del champ: champImg
- (#)link del champ:
- level del champ: champLvl
- spell1: spell1
- spell2: spell2
- (#)img spell1: spell1
- (#)link spell1
- (#)img spell2: spell2
- (#)link spell2

- tipo de juego: gameType (CUSTOM - MATCHED)
- modo de juego: gameMode (CLASSIC - ARAM)
- subtipo de juego: gameSubType (NORMAL - BOT)
- mapa: map
- duracion de partida: timePlayed
- pi ganados: piEarned
- kills: kills
- deaths: deaths
- asssists: assists
- oro: goldGained
- creeps(suma de neutralMinionsKilled + minionsKilled de la api): creepScore
- timestamp de inicio de partida: createDate
- (#)imagen item1:
- (#)link item1:
- item 1: item1
- (#)imagen item2
- (#)link item2
- item 2: item2
- (#)imagen item3
- (#)link item3
- item 3: item3
- (#)imagen item4
- (#)link item4
- item 4: item4
- (#)imagen item5
- (#)link item5
- item 5: item5
- (#)imagen item6
- (#)link item6
- item 6: item6
- (#)imagen baratija
- (#)link baratija
- baratija: item7

###runes
- numero pagina activa: activePage
- lista de paginas de runas: pages
	- lista de runas: runes
    	- nombre de pagina de runas: pageName
		- lista de las runas de la pagina
			- lista con info de la runa: rune
				- id de runa
				- posicion de runa
				- (#)imagen de runa
		    	- (#)tipo de runa
				- (#)total de stats que suma

###masteries
- numero de pagina activa
- distribucion de runa (21/9/0)
lista de
- nombre de pagina de maestrias
- lista de
	- id de maestria
	- cantidad de puntos
	- imagen de maestria

##CHAT

###estado del usuario
- id del invocador: id
- Estado de coneccion (chat, dnd (do not disturb) y away): statusChat
- Nombre de invocador: name
- numero de icono de perfil: profileIcon
- level: level
- champion Mastery Score: championMasteryScore
- (editable)mensaje de estado: statusMsg
- Nombre de la liga, Leona Urfriders, etc: rankedLeagueName
- Division de liga: rankedLeagueDivision
- Liga solo queue, BRONZE, GOLD: rankedLeagueTier

###conectados
lista de:
	-
###mensajes sin leer

#**(No tocar)Contactos**  
- friends = []  

#**(No tocar)Buzon**  
- buzon = []#Lista de mensajes sin leer  

#**(No tocar salvo statusChat)Del roster**  
- jid #Jabber ID del conectado  
- statusChat = "dnd" #chat, dnd (do not disturb) y away  
- name = "BanerSjK"#Nombre de invocador  

#**De roster.getStatus()**  
- profileIcon #Número de icono de invocado  
- level #Level  
- wins #?Victorias en general (de normal, ranked, todo?)  
- championMasteryScore #Mastery Champ Score  
- statusMsg #Mensaje de estado  
- rankedLeagueName #Nombre de la liga, Leona Urfriders, etc  
- rankedLeagueDivision #Division de la anterior I, IV, V  
- rankedLeagueTier #Liga solo queue, BRONZE, GOLD  

- skinname #si inGame, el champ jugado s
- gameQueueType #?Generalmente dice NORMAL  
- gameStatus #inGame, outOfGame, champSelect, hostingNormalGame  
