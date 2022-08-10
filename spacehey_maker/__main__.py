import os
import sys
import yaml

from argsy import Argsy

from spacehey_maker.libs.renderer import Renderer

from jinja2 import Environment, PackageLoader, select_autoescape

CLI_ARGS = """
program:
  name: spacehey_maker
  descripton: "Jinja templating to build SpaceHey layouts."
  args:
    root_dir:
      cmd_type: option
      flags: '-r|--root-dir'
      help: "Common root for template and data."
      required: false
    template:
      cmd_type: option
      flags: '-t|--template'
      help: "Template to use."
      required: true
    data_yaml:
      cmd_type: option
      flags: '-d|--data-yaml'
      help: "Data to template with."
      required: true
    output:
      cmd_type: option
      flags: '-o|--output'
      help: "Data to template with."
      required: false
"""


class SpaceHeyMaker:

    def make(self, template_path: str, data_path: str, output_path: str = None):
        with open(data_path,'r') as data_contents:
            data: dict = yaml.load(data_contents, yaml.SafeLoader)
            os.makedirs('./gen', exist_ok=True)

            if output_path is None:     
              output_path = f"gen/{template_path.replace('.j2','.html')}"
              os.makedirs(os.path.dirname(output_path), exist_ok=True)

            renderer = Renderer(
                template_base_dir=os.path.dirname(template_path)
            )
            
            renderer.render(
                template_path=template_path,
                data=data,
                output_path=output_path
            )


if __name__ == "__main__":
    parsed_args = Argsy(config_str=CLI_ARGS).parse_args(sys.argv[1:], True)
    args = parsed_args.get('args')
    SpaceHeyMaker().make(
        template_path=args.get('template'),
        data_path=args.get('data_yaml'),
        output_path=args.get('output')
    )