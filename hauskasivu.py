#!/usr/bin/python3

from flask import Flask, render_template, request
import random

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


def read_content(storyfiles):
    s = {}
    for k in storyfiles:
        try:
            with open(storyfiles[k], 'r') as f:
                s[k] = f.read()
        except Exception as e:
            print(e)
    return s

def roll_article(s):
    o = random.choice(list(s.keys()))
    return o

def roll_adjectives(possible_adjectives=possible_adjectives):
    a = []
    for i in range(0, 3):
        a.append(random.choice(possible_adjectives))
    return a

def handle_post(data):
    adjektiivit = []
    print(data)
    for i in range(1,4):
        adjektiivit.append(data['adjective_'+str(i)])
    otsikko = data['content']
    return adjektiivit, otsikko


@app.route('/', methods=['GET', 'POST'])
def funny_page(sisalto={}):
    if request.method == 'POST':
        adjektiivit, otsikko = handle_post(request.form)
        sisalto['otsikko'] = otsikko
        sisalto['tarina'] = stories[otsikko]
    else:
        adjektiivit = roll_adjectives(possible_adjectives)
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
    print(stories)