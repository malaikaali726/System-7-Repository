# Day 21 - Transfer Learning and Image Classifier (Module D)

## Learning notes
**Feature extraction vs fine-tuning.** With feature extraction, the pretrained base is frozen and only the new output layer learns. This is fast and works well when your dataset is small or similar to the original training data (ImageNet). With fine-tuning, you unfreeze some of the top layers of the base and train them with a very small learning rate. This adapts the model more closely to your data but needs more data and care to avoid overwriting useful features.

## Practice questions
- Q18 - `q18_mobilenet_transfer.py`: MobileNetV2 with a frozen base, compared with the scratch CNN, with prediction visualization

## Image classifier task
The task uses CIFAR-10 (objects and animals). To classify plant diseases instead, replace the dataset with an image folder loaded through `keras.utils.image_dataset_from_directory`.
