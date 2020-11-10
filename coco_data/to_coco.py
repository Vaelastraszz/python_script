import json
import csv
from PIL import Image
import _locale


class Coco:
    def __init__(self):
        self.document = self.load_document
        self.language = self.create_language
        self.coco = {}
        self.coco["info"] = {}
        self.coco["licenses"] = [{}]
        self.coco["images"] = []
        self.coco["annotations"] = []
        self.coco["categories"] = []

        self.coco["info"]["year"] = 2020
        self.coco["info"]["version"] = 1
        self.coco["info"]["description"] = "Food Images for localization"
        self.coco["info"]["contributor"] = "Romain Lejeune"

        self.coco["licenses"][0]["id"] = 1
        self.coco["licenses"][0]["name"] = "Public Domain"

    @property
    def load_document(self):
        with open("img_annotations.json") as json_file:
            self.document = json.load(json_file)

        return self.document

    @property
    def create_language(self):
        with open("label_mapping.csv") as csv_file:
            food_inv = csv.reader(csv_file, delimiter=";")
            next(food_inv)
            food_dic = {row[0]: row[2] for row in food_inv}
        return food_dic

    def get_size(self):
        for k in self.document.keys():
            im = Image.open("assignement_imgs/" + k)
            width, height = im.size

    def transform(self):
        pass


if __name__ == "__main__":
    test = Coco()
    print(print(test.language))
