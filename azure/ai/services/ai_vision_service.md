Azure AI Vision Service
---

- It provides `prebuilt` and `customizable computer vision models` that are based on the `Florence foundation model` and provide various powerful capabilities.
- With Azure AI Vision, you can create sophisticated computer vision solutions quickly and easily; taking advantage of "off-the-shelf" functionality for many common computer vision scenarios, while retaining the ability to `create custom models using your own images`.

# Azure resources for Azure AI Vision service

## Azure AI Vision

- A specific resource for the Azure AI Vision service.
- Use this resource type `if you don't intend to use any other Azure AI services`, or if you want to `track utilization and costs` for your Azure AI Vision resource `separately`.

## Azure AI Services

- A general resource that `includes Azure AI Vision` along with many other Azure AI services; such as `Azure AI Language, Azure AI Custom Vision, Azure AI Translator`, and others.
- Use this resource type if you plan to `use multiple AI services` and want to `simplify administration and development`.

# Using Azure AI Vision service

Many task can be performed in `Azure AI Vision Studio`.

# Azure AI Vision Service Capabilities

## Optical Character Recognition (OCR)

- Analyze image and extract the text.

## Describing an image  with captions

- Ability to analyze an image, evaluate the objects that are detected, and generate a human-readable phrase or sentence that can describe what was detected in the image.

## Detecting common objects in an image

- Identify thousands of common objects in images.
- Predictions include a confidence score that indicates the probability the model has calculated for the predicted objects.

## Tagging visual features

- Suggest tags for an image based on its contents. 
- These tags can be associated with the image as `metadata` that summarizes attributes of the image and can be useful if you want to index an image along with a set of key terms that might be used to search for images with specific attributes or contents.

# Training custom models

- You can use custom models for image classification or object detection.
- Azure AI Vision builds custom models on the pre-trained foundation model, meaning that you can train sophisticated models by using relatively few training images.
- Uses Cases:
    - Image classification
    - Object detection
