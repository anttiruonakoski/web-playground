#!/usr/bin/python3

from flask import Flask, render_template, request
import random
from utils import read_content

app = Flask(__name__)

template_filename = 'lomake_2.html'

storyfiles = {
    'Ilmastonmuutos': 'ilmasto.txt',
    'Töfö-pasta': 'pasta.txt'
}

dirs = {
    'imgdir': 'static/img/',
    'styledir': 'static/css/'
}

possible_adjectives = ['cooli', 'epäcooli', 'tyhjä', 'pörröinen', 'höpö', 'suurenmoinen', 'vituttava', 'vihreä', 'neliömäinen', 'pyöreä', 'juustomainen', 'kukkainen', 'koiramainen', 'iso', 'kaunis', 'upee', 'harmaa', 'pimeä', 'rasistinen']

stories = read_content(storyfiles)


def roll_article(s):
    o = random.choice(list(s.keys()))
    return o


def roll_adjective(possible_adjectives=possible_adjectives):
    a = random.choice(possible_adjectives)
    return a


def handle_post(data):
    a = []
    print(data)
    for i in range(1, 4):
        if data['adjective_'+str(i)]:
            a.append(data['adjective_'+str(i)])
        else:
            a.append(roll_adjective(possible_adjectives))
    title = data['content']
    return a, title


@app.route('/', methods=['GET', 'POST'])
def funny_page(sisalto={}):
    if request.method == 'POST':
        adjektiivit, otsikko = handle_post(request.form)
        sisalto['otsikko'] = otsikko
        sisalto['tarina'] = stories[otsikko]
    else:
        adjektiivit = [roll_adjective(possible_adjectives) for a in range(1, 4)]
        otsikko = roll_article(stories)
        sisalto['otsikko'] = otsikko
        sisalto['tarina'] = stories[otsikko]
    return render_template(
        template_filename,
        adjektiivit=adjektiivit,
        sisalto=sisalto,
        otsikot=list(stories.keys()),
        dirs=dirs)


if __name__ == '__main__':
    stories = read_content(storyfiles)
    app.run()
