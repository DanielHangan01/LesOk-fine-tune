import torch
import numpy as np
from src.segment_anything import build_sam_vit_b, SamPredictor, sam_model_registry
from src.processor import Samprocessor
from src.lora import LoRA_sam
from PIL import Image
import matplotlib.pyplot as plt
import src.utils as utils
from PIL import Image, ImageDraw
import yaml
import json
from torchvision.transforms import ToTensor

"""
This file is used to plots the predictions of a model (either baseline or LoRA) on the train or test set. Most of it is hard coded so I would like to explain some parameters to change 
referencing by lines : 
line 22: change the rank of lora; line 98: Do inference on train (inference_train=True) else on test; line 101 and 111 is_baseline arguments in fuction: True to use baseline False to use LoRA model. 
"""
sam_checkpoint = "sam_vit_b_01ec64.pth"
device = "cuda" if torch.cuda.is_available() else "cpu"
sam = build_sam_vit_b(checkpoint=sam_checkpoint)
rank = 512
sam_lora = LoRA_sam(sam, rank)
sam_lora.load_lora_parameters(f"lora_rank{rank} (1).safetensors")
model = sam_lora.sam


def inference_model(sam_model, image_path, filename, mask_path=None, is_baseline=False):
    if is_baseline == False:
        model = sam_model.sam
        rank = sam_model.rank
    else:
        model = build_sam_vit_b(checkpoint=sam_checkpoint)

    model.eval()
    model.to(device)
    image = Image.open(image_path)
    if mask_path != None:
        mask = Image.open(mask_path)
        mask = mask.convert('1')
        ground_truth_mask = np.array(mask)
        box = utils.get_bounding_box(ground_truth_mask)
    else:
        box = [0, 0, image.size[0], image.size[1]]

    predictor = SamPredictor(model)
    predictor.set_image(np.array(image))
    masks, iou_pred, low_res_iou = predictor.predict(
        box=np.array(box),
        multimask_output=False,
    )

    if mask_path == None:
        fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(15, 15))
        draw = ImageDraw.Draw(image)
        draw.rectangle(box, outline="red")
        ax1.imshow(image)
        ax1.set_title(f"Original image + Bounding box: {filename}")

        ax2.imshow(masks[0])
        if is_baseline:
            ax2.set_title(f"Baseline SAM prediction: {filename}")
            plt.savefig(f"./plots/{filename}_baseline.jpg")
        else:
            ax2.set_title(f"SAM LoRA rank {rank} prediction: {filename}")
            plt.savefig(f"./plots/{filename[:-4]}_rank{rank}.jpg")

    else:
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(15, 15))
        draw = ImageDraw.Draw(image)
        draw.rectangle(box, outline="red")
        ax1.imshow(image)
        ax1.set_title(f"Original image + Bounding box: {filename}")

        ax2.imshow(ground_truth_mask)
        ax2.set_title(f"Ground truth mask: {filename}")

        ax3.imshow(masks[0])
        if is_baseline:
            ax3.set_title(f"Baseline SAM prediction: {filename}")
            plt.savefig(f"./plots/{filename}_baseline.jpg")
        else:
            ax3.set_title(f"SAM LoRA rank {rank} prediction: {filename}")
            plt.savefig(f"./plots/{filename[:-4]}_rank{rank}.jpg")


# Open configuration file
with open("./config.yaml", "r") as ymlfile:
    config_file = yaml.load(ymlfile, Loader=yaml.Loader)

# Open annotation file
# f = open('annotations.json')
# annotations = json.load(f)


# train_set = annotations["train"]
test_set = {
    'lesok.png': {"mask_path": None},
    # '71125.png': {"mask_path": "./dataset/test/masks/71125.png"},
    # '71619.png': {"mask_path": "./dataset/test/masks/71619.png"},
    # '72807.png': {"mask_path": "./dataset/test/masks/72807.png"},
    # '76759.png': {"mask_path": "./dataset/test/masks/76759.png"},
}
inference_train = True

for image_name, dict_annot in test_set.items():
    image_path = f"./dataset/test/images/{image_name}"
    inference_model(sam_lora, image_path, filename=image_name, mask_path=dict_annot["mask_path"], is_baseline=False)
