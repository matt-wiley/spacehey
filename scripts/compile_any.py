#!/usr/bin/env python
import sys
import os
import yaml
from argsy import Argsy
from jinja2 import Environment, FileSystemLoader, select_autoescape

ARG_DEF="""
program:
  name: compile_any.py
  args:
    data:
      cmd_type: option
      flags: '-d|--data'
      help: 'YAML-formatted data set to be used by Jinja templating'
      required: true
    template:
      cmd_type: option
      flags: '-t|--template'
      help: 'Template file to be used by Jinja templating'
      required: true
    output_filename:
      cmd_type: option
      flags: '-o|--output'
      help: 'Output filename'
      required: true
"""


def render(template_path,data, output_path):
    env = Environment(
        loader=FileSystemLoader( os.path.dirname(template_path) ),
        autoescape=select_autoescape()
    )
    template = env.get_template( os.path.basename(template_path) )
    with open(output_path, 'w') as output_path:
        output_path.write(template.render(data))


def main():
    parsed_input = Argsy(config_str=ARG_DEF).parse_args(args=sys.argv[1:], print_result=True)
    args = parsed_input.get('args')
    with open(args.get('data'),'r') as template_data:
        render(
            template_path=args.get('template'),
            data=yaml.load(template_data,yaml.SafeLoader),
            output_path=args.get('output')
        )



main()