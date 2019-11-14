import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def get_image(name):
    url = "https://bulbapedia.bulbagarden.net/wiki/" + name + "_(Pok%C3%A9mon)"
    print("Going to : " + str(url))
    html = requests.get(url)
    soup = BeautifulSoup(html.text, features="lxml")
    imgs = soup.find_all('meta', attrs={"property": "og:image"})
    if len(imgs) != 0:
        print("Found image")
        response = requests.get(imgs[0]['content'])
        img = Image.open(BytesIO(response.content))
        return img
    else:
        print("Doesn't exist in site.")
        return None


def merge(img1, name1, img2, name2, winner):
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(img1)
    ax[0].set_title(name1)
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    ax[1].imshow(img2)
    ax[1].set_title(name2)
    plt.suptitle("Winner is : "+str(winner))
    plt.savefig("Battle.png")
    plt.show()



def show(name1, name2, winner):
    img1 = get_image(name1)
    img2 = get_image(name2)
    if img1 == None or img2 == None:
        print("No image available.")
    else:
        merge(img1, name1, img2, name2, winner)


if __name__ == "__main__":
    name1 = input("Name 1st Pokemon : ")
    name2 = input("Name 2nd Pokemon : ")
    show(name1, name2, name1)
