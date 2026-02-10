import psutil
import time
import keyboard  

def is_tibia_running():
    return any(
        process.info['name']
        and process.info['name'].lower() == 'client' # Mude o nome para "client.exe" se pretende usar no Windows.
        for process in psutil.process_iter(['name']))
        
def press_shift_at():

# Batendo Utamo Vita
    keyboard.press('shift')
    keyboard.press_and_release('@')
    keyboard.release('shift')

def main():
    tibia_aberto = False

    while True:
        if is_tibia_running():
            if not tibia_aberto:
                tibia_aberto = True
        else:
            if tibia_aberto:
                tibia_aberto = False

        time.sleep(1)

if __name__ == "__main__":
    main()
