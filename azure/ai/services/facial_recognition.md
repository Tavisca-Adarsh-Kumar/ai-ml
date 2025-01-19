Facial Recognition
---

- It uses algorithms to locate and analyze human faces in images or video content.
- It involves identifying regions of an image that contain a human face, typically by returning bounding box coordinates that form a rectangle around the face.

# Get started with facial analysis on Azure

Azure provides multiple Azure AI services that you can use to detect and analyze faces, including:

- Azure AI Vision
    - It offers face detection and some basic face analysis, such as returning the bounding box coordinates around an image.
- Azure AI Video Indexer
    - Used to detect and identify faces in a video.
- Azure AI Face
    - It offers pre-built algorithms that can detect, recognize, and analyze faces.

## Azure AI Face Service

- It can return the rectangle coordinates for any human faces that are found in an image, as well as a series of related attributes:
    - Accessories
    - Blur
    - Exposure
    - Glasses
    - Head pose
    - Mask
    - Noise
    - Occlusion
    - Quality For Recognition

# Azure resources for Face

## Face

- Use this specific resource type if you don't intend to use any other Azure AI services, or if you want to track utilization and costs for Face separately.

## Azure AI services

- A general resource that includes Azure AI Face along with many other Azure AI services such as Azure AI Content Safety, Azure AI Language, and others. Use this resource type if you plan to use multiple Azure AI services and want to simplify administration and development.


