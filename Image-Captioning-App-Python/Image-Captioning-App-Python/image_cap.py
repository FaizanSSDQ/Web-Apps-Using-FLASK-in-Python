import requests
from PIL import Image
from transformers import AutoProcessor , BlipForConditionalGeneration
import numpy as np

# print("Welcome")
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base" , use_fast=False)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")



class Generator:

    def __init__(self, input_image):
        if isinstance(input_image, np.ndarray):
            # If input is a NumPy array, convert it to a PIL image
            self.image = Image.fromarray(input_image)
        else:
            # If input is a file path, open it as an image
            self.image = Image.open(input_image).convert('RGB')
    def generate_caption(self):
        # Generate caption based on the image
        text = 'the image of '
        inputs = processor(images=self.image, text=text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        if caption is None:
            caption = "This is finally done"
        return caption