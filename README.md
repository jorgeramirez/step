# step

Simple demo using Pocketsphinx and GStreamer

<p style="text-align: center;">
  <img src="https://raw.github.com/jorgeramirez/step/master/screenshot.png" style="width: 400px;" />
</p>

*step* recognizes five basic commands in spanish:

* ADELANTE
* ATRAS
* ABAJO
* ARRIBA
* PASO (UNO | DOS ... | DIEZ)

and based on the recognized command it updates the state of the board.

## Run the demo

There are two front-ends: `main.py` is a CLI-based program
and `main_gui.py` is a [pygame](http://www.pygame.org/) 
powered app. You can run this demo by issuing `python main.py`
or `python main_gui.py`.