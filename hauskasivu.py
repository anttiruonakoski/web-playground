#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template
import random

app = Flask(__name__)

template_filename = 'anzun.html'

story_filenames = ['ilmasto.txt', 'pasta.txt']

dirs = {
    'imgdir': 'static/img/',
    'styledir': 'static/css/'
}

possible_adjectives = ['cooli', 'epäcooli', 'tyhjä', 'pörröinen', 'höpö', 'suurenmoinen', 'vituttava', 'vihreä', 'neliömäinen', 'pyöreä', 'juustomainen', 'kukkainen', 'koiramainen', 'iso', 'kaunis', 'upee', 'harmaa', 'pimeä']


def read_content(story_filenames):
    stories = []
    for file in story_filenames:
        try:
            with open(file, 'r') as f:
                stories.append(f.read())
        except Exception as e:
            print(e)
    return random.choice(stories)


def roll_adjectives(possible_adjectives=possible_adjectives):
    a = []
    for i in range(0, 3):
        a.append(random.choice(possible_adjectives))
    return a


@app.route('/')
def funny_page():
    return render_template(
        template_filename,
        adjektiivit=roll_adjectives(possible_adjectives),
        sisalto=read_content(story_filenames),
        dirs=dirs)


if __name__ == '__main__':
    app.run('0.0.0.0', 5001)