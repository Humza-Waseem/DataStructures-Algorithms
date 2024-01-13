import Web_Scraping
import threading
flag = threading.Event()
pause_flag = False


def resume():
    global flag, pause_flag
    start = Web_Scraping.get_start_index()
    pause_flag = False
    for x in range(start, 32185):
        if not pause_flag:
            Web_Scraping.web_scraping(x)
        else:
            flag.set()
            break


def pause():
    global flag, pause_flag
    pause_flag = True
    flag.set()


