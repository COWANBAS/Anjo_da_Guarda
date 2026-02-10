import psutil
import time
from PIL import ImageGrab
from pynput.keyboard import Controller, Key
from threading import Thread

Cor = (210, 106, 106)
Local = (193, 7, 143, 6)

keyboard_controller = Controller()

def is_tibia_running():
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] and process.info['name'].lower() == 'client':
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def press_shift_2():
    keyboard_controller.press(Key.shift)
    keyboard_controller.press('2')
    keyboard_controller.release('2')
    keyboard_controller.release(Key.shift)

def cor_detectada():
    x0, y0, largura, altura = Local
    screenshot = ImageGrab.grab(bbox=(x0, y0, x0 + largura, y0 + altura))
    pixels = screenshot.load()

    for x in range(0, largura, 10): 
        for y in range(0, altura, 10):
            r, g, b = pixels[x, y]
            if (r, g, b) == Cor:
                return True
    return False

def monitorar_cor():
    tibia_aberto = False
    cor_detectada_ultima_vez = False
    intervalo_verificacao = 0.1 

    while True:
        if is_tibia_running():
            if not tibia_aberto:
                tibia_aberto = True
            if cor_detectada():
                if not cor_detectada_ultima_vez:
                    press_shift_2()
                    cor_detectada_ultima_vez = True
            else:
                cor_detectada_ultima_vez = False
        else:
            if tibia_aberto:
                tibia_aberto = False

        time.sleep(intervalo_verificacao)

def main():
    thread_cor = Thread(target=monitorar_cor, daemon=True)
    thread_cor.start()

    while True:
        time.sleep(1) 

if __name__ == "__main__":
    main()
