#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import shutil
import glob
import random

template_filename = 'lomake_2.html'
story_filename = 'ilmasto.txt'

dirs = {
    'imgdir': 'img/',
    'styledir': 'css/'
}

file_loader = FileSystemLoader('./templates')
env = Environment(loader=file_loader)
template = env.get_template(template_filename)

adjektiivit = []


def main():
    try:
        with open(story_filename, 'r') as f:
            sisalto = f.read()
    except Exception as e:
        print(e)

    mahdolliset_adjektiivit = ['cooli', 'epäcooli', 'tyhjä', 'pörröinen', 'höpö', 'suurenmoinen', 'vituttava', 'vihreä', 'neliömäinen', 'pyöreä']

    for i in range(0, 3):
        adjektiivit.append(random.choice(mahdolliset_adjektiivit))

    # for numero in range(0,3):
    # adjektiivit.append(input(f'anna adjektiivi numero {numero+1} \n'))

    html = template.render(adjektiivit=adjektiivit, sisalto=sisalto, dirs=dirs)

    try:
        f = open('public/index.html', 'w')
        f.write(html)
    except Exception as e:
        print(e)

    dest_dir = 'public/'
    # copy css
    try:
        shutil.copy('static/css/style.css', dest_dir+'css/style.css')
    except Exception as e:
        print(e)

    # copy images
    try:
        for file in glob.glob(r'static/img/*.jpg'):
            print(f'siirrettään kuva {file}')
            shutil.copy(file, dest_dir+'img/')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()