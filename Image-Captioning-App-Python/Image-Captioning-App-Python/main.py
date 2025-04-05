import gradio as gr
import numpy as np
from image_cap import Generator


main_path = "Bar_Chart.png"
caption_generator = Generator(main_path)

# Generate the caption using the method
my_caption = caption_generator.generate_caption()
print("The Caption of the image is : ")
print(my_caption)

def caption_image(input_image: np.ndarray):
    caption_generator = Generator(input_image)
    my_caption = caption_generator.generate_caption()
    return my_caption

iface = gr.Interface(
    fn=caption_image, 
    inputs=gr.Image(), 
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)

print("Let's Go")
iface.launch(server_name="0.0.0.0" , server_port = 7868 , share = True)