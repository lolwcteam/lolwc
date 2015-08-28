#LoLWC Team

##Guía Para Realizar Cambios a LoLWC


-----------------------------------------

#Por Terminal

####Primera vez
Esto va a descargar el repositorio en una carpeta con el mismo nombre

	git clone https://github.com/lolwcteam/lolwc

Esto va a configurar su mail y nombre de usuario para que cuando hagan el comando *commit* no les de error
	
	git config --global user.email "ACA VA TU EMAIL ENTRE COMILLAS"
	git config --global user.name "ACA VA TU USUARIO ENTRE COMILLAS"

Y si también lo desean para que no pida a cada rato usuario y contraseña cuando hagan un push puede hacer estos dos comandos y ponerle un timeout de por cuanto tiempo quieren que recuerde git su contraseña (*en segundos*)

	git config --global credential.helper cache
	git config --global credential.helper 'cache --timeout="CANTIDAD DE SEGUNDOS SIN COMILLAS"'

####(*Siempre*) Antes de comenzar a trabajar
Esto va a descargar todos los cambios que haya en el repositiorio original. Si hay alguna incompatibilidad va a saltar un error diciendo en que archivo, y en ese archivo se agregarán líneas que mostrarán las diferencias entre un archivo y otro.
 
	git pull -u origin master

####(*Siempre*) Luego de modificar lo deseado
El primer comando revisará todos los archivos modificados/agregados/borrados del repositiorio local (la carpeta), el segundo planteará el commit que debe realizarse con el mensaje correspondiente, y el tercero comenzará a subir a github.

	git add --all
	git commit -m "ACA VA EL MENSAJE DEL COMMIT"
	git push -u origin master

Luego de ese comando se te solicitará el usuario de github, y la contraseña del mismo. Si hay algún conflicto github te avisará y no dejará subir el commit, para solucionarlo deberás mover tus archivos modificados en algún lado, y borrarlos de la carpeta y luego hacer otra vez el comando *"git pull -u origin master"* para recargar los cambios que alguién hizo mientras trabajabas. y deberás modificar manualmente los archivos para que no tengan conflictos.

####Cosas opcionales

- Cabe aclarar que luego de *"git add ."* también pueden introducir el siguiente comando para corroborar que estén haciendo bien los cambios:

		git status

- También si uno ya hizo al menos una vez un pull y un push puede reemplazar esos comandos directamente por 	

		git pull
		git push

- Si uno está modificando archivos o agregando solamente, y no borrando ninguno puede utilizar este comando, el cual no borrará ningún archivo solo modificará los existente y agregará nuevos.

		git add .



-----------------------------------------




#Por Brackets

####Primera Vez

- Ir al botón de extensiones y buscar una de nombre *Brackets Git* de Martin Zagora, presionar instalar.
- Nos vamos a la carpeta donde queramos clonar el repositorio (Tocamos a la izquierda en el combobox y damos en *Abrir Carpeta*)
- Si no está ya abierto el panel de git debajo lo abrimos mediante presionar en la toolbar de la izquierda el botón que tiene forma de flechas
- Damos en ese panel al botón que dice *Clone* y ponemos la URL del proyecto en el diálogo (*https://github.com/lolwcteam/lolwc*)
- Una vez que termine (*Quizás haya que tocar Enter*) tendremos todo el repositorio clonado a nuestra carpeta

####(*Siempre*) Antes de comenzar a trabajar

- Tocar el botón del libro y flecha de costado (*Git Pull*) para descargar todos los cambios del repositorio y poner si hace falta usuario y contraseña de github y recordar si se quiere

####(*Siempre*) Luego de modificar lo deseado

- Aparecerá una lista en el cuadro de git con todos los archivos modificados y en que se modificaron
- Seleccionamos todos los archivos que deseemos enviar en el commit (*Tocar el tick de arriba para seleccionar todos*)
- Presionamos el botón *Commit* e ingresamos el mensaje del commit y damos ok, eso guardará el commit para poder luego pushearlo
- Nos vamos al botón del cuadro de git a la derecha conforma de libro y una flecha en su dirección que dice *Git Push* y que debería tener un número entre paréntesis y nos pedirá nombre de usuario y contraseña.
