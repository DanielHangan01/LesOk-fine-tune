# Introduction
Introducing SAM: The Segment Anything Model (SAM) by Meta marks a pivotal moment in computer vision, analogous to ChatGPT's breakthrough. Trained on an extensive dataset, SAM exhibits unparalleled prowess in segmenting diverse image modalities. However, its release without fine-tuning functionality presents a challenge for tailored applications. Fine-tuning, crucial for optimizing models to specific tasks, opens doors to advanced techniques like Low-Rank Adaptation (LoRA). In this project, we explore the integration of SAM and fine-tuning methodologies to unlock the full potential of computer vision in addressing diverse real-world challenges.

One such critical application is detecting forest patterns in satellite photographs. By harnessing SAM's segmentation capabilities and fine-tuning it for this task, we aim to contribute significantly to forest conservation efforts. The ability to accurately identify forest areas helps prevent deforestation by enabling timely intervention and monitoring. Moreover, it aids in assessing forest health, biodiversity conservation, and mitigating climate change impacts. Our project underscores the urgency and importance of leveraging cutting-edge technology like SAM to safeguard our planet's vital ecosystems and ensure sustainable development.

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

# Reference

1. https://zenodo.org/records/3233081#.Y6LPLOzP1hE - 
2. https://zenodo.org/records/4498086#.Y6LPLuzP1hE
3. https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset
