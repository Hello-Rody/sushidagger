from PIL import Image, ImageFilter
import webbrowser
import pyautogui as pgui
from pynput import mouse
import time
import datetime
import pyocr
import re

url_easy = "http://firefoxhome.html.xdomain.jp/sushidagger/Play_easy.html"
url_normal = "http://firefoxhome.html.xdomain.jp/sushidagger/Play_normal.html"
url_hard = "http://firefoxhome.html.xdomain.jp/sushidagger/Play_hard.html"
url_pop = "http://firefoxhome.html.xdomain.jp/sushidagger/pop.html"

sushi_url = "https://sushida.net/play.html"
pop_url = "http://typingx0.net/pop/"

pyocr.tesseract.TESSERACT_CMD = r"/usr/bin/tesseract"
tools = pyocr.get_available_tools()
tool = tools[0]

count = 1

banner = """                        __    _     __
       _______  _______/ /_  (_)___/ /___ _____ _____ ____  _____
      / ___/ / / / ___/ __ \/ / __  / __ `/ __ `/ __ `/ _ \/ ___/
     (__  ) /_/ (__  ) / / / / /_/ / /_/ / /_/ / /_/ /  __/ /
    /____/\__,_/____/_/ /_/_/\__,_/\__,_/\__, /\__, /\___/_/
                                        /____//____/  """

author = """
                By: Rody (GitHub @Hello-Rody)\n"""


def binarization(img):
    new_im = img.convert('1', dither=Image.Dither.NONE)
    return new_im


def ocr(img):
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img, lang="eng", builder=builder)
    print(str(datetime.datetime.now()) + " DEBUG - get text.")
    if text.count(" ") == 2:
        new_text = re.search(r" (.+) ", text).group(1)
    elif text.count(" ") == 1:
        new_text = text
    else:
        new_text = text
    return str.lower(new_text)

# マウスイベントハンドラを定義


def on_move(x, y):
    return


def on_click(x, y, button, pressed):
    if pressed:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    return


# リスナー起動
# クリック座標を取得
def point():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

    recttop_x, recttop_y = pgui.position()
    return recttop_x, recttop_y


class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'


try:
    # レベルの選択
    print(Color.RED + banner + Color.END + author)
    while True:
        print(Color.YELLOW + "3,000 yen course : 1" + Color.END)
        print(Color.BLUE + "5,000 yen course : 2" + Color.END)
        print(Color.RED + "10,000 yen course : 3" + Color.END)
        print(Color.CYAN + "POP typing : 4" + Color.END)

        level = input("Select the level : ")
        if level == "1":
            webbrowser.open_new_tab(url_easy)
            url = sushi_url
            waittime = 2
            break
        elif level == "2":
            webbrowser.open_new_tab(url_normal)
            url = sushi_url
            waittime = 2
            break
        elif level == "3":
            webbrowser.open_new_tab(url_hard)
            url = sushi_url
            waittime = 2
            break
        elif level == "4":
            webbrowser.open_new_tab(url_pop)
            url = pop_url
            waittime = 1
            break
        else:
            print("\nPlease enter numbers 1~3")

    # 座標の取得
    print("\nClick on the " + Color.RED +
          "red dot" + Color.END)
    x1, y1 = point()
    print("Click on the " + Color.BLUE +
          "blue dot" + Color.END)
    x2, y2 = point()

    # 座標の設定
    region = (x1, y1, x2 - x1, y2 - y1)

    print("\nSet the screen just before starting.\nDo not register for the ranking.")
    webbrowser.open_new_tab(url)
    print("As soon as you start, focus on the browser.")
    reply = input("Are you ready? [Y/n]:")

    if reply == "Y" or reply == "y" or reply == "Yes" or reply == "yes":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        pgui.press("space")
        time.sleep(waittime)
        while True:
            im = pgui.screenshot(region=region)
            print(str(datetime.datetime.now()) +
                  " INFO - captured screenshot.")
            new_im = binarization(im)
            text = ocr(new_im)
            if len(text) == 0 or text == "ushida.net":
                print("Bye")
                break
            pgui.write(text)
            print(str(datetime.datetime.now()) + " INFO - " +
                  str(count)+" - input - " + text)
            count += 1
    else:
        print("Bye")

except KeyboardInterrupt:
    print('\nBye')
