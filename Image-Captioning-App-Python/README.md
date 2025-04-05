# Image Caption Generator with BLIP and Gradio

This project implements an image captioning system using the pretrained BLIP model from Hugging Face and provides a user-friendly web interface built with Gradio. The application allows users to upload images and automatically generates descriptive captions for them.

## Explanation:
The Image Caption Generator is a sophisticated application that combines cutting-edge artificial intelligence with an intuitive user interface to automatically generate descriptive captions for images. At its core, the project leverages the BLIP (Bootstrapped Language-Image Pre-training) model from Hugging Face, a powerful vision-language model pretrained on vast datasets to understand and describe visual content. The system processes images through the `AutoProcessor`, which handles the necessary preprocessing steps to prepare images for the model, while the `BlipForConditionalGeneration` component generates natural language captions based on the visual input. This functionality is encapsulated within the `Generator` class in `image_cap.py`, keeping the image processing logic separate and modular. The `main.py` file integrates this functionality into a user-friendly web application using Gradio, allowing users to upload images through a browser interface and receive instant captions. This project demonstrates the practical application of vision-language models and provides an accessible tool for generating image descriptions, with potential use cases ranging from content creation to accessibility enhancements.
## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Features
- Automatic image caption generation using the BLIP model
- Simple web interface for uploading images and viewing captions
- Modular code structure with separate files for image processing and web app
- Easy-to-use Gradio interface

## Requirements
- Python 3.8+
- Git
- Basic understanding of Python and machine learning concepts

## Project Structure
AI-image-caption-generator/
│
├── main.py             # Gradio web interface implementation
├── image_cap.py        # Image processing and caption generation logic
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation


## Usage
-1 Run the application:
```bash
python main.py
```
2. Open your web browser and go to the URL displayed in the terminal (typically http://127.0.0.1:7860)
3. Use the interface:
    * Click "Choose File" to upload an image
    * Wait for the caption to be generated
    * View the generated caption below the image


## How It Works
The project consists of two main components:

1. image_cap.py:
    * Contains the Generator class
    * Uses AutoProcessor to preprocess uploaded images
    * Utilizes BlipForConditionalGeneration for caption generation
    * Handles the core image captioning functionality
2. main.py:
    * Imports the Generator class from image_cap.py
    * Creates a Gradio interface
    * Sets up the web application
    * Handles user interactions
The BLIP (Bootstrapped Language-Image Pre-training) model is a state-of-the-art vision-language model that generates natural language descriptions for images.
## Dependencies
  * torch
  * transformers
  * gradio
  * PIL (Python Imaging Library)


## License
This project is licensed under the MIT License - see the  file for details.



