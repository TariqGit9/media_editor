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

# if __name__ == "__main__":
#     image_processor = ImageProcessor("image.png")

#     # Apply filters and save images
#     image_processor.save_image(image_processor.apply_blur_filter(), "image_blur.jpg")
#     image_processor.save_image(image_processor.apply_contour_filter(), "image_contour.jpg")
#     image_processor.save_image(image_processor.apply_detail_filter(), "image_detail.jpg")
#     image_processor.save_image(image_processor.apply_edge_enhance_filter(), "image_edge_enhance.jpg")
#     image_processor.save_image(image_processor.apply_emboss_filter(), "image_emboss.jpg")
#     image_processor.save_image(image_processor.apply_sharpen_filter(), "image_sharpen.jpg")
#     image_processor.save_image(image_processor.apply_smooth_filter(), "image_smooth.jpg")

#     # Resize and save the image
#     resized_image = image_processor.resize_image(400, 300)
#     image_processor.save_image(resized_image, "resized_image.jpg")

#     # Apply reddish black-and-white filter and save
#     reddish_bw_image = image_processor.apply_reddish_black_and_white_filter()
#     image_processor.save_image(reddish_bw_image, "reddish_black_and_white.jpg")

#     # Convert to grayscale and save
#     grayscale_image = image_processor.convert_to_grayscale()
#     image_processor.save_image(grayscale_image, "black_and_white.jpg")
