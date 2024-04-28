# Introduction
Introducing SAM: The Segment Anything Model (SAM) by Meta marks a pivotal moment in computer vision, analogous to ChatGPT's breakthrough. Trained on an extensive dataset, SAM exhibits unparalleled prowess in segmenting diverse image modalities. However, its release without fine-tuning functionality presents a challenge for tailored applications. Fine-tuning, crucial for optimizing models to specific tasks, opens doors to advanced techniques like Low-Rank Adaptation (LoRA). In this project, we explore the integration of SAM and fine-tuning methodologies to unlock the full potential of computer vision in addressing diverse real-world challenges.

One such critical application is detecting forest patterns in satellite photographs. By harnessing SAM's segmentation capabilities and fine-tuning it for this task, we aim to contribute significantly to forest conservation efforts. The ability to accurately identify forest areas helps prevent deforestation by enabling timely intervention and monitoring. Moreover, it aids in assessing forest health, biodiversity conservation, and mitigating climate change impacts. Our project underscores the urgency and importance of leveraging cutting-edge technology like SAM to safeguard our planet's vital ecosystems and ensure sustainable development.

## Data Preprocessing
We collected more than 2000 images of various satellite observations; There were pictures from areas with a high concentration of greenery (like Datasets from Amazon & Atlantic Forests) as well as datasets with an extensive variety of landscapes (DeepGlobe DataSet that contains images and masks that represent 7 types of terrain, such as water, agriculture, urban, forest, etc.). After preproccesing the data, we divided all sample-images with available masks into training and validation datatsets in 9:1 proportion.  

Data Preprocessing makes up a significant portion of the code in this repository. That is due to the variety of formats and types of input databases. In the next part of this subsection we briefly explain what functons do the implemened algorithms serve. 

folder data_preprocessing_package:
1. divide_jpg_and_png.py
Was used for dividing given images and their respectful masks in the DeepGlobe DataSet (reference 3).
2. convert_jpg_folder_to_png.py
Contains a function that convertes all jpg-images from given folder into png format and adds them to another referenced folder. Was used when converting given images in the DeepGlobe DataSet (reference 3).
3. make_masks_binary.py
In the DeepGlobe DataSet, the given masks differentiate 7 types of landscape, but for our task, only the forest pixels are relevant. They have the corresponding [0, 255, 0] RGB code in those masks. That is why we convert each mask, turning the pure green color into pure white (that is how forest pixels are represented in the binary masks). All of the other 6 possible RGB encodings are all converted to pure black, since they are not forest. That is how we make the masks in a given folder binary.
4. renaming_masks.py
Renames masks so that eavh file name consists only of unique picture id (same is done on photographs). That helps us with assigning the same name for each image & mask (they are in separate folders), because our model requires the names to be identical.
5. compress.py
After converting a DeepGlobe DataSet, we realized that the images were enormously large due to the terrain diversity, so we decided to compress them to the 1024*1024 pixels. This method allows to automate the compressing process for the whole package; we also applied the algorithm on corresponding masks, so they would have the same dimension as the photos.
6. convert_from_P_to_RGB.py
The png photos of a DeepGlobe DataSet also needed to be converted to RGB format, as they were not given like that.
7. fix_pixels.py
Due to the unevitable compression performed on DeepGlobe DataSet´s masks, some of the "borderline" pixels between pure black and whites became grey-scaled. We provide a function that computes the "distance" to pure black & white and assigns one of those colors (the one with smaller "distance" value) to each unsuited pixel.
8. random_validation_assignment.py
When inspecting the DeepGlobe DataSet, we realized that the validation photographs do not have masks, so we needed to split available train data into new training and validation set, This method helps to choose 100 photographs randomly and refactor them with their masks for validation purposes.
9. convert_tif_to_png.py
After unzipping (unraring :)) the rar archives, all of the masks and images were in tif/tiff format and should have been converted to png as it is our chosen data format. This method helps us convert the pictures even though they were given in an unsupported by windows or python form. The tif picture´s pixels are being rescaled to [0,255] intervals so the images can be processed and transformed into pngs. 
10. comparing_names_and_size.py
This method is used for filtering out any training/validation purposed images that do not have an according mask or if the existing corresponding mask has different dimension compared to the photograph. If that is the case, the images(photographs) are being deleted from the handed folder. This method can also be used the other way round (filtering out masks that have no corresponding image). The first input folder should contain all images and the second should consist of the masks of the first folder´s pics. It is also important that the image from first folder and "its" mask from the second folder should be named identically, we already introduced a method for hat subtask. This method is also used after necessary resizing of the data so it acts as the forelast step, so to say it is our additional check for the correctness of the previously done procedures.
11. RGBA_package_check.py
The last check; takes folders of images or masks in png format as input. Iterates through the folders and proves whether each picture from the folder satisfies the three following characteristics. Firstly, whether the R, G and B parameters of every pixel take values between 0 and 255 (both inclusively) - that ensures that each picture is in RGB format. Secondly, whether the alpha channel parameter is equal to 255 - guaranteeing that every pic is non-transparent. Lastly, this binnary criterion should be true for the masks folders only - Whether all three parameters (R, G and B) for every picture in the package are either all equal to 0 or all equal to 255 - ensuring all of the masks are binary and contain pure black and white only.


## Setup
The project use python poetry.

```bash
pip install poetry
```

If you are running this on a headless server, run this first so that poetry doesn't hang:
```bash
export PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring
```

To install the dependencies use:
```bash
poetry config virtualenvs.in-project false
```

```bash
poetry install --all-extras
```

Some dependencies are not loaded with the poetry install, so I added them manually.
```bash
poetry run pip install --upgrade torch torchvision gradio safetensors opencv-python monai
```

Download the image encoder checkpoint (`only support vit-b`)
```bash
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth
```

## Notes on the Data
- The script expects all of the images to have the same amount of channels (all RGB, all Grayscale, etc) and no alpha channel (transparency). This will be proved via data-preprocessing folders

## Train
Configure the model and paths in the configuration file:
```bash
config.yaml
```

To run the training, use:
```bash
poetry run python train.py
```

# References

1. https://zenodo.org/records/3233081#.Y6LPLOzP1hE - 
2. https://zenodo.org/records/4498086#.Y6LPLuzP1hE
3. https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset
