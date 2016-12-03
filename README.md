# local_hack_day #
## This is a sample local hack day project ##

## Kratek opis ##
Aplikacija A:Attend je preprosta aplikacija za spremljanje prisotnosti študentov v predavalnici oz. učilnici. Ideja je da bi z raspberry pi kontorlerjem spremljali wi-fi omrežje in zaznali prisotnost mobilnega telefona ali računalnika študenta, tako bi beležili prisotnost le z enrkatno registracijo mac naslova naprave študenta v bazo pdoatkov. 

## težave pri izdelavi ##
Oviral nas je čas in tehnične težave z raspberry pi kontrolerjem.

## Requirements ##

* `sudo apt-get install libpq-dev`
* `sudo apt-get install postgresql`
* `sudo apt-get install python-dev`


## Setup postgresql (You must be in virtualenv) ##
* `python manage.py db init`
* `python manage.py db migrate`
