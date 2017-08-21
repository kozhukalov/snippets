import argparse
import itertools
import math
import os
import yaml
import subprocess

from jinja2 import FileSystemLoader
from jinja2 import Environment


class Render(object):
    def __init__(self, template):
        self.env = Environment(
            loader=FileSystemLoader(
                os.path.dirname(os.path.abspath(template))))
        self.template = self.env.get_template(
            os.path.basename(os.path.abspath(template)))

    def render(self, data):
        return self.template.render(data=data)

    def render2file(self, filename, data):
        with open(filename, "w") as f:
            f.write(self.render(data).encode("utf-8"))


def _paginate(items, items_on_page):
    for i, chunk in enumerate(
            itertools.izip_longest(*([iter(items)] * items_on_page)), start=1):
        yield (i, filter(lambda x: x is not None, chunk))


def index(data):
    template = data["template"]
    items_on_page = data.get("items_on_page", 10)
    items = data.get("items", [])
    dir = os.path.dirname(data["output"])
    name, ext = os.path.basename(data["output"]).rsplit(".", 1)
    num_pages = int(math.ceil(float(len(items)) / float(items_on_page)))

    all_pages = {
        i: os.path.join(name + (str(i) if i > 1 else "") + "." + ext)
        for i in [i + 1 for i in range(num_pages)]
    }
    if len(all_pages.keys()) == 1:
        all_pages = {}

    for idx, chunk in _paginate(items, items_on_page):
        suffix = (idx if idx > 1 else "")
        page_output = os.path.join(dir, name + str(suffix) + "." + ext)
        data = {
            "items": chunk,
            "pages": all_pages
        }
        rf = Render(template=template)
        rf.render2file(page_output, data)


def post(data):
    rf = Render(template=data["template"])
    rf.render2file(data["output"], data)


def iterate(data, metadata_directory):
    for section in data:
        if "include" in section:
            with open(os.path.join(metadata_directory, section["include"])) as f:
                section_data = yaml.safe_load(f)
            for subsection in iterate(section_data, metadata_directory):
                yield subsection
        else:
            yield section


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata", action="store", dest="metadata",
                        required=True, help="Path to metadata file")

    known, others = parser.parse_known_args()
    metadata_directory = os.path.dirname(known.metadata)

    with open(known.metadata) as f:
        data = yaml.safe_load(f)

    for section in iterate(data, metadata_directory):
        globals()[section["type"]](section)

if __name__ == "__main__":
    main()
