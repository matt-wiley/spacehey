import os

from spacehey_maker.templates.template_catalog import TemplateCatalog

from jinja2 import Environment, select_autoescape, FunctionLoader, PackageLoader


class Renderer():

    def __init__(self, template_base_dir: str) -> None:
        self._user_template_base_dir = template_base_dir
        self._template_catalog = TemplateCatalog()
        self._base_env = Environment(
            loader=PackageLoader('spacehey_maker','templates')
        )

    def _get_contents(self, file_path: str):
        with open(file_path, 'r') as file_contents:
            return file_contents.read()


    def _load_template(self, template: str):
        template_name = os.path.basename(template)
        if template.endswith("base_profile.j2"):
            template_path = self._template_catalog.get_template_path(template_name)
            return self._get_contents(template_path)
        else:
            if self._user_template_base_dir is None or self._user_template_base_dir == "":
                base_path = ""
            else:
                base_path = f"{self._user_template_base_dir}/"
                
            template_path = f"{base_path}{template}"
            return self._get_contents(template_path)


    def render(self, template_path: str, data: dict, output_path: str):
        env = self._base_env.overlay(
            loader=FunctionLoader(load_func=self._load_template),
            autoescape=select_autoescape()
        )
        template = env.get_template( os.path.basename(template_path) )
        with open(output_path, 'w') as output_path:
            output_path.write(template.render(data))