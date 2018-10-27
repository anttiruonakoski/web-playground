#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
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

possible_adjectives = ['cooli', 'epäcooli', 'tyhjä', 'pörröinen', 'höpö', 'suurenmoinen', 'vituttava', 'vihreä', 'neliömäinen', 'pyöreä', 'juustomainen', 'kukkainen', 'koiramainen', 'iso', 'kaunis', 'upee', 'harmaa', 'pimeä']


def read_content(stories):
    s = {}
    for k in stories:
        try:
            with open(stories[k], 'r') as f:
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
def funny_page():
    if request.method == 'POST':
        adjektiivit, otsikko = handle_post(request.form)
    else:
        adjektiivit = roll_adjectives(possible_adjectives)
        otsikko = roll_article(stories)
    return render_template(
        template_filename,
        adjektiivit=adjektiivit,
        sisalto=stories[otsikko],
        otsikot=list(stories.keys()),
        dirs=dirs)


if __name__ == '__main__':
    stories = read_content(storyfiles)
    print(stories)
    app.run('0.0.0.0', 5001)