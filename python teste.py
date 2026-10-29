import pyautogui 
import time 

pyautogui.PAUSE =1
# pyautogui.press() -> apertar 1 tecla
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.hotkey("command", "space") -> atalho de teclado

# abriria o meu navegador (Chrome)
pyautogui.press("Win")

time.sleep(2)

pyautogui.write("Chrome")
time.sleep(2)

pyautogui.press("enter")

time.sleep(2)

# entrar no site (hashtagtreinamentos.com/curso-python)
pyautogui.write("hashtagtreinamentos.com/curso-python")

time.sleep(2)

pyautogui.press("enter")
 
time.sleep(3)


# preencher o formulários
pyautogui.click(x=1186,y=161)
time.sleep(2)

pyautogui.click(x=779, y=679)
time.sleep(3)

pyautogui.click(x=724, y=682)
time.sleep(2)
pyautogui.click(x=646, y=320)
time.sleep(2)
pyautogui.write("Pedro")
time.sleep(2)

pyautogui.press("tab")
pyautogui.write("Dasilvapedrohenrique748@gmail.com")
pyautogui.press("tab")
pyautogui.write("11954931786")
pyautogui.press("tab")
pyautogui.press("enter")


# enviar o formulário

