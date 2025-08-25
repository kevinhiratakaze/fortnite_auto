import pyautogui
import time

intervalo_click = 180
intervalo_tecla = 30
duracao_press = 10

print("iniciando Auto Click. Pressione crtl+c para parar o código")

try:
    tempo_click = time.time()
    tempo_tecla = time.time()
 
 
    while True:
        agora = time.time()
            
        
        if agora - tempo_click >= intervalo_click:
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            print(f"Clique realizado em ({x}, {y})")
            tempo_click = agora
 
        if agora - tempo_tecla >= intervalo_tecla:
            pyautogui.keyDown("space")
            print("Tecla 'espaço' pressionada")
            time.sleep(duracao_press)
            pyautogui.keyUp('space')
            tempo_tecla = agora + duracao_press

        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrompido")
