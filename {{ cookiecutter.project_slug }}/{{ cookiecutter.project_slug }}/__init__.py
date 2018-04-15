# -*- coding: utf-8 -*-
import argparse
import configparser
import logging

__author__ = '{{cookiecutter.full_name}}'
__email__ = '{{cookiecutter.email}}'
__version__ = '{{cookiecutter.version}}'
__project__ = '{{cookiecutter.project_slug}}'

def boot(config):
    section = 'dummy'
    key = 'hello'
    print("{0} {1}".format(key, config.get(section, key)))

def main():
    """Entrypoint for service."""
    parser = argparse.ArgumentParser(description='Service Arguments')
    parser.add_argument('-c',
                        '--config',
                        help='config file path',
                        default='{{cookiecutter.project_slug}}/etc/config.ini')

    parser.add_argument('-l',
                        '--logs',
                        help='logs file path',
                        default='{{cookiecutter.project_slug}}/logs/{{cookiecutter.project_slug}}.log')

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    fmt = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename=args.logs)

    boot(config)


if __name__ == '__main__':
    main()
