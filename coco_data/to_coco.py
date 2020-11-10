import json


class Coco:
    def __init__(self):
        self.document = None
        self.coco = {}

    def load_document(self, path):
        with open("img_annotations.json") as json_file:
            self.document = json.load(json_file)

    def transform(self):
        pass
