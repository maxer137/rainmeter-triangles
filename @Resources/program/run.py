import os
import urllib
import cStringIO
from PIL import Image
import datetime
from colorama import Fore, Back, Style

def getID(filename, platform):
    link = "https://api.icons8.com/api/iconsets/search?term="+filename+"&amount=&offset=&platform=" + platform
    f = urllib.urlopen(link)
    data = f.read()
    linkIndex = data.find('<icon id="')
    if linkIndex is not -1:
        data = data.replace(data[:linkIndex + 10], '')
        # if platform is "ios7":
        #     data = data.split('" name="', 1)[1]
        #     data = data.split('" platform=', 1)
        #     data[0] += " Filled"
        data = data.split('" name="', 1)[0]
        return data
    else:
        return ""


def getIcons(IconIndex):
    url = "https://api.icons8.com/api/iconsets/download?id="+IconIndex+"&format=png&size=24&color=ffffff&filename=test"
    content = cStringIO.StringIO(urllib.urlopen(url).read())
    img = Image.open(content)
    size = 24,24
    img.thumbnail(size, Image.ANTIALIAS)
    return img


def customPrint(message):
    print Fore.YELLOW + datetime.datetime.now().strftime('[%H:%M:%S]') + Style.RESET_ALL + " " + message + Style.RESET_ALL


with open('template-up.txt', 'r') as f:
    templateUp = f.read()

with open('template-down.txt', 'r') as f:
    templateDown = f.read()

with open('wallpaper.txt', 'r') as f:
    wallpaper = f.read()

for filename in os.listdir('../icons'):
    customPrint(Fore.CYAN + "creating files for " + filename)
    filename = filename.replace('.png', '')
    content1 = templateUp.replace('Application', filename)
    content2 = templateDown.replace('Application', filename)
    content3 = wallpaper.replace('Application', filename)

    if os.path.exists('../../icons/' + filename) is not True:
        os.makedirs('../../icons/' + filename)
        with open('../../icons/' + filename + '/' + filename + '-up.ini', "w+") as f:
            f.write(content1)
        with open('../../icons/' + filename + '/' + filename + '-down.ini', "w+") as f:
            f.write(content2)
        with open('../../wallpapers/' + filename + '.ini', "w+") as f:
            f.write(content3)
        customPrint(Fore.GREEN + 'saved as: icons/' + filename + '/' + filename + '.ini')
    else:
        customPrint(Fore.RED + ".ini file for " + filename + " already exists")
    print("")
