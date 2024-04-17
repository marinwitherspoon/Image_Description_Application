# Image_Description_Application

## Intro
This project experimented with image description generation using the Microsoft GIT Base model found on huggingFace. The datasets used for experimentation consist of Flickr3k, Flickr8k and Instagram Images with Captions. 

For each dataset, a model was fine tuned and then in a seperate notebook, inference was performed and ROUGE score was calculated against the test set. 

The following files correspond to the finetuning process and inference process respectively:
- Flickr 3k: 3k_Microsoft_git_based_Finetuned_PyTorch.ipynb, 3k_model_predict.ipnb
- Flickr 8k: 8k_grad_acc_Microsoft_git_based_Finetuned_PyTorch_v2.ipynb, 8k_grad_acc_model_predict.ipynb
- Instagram: Instagram_FineTuned.ipnyb, instagram_model_predict.ipynb

## Main Application
Finally, the Flickr8k model was selected to use for a simple user interface build with Streamlit version 1.24.0. Upon launching the application (UI_Image_caption.py), the user can upload an image and the model is used to generate a caption for the user. The files for the finetuned model must be present in the same directory as the user interface.

### Requirements for UI_Image_Caption.py
-Python 3.0 or higher
- streamlit version 1.24.0
- torch
- transformers
- accelerate
- PIL
- numpy
- os


### Instructions to run UI_Image_Caption.py
- streamlit run UI_Image_Caption.py

## Datasets and Model Access
The Flickr 3k and 8k datasets and model files were too large to upload to Github so links are provided ffor access:
- Flickr3k dataset: https://drive.google.com/drive/folders/1lwqk9jd1oVHMIe2NiUxD68zKU2mjd6F4?usp=drive_link
- Flickr 8k dataset: https://drive.google.com/drive/folders/1k_NC7LSjQIpwCQJeItHLUR6M2FbYAdAM?usp=sharing
- Flickr 8k model: https://drive.google.com/file/d/1_fRVYBHAeC7HS76b9OFqiVS9mIWUwUYj/view?usp=sharing
- Flickr 8k optimizer state: https://drive.google.com/file/d/13tzP2ti7x3sxAR__GvT2f3PZH-EP2_k6/view?usp=sharing

In order to create and structure the data to be compatible with HuggingFace load_dataset function, Data_Formatting.ipynb was used. 

This repository is maintained by Surabhi Kulkarni, Marin Witherspoon and Sumit Hawal for the DS 5500 Capstone Class at Northeastern University

## Other Files
Other files that are reflective of our work/effort but not directly pertinent to the final deliverables of the project:

- User_Interface.ipynb (initial attempt at user interface)
- data_Cleaning.ipynb (initial data cleaning process)
- data_structure (initial preprocessed data structure)
  1. captions.txt --> images with description.
  2. data_process --> gettign the images and descrption in desirable format.
  3. captions.json --> images with captions with required format.
  4. images_structure --> text file explaining how the data is kept prior to preprocessing.
