# --------------------------------------------- STAGE 1 ---------------------------------------------
#
# lang = input("Type \"en\" if you want to translate from French into English, or "
#              "\"fr\" if you want to translate from English into French:\n")
# word = input("Type the word you want to translate:\n")
# print("You choose \"{}\" as the language to translate \"{}\" to.".format(lang, word))

# --------------------------------------------- STAGE 2 ---------------------------------------------
# import requests
# from bs4 import BeautifulSoup
#
# LANGUAGES = ['en', 'fr']
# REVERSE_CONTEXT_URL = 'https://context.reverso.net/translation/'
#
# lang = ''
# while lang not in LANGUAGES:
#     lang = input("Type \"en\" if you want to translate from French into English, or "
#                  "\"fr\" if you want to translate from English into French:\n")
# word = input("Type the word you want to translate:\n")
# print("You choose \"{}\" as the language to translate \"{}\" to.".format(lang, word))
#
# if lang == 'fr':
#     url_adr = REVERSE_CONTEXT_URL + 'english-french/' + word
# else:
#     url_adr = REVERSE_CONTEXT_URL + 'french-english/' + word
#
# # creating request
# headers = {'User-Agent': 'Chrome/100.0'}
# try:
#     r = requests.get(url_adr, headers=headers)
# except ValueError:
#     print("Invalid resource!")
#
# if r.status_code == 200:
#     print("200 OK")
#     soup = BeautifulSoup(r.content, 'html.parser')
#     translations_list = []
#     examples_list = []
#     for elem in soup.find('div', {'id': 'translations-content'}):
#         text = elem.text.strip()
#         if text:
#             translations_list.append(text)
#     for elem in soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'}):
#         text = elem.text.strip()
#         if text:
#             examples_list.append(text)
#     print("Translations")
#     print(translations_list)
#     print(examples_list)
# else:
#     print("Something went wrong")

# --------------------------------------------- STAGE 3 ---------------------------------------------
# import requests
# from bs4 import BeautifulSoup
#
# LANGUAGES = {'en': 'English', 'fr': 'French'}
#
# REVERSE_CONTEXT_URL = 'https://context.reverso.net/translation/'
#
# lang = ''
# while lang not in LANGUAGES.keys():
#     lang = input("Type \"en\" if you want to translate from French into English, or "
#                  "\"fr\" if you want to translate from English into French:\n")
# word = input("Type the word you want to translate:\n")
# print("You choose \"{}\" as the language to translate \"{}\" to.".format(lang, word))
#
# if lang == 'fr':
#     url_adr = REVERSE_CONTEXT_URL + 'english-french/' + word
# else:
#     url_adr = REVERSE_CONTEXT_URL + 'french-english/' + word
#
# # creating request
# headers = {'User-Agent': 'Chrome/100.0'}
# try:
#     r = requests.get(url_adr, headers=headers)
# except ValueError:
#     print("Invalid resource!")
#
# if r.status_code == 200:
#     print("200 OK")
#     soup = BeautifulSoup(r.content, 'html.parser')
#     translations_list = []
#     examples_list = []
#     for elem in soup.find('div', {'id': 'translations-content'}):
#         text = elem.text.strip()
#         if text:
#             translations_list.append(text)
#     for elem in soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'}):
#         text = elem.text.strip()
#         if text:
#             examples_list.append(text)
#     print(f"{LANGUAGES[lang]} Translations:")
#     print(*translations_list[:5], sep='\n')
#     print()
#     print(f"{LANGUAGES[lang]} Examples:")
#     for i, example in enumerate(examples_list[:10]):
#         print(example)
#         if i % 2 == 1:
#             print()
# else:
#     print("Something went wrong")

# --------------------------------------------- STAGE 4 ---------------------------------------------
import requests
from bs4 import BeautifulSoup

LANGUAGES = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish',
             'Portuguese', 'Romanian', 'Russian', 'Turkish']

REVERSE_CONTEXT_URL = 'https://context.reverso.net/translation/'

print("Hello, welcome to the translator. Translator supports:")
for i, lang in enumerate(LANGUAGES):
    print(f"{i + 1}. {lang}")
num = 0
while num not in range(1, 14):
    try:
        num = int(input("Type the number of your language:\n"))
    except ValueError:
        pass
first_lang = LANGUAGES[num - 1]
num = 0
while num not in range(1, 14):
    try:
        num = int(input("Type the number of language you want to translate to:\n"))
    except ValueError:
        pass
second_lang = LANGUAGES[num - 1]
word = input("Type the word you want to translate:\n")

url_adr = REVERSE_CONTEXT_URL + first_lang.lower() + '-' + second_lang.lower() + '/' + word

# creating request
headers = {'User-Agent': 'Chrome/100.0'}
try:
    r = requests.get(url_adr, headers=headers)
except ValueError:
    print("Invalid resource!")

if r.status_code == 200:
    print()
    soup = BeautifulSoup(r.content, 'html.parser')
    translations_list = []
    examples_list = []
    for elem in soup.find('div', {'id': 'translations-content'}):
        text = elem.text.strip()
        if text:
            translations_list.append(text)
    for elem in soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'}):
        text = elem.text.strip()
        if text:
            examples_list.append(text)
    print(f"{second_lang} Translations:")
    print(*translations_list[:5], sep='\n')
    print()
    print(f"{second_lang} Examples:")
    for i, example in enumerate(examples_list[:10]):
        print(example)
        if i % 2 == 1:
            print()
else:
    print("Something went wrong")