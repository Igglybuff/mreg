#!/usr/bin/env python3

from flask import Flask, Response
import requests
import configparser
from bs4 import BeautifulSoup
import click
from pathlib import Path
import re
import sys


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


def get_abs_path(file):
    file = Path(file)
    return file.resolve(strict=True)


def update_autodl_cfg(expression, autodlcfg, filter_name):
    autodlcfg_abs = get_abs_path(autodlcfg)
    new_expression = ''.join(expression)
    config = configparser.ConfigParser()
    config.read(get_abs_path(autodlcfg_abs))
    config[filter_name]['match-releases'] = new_expression
    with open(get_abs_path(autodlcfg_abs), 'w') as configfile:
        config.write(configfile)


def fix_filter(filter_name):
    # if first word of filter is not "filter",
    # prepend expression with "filter "
    pass


def check_config(autodlcfg, filter_name):
    config = configparser.ConfigParser()
    config.read(get_abs_path(autodlcfg))
    if not filter_name in config:
        raise configparser.Error('Unable to find filter "' + filter_name + '" in ' + autodlcfg)


def check_regex_validity(expression):
    new_expression = ''.join(expression)
    try:
        re.compile(new_expression)
    except re.error:
        click.echo('ERROR - mreg generated an invalid regex.')
        sys.exit(1)


@click.command()
@click.option('-c', '--autodlcfg', 'autodlcfg', envvar='MREG_AUTODLCFG_PATH', default='~/.autodl/autodl.cfg', show_default=True, help='The path to your autodl.cfg file.')
@click.option('-f', '--filter', 'filter', envvar='MREG_FILTER_NAME', required=True, help='The name of your autodl-irssi filter for movies.')
def mreg(autodlcfg, filter):
    expression = scrape_releases()
    check_regex_validity(expression)
    fix_filter(filter)
    check_config(autodlcfg, filter)
    update_autodl_cfg(expression, autodlcfg, filter)
    click.echo('Your filter was updated successfully!')

# TODO: add "live" mode which triggers every x minutes
