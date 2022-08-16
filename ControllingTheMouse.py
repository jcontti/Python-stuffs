import pyautogui

pyautogui.size() # muestra el size del la pantalla
pyautogui.position() # nos dice las coordenadas de donde esta el mouse
pyautogui.displayMousePosition() # nos va diciendo en tiempo real donde esta parado el mouse.

pyautogui.moveTo(x=0, y=0) # muevo el mouse a las coordenadas que quiero, "0,0" sería izquierda superior
pyautogui.moveTo(20, 20, duration=1.5) # agregandole el parametro duration puedo controlar la velocidad con que se desplaza el mouse.
pyautogui.click(235, 49) # con este metodo click simulo hacer un click real con el mouse.
pyautogui.rightClick() # simulo click derecho del mouse.


