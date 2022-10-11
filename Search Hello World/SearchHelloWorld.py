import webbrowser
from time import sleep
import pyautogui as auto

url = "https://www.google.com/"


def search_HelloWorld(url):

    webbrowser.open(url)

    sleep(3)

    auto.write("Hello World")

    auto.press("enter")


search_HelloWorld(url)
