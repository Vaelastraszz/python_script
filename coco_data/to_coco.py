import json


class Coco:
    def __init__(self):
        self.document = None
        self.coco = {}
        self.coco["info"] = {}
        self.coco["licenses"] = {}
        self.coco["images"] = {}
        self.coco["annotations"] = {}
        self.coco["categories"] = {}
        self.coco["annotations"] = {}

    @property
    def load_document(self):
        with open("img_annotations.json") as json_file:
            self.document = json.load(json_file)

    def transform(self):
        self.load_document
