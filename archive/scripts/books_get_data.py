#!/usr/bin/env python
import requests
import sys
import json
import yaml
from argsy import Argsy

ARG_DEF="""
program:
  name: get_book_data.py
  args:
    seed_data:
      cmd_type: option
      flags: '-s|--seed-data'
      help: 'YAML-formatted list of ISBN numbers to be used during lookup'
      required: true
    output_filename:
      cmd_type: option
      flags: '-o|--output'
      help: 'Output filename'
      required: true
"""

def api_call(idn):
    url = f"https://openlibrary.org/api/books?jscmd=data&bibkeys={idn}&format=json"
    print(url)
    return requests.get(url).json().get(f'{idn}')


def generate_data(idn_list):
    book_list = []

    for idn in idn_list:
        book_data = api_call(idn)
        # print(json.dumps(book_data, indent=2))
        book_list.append(
            dict(
                title = book_data.get('title'),
                author = book_data.get('authors')[0].get('name'),
                cover = book_data.get('cover').get('medium'),
                url = book_data.get('url')
            )
        )
    
    return book_list


def main():
    parsed_input = Argsy(config_str=ARG_DEF).parse_args(args=sys.argv[1:], print_result=True)

    args = parsed_input.get('args')

    with open(f'{args.get("seed_data")}','r') as seed_data_file:
        seed_data = yaml.load(seed_data_file, Loader=yaml.SafeLoader)
        # print(seed_data)
        
        book_list = dict(books = generate_data(seed_data))

        with open(f'{args.get("output")}','w') as data_file:
            data_file.write(yaml.dump(book_list))


main()