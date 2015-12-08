# lightshow

Allumer et éteindre des lumières à partir d'une détection faciale et yeux d'une caméra externe (sur un poste lointain).

Pour le bon fonctionnement, une connection "internet" est requise.

## Client Side
#### Dépendance
  * Caméra
  * Python 2.7
  * OpenCV
  
#### Fonctionnement
  Pour faire fonctionner la caméra : `python webcam.py`

  Présentement, les adresse IP vers le serveur ainsi que le port de communication sont des variables qui peuvent être adapté à tout moment.
  
  Seul les yeux ainsi que le visage peuvent être détecté, si plus, simplement ajouter l'algorithme xml nécéssaire à la détection ainsi que sa capture dans le code Python.
  
 
## Server Side
#### Dépendance
  * RaspberryPi
  * Golang (la plus récente possible! Fonctionne avec 1.5)
  * LED
  * root

#### Fonctionnement
  Avant l'utilisation du serveur lancer : `go get github.com/stianeikeland/go-rpio`
  
  Pour partir le serveur : `go run server.go`
  
  Le serveur écoute sur le port 10001, ceci peut être adapté au besoin.
  
  Pour les besoins courant, 4 variables peuvent être reçus par le serveur, sois :
  - 00 => Aucun visage a été détecté
  - 01 => Un visage a été détecté
  - 10 => Aucun yeux a été détecté
  - 11 => Deux yeux ont été détecté

  Pour l'utilisation des Pin, présentement 3 Pin peuveut être utilisé, pour obtenir les bons numéros d'utilisation de Pin, se référer à : [RaspberryPi Code](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2014/07/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated.png)
  
  
