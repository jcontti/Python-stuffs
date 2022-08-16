import pyautogui

pyautogui.typewrite('texto a escribir') # escribe texto en donde este parado
pyautogui.click(100, 100, duration=3.0) ; pyautogui.typewrite("testeanding") # me paro en la coord. que quiero y escribo.
pyautogui.click(100, 100, duration=2.0) ; pyautogui.typewrite("testeanding", interval=0.2) # le agrego intervalos a la escritura para que parezca real.

pyautogui.KEYBOARD_KEYS # nos muestra los param. para poder usar teclas especiales como flechitas, ctrl, etc
pyautogui.typewrite(['winleft']) # apreta la tecla windows de la izq.
