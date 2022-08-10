import os


class TemplateCatalog():

    def __init__(self) -> None:
        self._root_dir = os.path.abspath(os.path.dirname(__file__))

    def _template_path_for(self, template_file_name) -> str:
        return os.path.join(self._root_dir, template_file_name)

    def get_template_path(self, template_name) -> str:
        return self._template_path_for(template_name)