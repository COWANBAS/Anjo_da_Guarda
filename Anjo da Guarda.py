import psutil
import time
import keyboard
import pyautogui

Cor = (255, 0, 0)  
Local = (100, 100)        

def is_tibia_running():
    return any(
        process.info['name']
        and process.info['name'].lower() == 'client'  # Mude o nome para "client.exe" se pretende usar no Windows.
        for process in psutil.process_iter(['name'])
    )

# Batendo Utamo Vita
def press_shift_2():
    keyboard.press('shift')
    keyboard.press_and_release('2')
    keyboard.release('shift')

def cor_detectada():
    pixel = pyautogui.screenshot().getpixel(Local)
    return pixel == Cor

def main():
    tibia_aberto = False

    while True:
        if is_tibia_running():
            if not tibia_aberto:
                tibia_aberto = True

            if cor_detectada():
                press_shift_2()
        else:
            if tibia_aberto:
                tibia_aberto = False

        time.sleep(0.1)  

if __name__ == "__main__":
    main()
