
from pytube import *
from pick import pick
from webbrowser import open
import platform
import os
import colorama


try:
    os.system('pip install -r requirements.txt')
    Ti = 'Download File is YouTube'
    li = ['Download File', 'Help', 'Exit']

    li, ind = pick(li, Ti)

    def run():
        open('https://youtube.com/c/securitycom')
        open('https://aparat.com/securitycom')
        try:
            text = colorama.Fore.CYAN+'--YouTube Downloader--'
            print(text)

            user = input(colorama.Fore.MAGENTA +
                         'Enter the Url >  '+colorama.Fore.YELLOW)
            print(colorama.Back.WHITE+colorama.Fore.BLUE +
                  'Downloading the video, please wait. . .'+colorama.Back.RESET)
            Yt = YouTube(user)

            Yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download()
            print(colorama.Back.WHITE+colorama.Fore.RED +
                  'The download is complete!'+colorama.Back.RESET)
        except:
            print(colorama.Back.WHITE+colorama.Fore.BLACK +
                  'Eroor'+colorama.Back.RESET)

    if ind == 0:
        if platform.uname()[0] == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        run()
    elif ind == 1:
        if platform.uname()[0] == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        print(colorama.Fore.MAGENTA+'''Hello, friends, this tool is written in Python language,
    and keep in mind that the downloaded files are downloaded with the best quality and saved in the main folder of the tool.Programmer: Kamiyar''')

    else:
        quit()
except:
    exit
