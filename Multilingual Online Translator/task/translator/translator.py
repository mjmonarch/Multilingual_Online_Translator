# --------------------------------------------- STAGE 1 ---------------------------------------------
#
# lang = input("Type \"en\" if you want to translate from French into English, or "
#              "\"fr\" if you want to translate from English into French:\n")
# word = input("Type the word you want to translate:\n")
# print("You choose \"{}\" as the language to translate \"{}\" to.".format(lang, word))

# --------------------------------------------- STAGE 2 ---------------------------------------------
import requests
from bs4 import BeautifulSoup

LANGUAGES = ['en', 'fr']
REVERSE_CONTEXT_URL = 'https://context.reverso.net/translation/'

lang = ''
while lang not in LANGUAGES:
    lang = input("Type \"en\" if you want to translate from French into English, or "
                 "\"fr\" if you want to translate from English into French:\n")
word = input("Type the word you want to translate:\n")
print("You choose \"{}\" as the language to translate \"{}\" to.".format(lang, word))

if lang == 'fr':
    url_adr = REVERSE_CONTEXT_URL + 'english-french/' + word
else:
    url_adr = REVERSE_CONTEXT_URL + 'french-english/' + word

# creating request
headers = {'User-Agent': 'Chrome/100.0'}
try:
    r = requests.get(url_adr, headers=headers)
except ValueError:
    print("Invalid resource!")

if r.status_code == 200:
    print("200 OK")
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
    print("Translations")
    print(translations_list)
    print(examples_list)
else:
    print("Something went wrong")