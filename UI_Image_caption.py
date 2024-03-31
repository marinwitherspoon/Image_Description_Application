# import packages
# needs pip install streamlit==1.24.0 in order to run
#use command streamlit run UI_Image_caption.py to run
import torch
from PIL import Image
import numpy as np
import os
from transformers import AutoProcessor, AutoModelForCausalLM
import streamlit as st


#load model
processor = AutoProcessor.from_pretrained("microsoft/git-base")

loaded_model =  AutoModelForCausalLM.from_pretrained("microsoft/git-base")
loaded_optimizer = torch.optim.AdamW(loaded_model.parameters(), lr=5e-5)

# Load the saved model and optimizer state
loaded_model.load_state_dict(torch.load(r'finetuned_model_grad', map_location=torch.device('cpu')))
loaded_optimizer.load_state_dict(torch.load(r'optimizer_state_grad', map_location=torch.device('cpu')))

# Set the model to evaluation mode for inference
loaded_model.eval()

def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt") #.to(device)
    pixel_values = inputs.pixel_values
    generated_ids = loaded_model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_caption


def main():
    st.title("Image Captioning with Microsoft GIT Base Model")
    st.write("This application uses the Microsoft GIT Base model for image captioning. The model has been fine tuned on the Flickr 8k dataset.")
    st.write("Created by Surabhi Kulkarni, Sumit Hawal and Marin Witherspoon for the DS5500 Capstone Class at Northeastern.")

    # Upload image
    image = st.file_uploader("Upload Image to Generate a Caption", type=["jpg", "jpeg", "png"])

    if image is not None:
        # Display uploaded image
        img = Image.open(image)
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Generate caption
        if st.button('Generate Caption'):
            caption = generate_caption(img)
            st.write("### Generated Caption:")
            st.write(caption)

if __name__ == "__main__":
    main()