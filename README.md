## Train Your Model in PyTorch
Model Training in PyTorch

## Includes
- [models](models) for training on CIFAR-10 and Tiny ImageNet.
  - [ResNet for CIFAR-10](models/resnet.py)
  - [Custom ResNet for CIFAR-10](models/custom_resnet.py)
  - [ResNet18 for Tiny ImageNet](models/resnet18.py)
- [GradCAM](utils/grad_cam.py) for seeing the features of model at each layer.
- [transforms](utils/transforms.py) for various augmentation strategies.
- [LR Finder](utils/lr_finder.py) for finding the best learning rate.
- Some [general helper functions](utils/helper.py)
  - `model_summary` - Summary of the model.
  - `get_default_device` - To get the device. Pick GPU if available, else CPU.
  - `seed_everything` - Seed everything for reproducibility and deterministic behaviour.
  - `class_level_accuracy` - Accuracy per class level.
  - `unnormalize` - De-normalize the image.
  - `calculate_mean_std` - Calculate mean and std for a dataset.
- Some [helper functions for plots](utils/plot_utils.py)
  - `show_batch` - Visualize a batch of images.
  - `plot_metrics` - Plot Train and Test Accuracy and Loss.
  - `misclassified_images` - Get misclassified images.
  - `plot_misclassified_images` - Plot the misclassified images.
- And finally [trainer](main.py) to train and evaluate a model on a given dataset.

## Folder Structure
```bash
.
├── main.py
├── models
│   ├── custom_resnet.py
│   ├── __init__.py
│   └── resnet.py
    └── resnet18.py
├── README.md
├── requirements.txt
└── utils
    ├── dataset.py
    ├── grad_cam.py
    ├── helper.py
    ├── lr_finder.py
    ├── __init__.py
    ├── plot_utils.py
    ├── test.py
    ├── train.py
    └── transforms.py
```
