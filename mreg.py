#!/usr/bin/env python3

from flask import Flask, Response
import requests
import configparser
from bs4 import BeautifulSoup
import click


def scrape_releases():
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7',
    }

    page = requests.get('https://www.dvdsreleasedates.com/', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    requested_table = soup.find("div", {"id": 'requested'})
    requested_hrefs = requested_table.find_all('a')
    movie_names = [ movie.contents[0].replace(' ', '?') + "*," for movie in requested_hrefs ]

    return movie_names


def update_autodl_cfg(expression, autodlcfg, filter_name):
    new_expression = ''.join(expression)
    config = configparser.ConfigParser()
    config.read(autodlcfg)
    config[filter_name]['match-releases'] = new_expression
    with open(autodlcfg, 'w') as configfile:
        config.write(configfile)

    return True


@click.command()
@click.option('-c', '--autodlcfg', 'autodlcfg', envvar='MREG_AUTODLCFG_PATH', default='~/.autodl/autodl.cfg', show_default=True, help='The path to your autodl.cfg file.')
@click.option('-f', '--filter', 'filter', envvar='MREG_FILTER_NAME', required=True, help='The name of your autodl-irssi filter for movies.')
def mreg(autodlcfg, filter):
    expression = scrape_releases()
    update_autodl_cfg(expression, autodlcfg, filter)
    click.echo('Your filter was updated successfully!')

# TODO: add "live" mode which triggers every x minutes

