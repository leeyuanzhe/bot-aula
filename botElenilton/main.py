import PIL
import pyautogui
import time
chat = "imagens/chat.png";
presente = "imagens/presente.png";
sair = "imagens/sair.png"
while True:
    print("não ainda")
    if pyautogui.locateOnScreen(presente, confidence =0.8) is not None:
        print("foi")
        pyautogui.click(pyautogui.locateOnScreen(chat,confidence=0.8));pyautogui.typewrite('presente')
        pyautogui.press('enter')
        variavel = True;
        while variavel == True:
            print("finalizando em 2 minutos")
            time.sleep(10)
            pyautogui.click(pyautogui.locateOnScreen(sair, confidence =0.8))
            while variavel == true:
                print("sair")
                if pyautogui.locateOnScreen(sair,  confidence=0.7) is not None:
                 botao = pyautogui.locateOnScreen(sair, confidence=0.7);
                 print(botao)
                 pyautogui.click(botao)
                 variavel = False;
                print("achou")
            exit()


