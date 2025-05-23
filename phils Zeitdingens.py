import time
import winsound
import threading

intervall = 300  # Sekunden
stop_flag = False


def ton_abspielen():
    while not stop_flag:
        winsound.Beep(400, 675)
        winsound.Beep(375, 675)
        time.sleep(intervall)


def stop_abfragen():
    global stop_flag
    while True:
        if input('Gib "STOP" ein, um zu beenden: ').strip().upper() == "STOP":
            stop_flag = True
            break


ton_thread = threading.Thread(target=ton_abspielen)
ton_thread.start()

stop_abfragen()

print("Programm beendet.")
