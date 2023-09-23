# python modules 
from PIL import Image, ImageFilter
import os 
import io

class ImageProcessor:
    def __init__(self):
        pass

    def image_blur(self,image):
        return image.filter(ImageFilter.BLUR)

    def image_contour(self,image):
        return image.filter(ImageFilter.CONTOUR)

    def image_detail(self,image):
        return image.filter(ImageFilter.DETAIL)

    def image_edge_enhance(self,image):
        return image.filter(ImageFilter.EDGE_ENHANCE)

    def image_emboss(self,image):
        return image.filter(ImageFilter.EMBOSS)

    def image_sharpen(self,image):
        return image.filter(ImageFilter.SHARPEN)

    def smooth_filter(self,image):
        return image.filter(ImageFilter.SMOOTH)

    def resized_image(self,image, width, height):
        return image.resize((width, height))

    def black_and_white(self,image):
        return image.convert("L")

    def save_image(self, image, file_name):
        image.save(os.path.join('static/result', file_name), "JPEG")


    def convert_image(self,image):
        image = Image.open(io.BytesIO(image)).convert("RGB")
        return image
