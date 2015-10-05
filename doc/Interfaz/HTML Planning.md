#URLS
**PERFIL por nombre (te debería detectar la región)-** lolwc.com/las/sadjockerking
**PERFIL por id -** lolwc.com/las/id=426174
**PERFIL profile/league/history/runes/masteries -** lolwc.com/las/sadjockerking/history
este no es obligatorio, pero si se quisiese acceder directamente a una sección, poniendo la url funcionaría
**CHAT -** lolwc.com/las/chat
**CHAT por contacto (abre el chat con ese contacto) -** lolwc.com/las/chat/groll
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
- imagen baner del champion mas usado: mostPlayedChampBannerImg
- imagen del summoner: summonerImg
- nombre del summoner: summonerName
- imagen de la liga actual del sumoner: summonerLeagueImg
- liga actual del sumoner (ej:Silver IV): summonerLeagueName
- server del summoner: summonerServer
- prom kills: summonerKills
- prom deaths: summonerDeaths
- prom assists: summonerAssist
- kda: summonerKdaRatio
- porcentaje de victorias: summonerWinrate

*most played champ info*
- imagen (icono): mostPlayedChampIconImg
- nombre: mostPlayedChampName
- cantidad de jugada: mostPlayedChampMatchesCount
- cantidad de victorias: mostPlayedChampMatchesWinCount
- cantidad de derrotas: mostPlayedChampMatchesLooseCount 
- kda: mostPlayedChampKdaRatio
- prom kills: mostPlayedChampKills
- prom deaths: mostPlayedChampDeaths
- prom asssists: mostPlayedChampAssist
- prom creeps: mostPlayedChampCs
- prom gold: mostPlayedChampGold

*free week champs*
lista de
- imagen del champ: freeChamp_1
- nombre del champ: freeChamp_name
- link del champ en static (lolwc.com/static/champs/riven)
- precio ip
- precio rp

*skin sales*
lista de
- imagen del skin
- rp del skin
- link al champ en static

*champ sales*
lista de
- imagen del champ
- rp del champ
- link al champ en static

*featured games*
lista de 5
- tipo de juego
- tiempo transcurrido
- comando para ver el game (https://developer.riotgames.com/docs/spectating-games)
- nombre 1 azul
- imagenChamp 1 azul
- nombre 2 azul
- imagenChamp 2 azul
- nombre 3 azul
- imagenChamp 3 azul
- nombre 4 azul
- imagenChamp 4 azul
- nombre 5 azul
- imagenChamp 5 azul
- nombre 1 rojo
- imagenChamp 1 rojo
- nombre 2 rojo
- imagenChamp 2 rojo
- nombre 3 rojo
- imagenChamp 3 rojo
- nombre 4 rojo
- imagenChamp 4 rojo
- nombre 5 rojo
- imagenChamp 5 rojo

###profile

###league
- icono de liga: summoner_league_img_tab
- nombre de liga: summoner_league_name (idem anterior variable)
- division de liga: summoner_league_division
- lista de en promo
	- rank de sumoner en la liga
	- change (fijarse en lolking)
	- nombre de summoner
	- icono de summoner: league_champion_img
	- isRecienteenliga
	- isEnRacha
	- wins
	- cantidad de partidas que tiene que jugar para promocionar
	- cantidad ganadas
	- cantidad perdidas
- lista de el resto
	- rank de sumoner en la liga
	- change: 
	- nombre de sumoner: league_summoner_name
	- icono de sumoner: league_champion_img
	- isRecienteenliga
	- isEnRacha
	- Wins
	- puntos(LP)

###history
lista de 
- victoria o derrota: history_win_or_def
- imagen del champ: history_champ_img
- link del champ
- level del champ: history_level_champ
- img spell1: history_spell1_img
- link spell1
- img spell2
- link spell2

- tipo de juego: history_game_type
- mapa: history_map
- duracion de partida
- pi ganados: 
- score: history_score
- oro: history_gold
- creeps: history_creeps
- fecha de partida
- imagen item1
- link item1: history_item1
- imagen item2
- link item2
- imagen item3
- link item3
- imagen item4
- link item4
- imagen item5
- link item5
- imagen item6
- link item6
- imagen baratija
- link baratija

###runes
- numero pagina activa
lista de
- nombre de pagina de runas
- lista de
	- id de runa
	- posicion de runa
	- imagen de runa
- lista de
	- tipo de runa
	- total de stats que suma

###masteries
- numero de pagina activa
- distribucion de runa (21/9/0)
lista de
- nombre de pagina de maestrias
- lista de
	- id de maestria
	- cantidad de puntos
	- imagen de maestria


