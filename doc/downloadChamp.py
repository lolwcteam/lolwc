#http://www.lolking.net/shared/images/champion_headers/157_0.jpg
#for i in range(len(file.readlines())):
#curl -s -o /dev/null -w "%{http_code}" http://www.lolking.net/red/images/champion_headers/157_0.jpg
from subprocess import PIPE, Popen
import os

def cmdline(command):
	#ejecuta un comando y guarda su output a una variable
	process = Popen(args=command, stdout=PIPE, shell=True)
	return process.communicate()[0]

res = ""
file = open("champs.txt","r")
for i in file.readlines():
	lista = i.rstrip('\n').split("-")
	champ = lista[0]
	name = lista[1]
	
	#aplico camel case
	if name[0].isupper():
		nameAux = list(name)
		nameAux[0] = nameAux[0].lower()
		name = ""
		for i in nameAux:
			name+=i

	#reviso que la imagen exista
	for skin in range(10):
		link = "http://www.lolking.net/shared/images/champion_headers/"+champ+"_"+str(skin)+".jpg" 
		print("curl -s -o /dev/null -w \"%{http_code}\" " + link)
		curl = cmdline("curl -s -o /dev/null -w \"%{http_code}\" " + link)
		#si la imagen existe la descarga con el nombre adecuado
		if curl == "200":
			wget = "wget -O ba_" + name + str(skin) + ".jpg " + link
			print(wget)			
			os.system(wget)
			res += wget+"\n"

file.close()
print("\n#---URLS DE IMAGENES OBTENIDAS---#\n"+res)
