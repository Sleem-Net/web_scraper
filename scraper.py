import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=32655533"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="comment-tree")

    print(f"Elements: {len(elements)}")





    







if __name__ == "__main__":
    main()
    