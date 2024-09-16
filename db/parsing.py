
from fake_useragent import UserAgent


import requests
from bs4 import BeautifulSoup



user_agent = UserAgent()
headers = {
    "Accept": "*/*",
    "User-Agent": user_agent.random  # Call the method to get a random user agent
}



def questions1():
    url1 = "https://lifehacker.ru/kak-razgovorit-cheloveka/"
    req = requests.get(url1, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    questions = soup.find_all("li")
    with open("test.txt", "a") as file:
        for i in questions:
            file.write(i.text + "\n")
            print(f"Добавлен вопрос {i.text}")

def questions2():
    url1 = 'https://femmie.ru/40-voprosov-kotory-e-sleduet-zadat-chtoby-horosho-uznat-cheloveka-65552/'
    req = requests.get(url1, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    questions = soup.find_all("li")
    with open("test.txt", "a") as file:
        for i in questions[2:-6]:
            file.write(i.text + "\n")
            print(f"Добавлен вопрос {i.text}")


def questions3():
    url1 = 'https://www.thevoicemag.ru/lifestyle/stil-zhizni/100-voprosov-dlya-druzei-o-chem-sprashivat-chtoby-luchshe-uznat-drug-druga/'
    req = requests.get(url1, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    questions = soup.find_all("li")
    with open("test.txt", "a") as file:
        for i in questions[4:]:
            file.write(i.text + "\n")
            print(f"Добавлен вопрос {i.text}")


def main_db_questions_create():
    questions1()
    questions2()
    questions3()
main_db_questions_create()