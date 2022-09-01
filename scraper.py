import keyword
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def main():
    url = "https://news.ycombinator.com/item?id=22665398"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]

    keywords = {"software engineer": 0, "UI/UX Design": 0,
                "frontend engineer": 0, "full-stack engineer": 0, }

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(" ")
        words = {word.strip(".,/:;!@") for word in words}

        for k in keywords:
            if k in words:
                keywords[k] += 1
        print(keywords)

        plt.bar(keywords.keys(), keywords.values())
        plt.xlabel("jobs")
        plt.ylabel("mentions")
        plt.show()


if __name__ == "__main__":
    main()
