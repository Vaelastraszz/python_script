import csv
import json
import os
import glob
from PIL import Image


class Coco:
    def __init__(self):
        self.document = self.load_document
        self.language = self.create_language
        self.coco = {}
        self.hash_img = {}
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

    @property
    def create_imgs(self):
        for i, filename in enumerate(glob.iglob("assignment_imgs/*.j*")):
            temp_dict = {}
            img = Image.open(
                "/Users/RomainLejeune/Desktop/python_script/coco_data/" + filename
            )
            width, height = img.size

            if filename not in self.hash_img:
                self.hash_img[filename.split("/")[-1]] = i

            temp_dict["id"] = i
            temp_dict["file_name"] = filename.split("/")[-1]
            temp_dict["width"] = width
            temp_dict["height"] = height

            self.coco["images"].append(temp_dict)

    @property
    def create_categ(self):
        for key, value in self.language.items():
            temp_dict = {}
            temp_dict["id"] = key
            temp_dict["name"] = value
            temp_dict["supercategory"] = "none"
            self.coco["categories"].append(temp_dict)

    @property
    def create_annotations(self, i=0):
        for key, value in self.document.items():
            for element in value:
                if element["is_background"] is False:
                    temp = {}
                    temp["id"] = i
                    temp["image_id"] = self.hash_img[key]
                    temp["category_id"] = element["id"]
                    temp["bbox"] = element["box"]
                    temp["area"] = element["box"][-1] * element["box"][-2]
                    temp["segmentation"] = []
                    temp["iscrowd"] = 0
                    self.coco["annotations"].append(temp)
                    i += 1


if __name__ == "__main__":
    prout = Coco()
    prout.create_imgs
    prout.create_categ
    prout.create_annotations
    with open("data.json", "w") as fp:
        json.dump(prout.coco, fp)
