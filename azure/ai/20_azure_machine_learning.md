Azure Machine Learning
---

# Introduction

- A cloud service for `training, deploying, and managing` machine learning models.
- Designed to be used by data scientists, software engineers, devops professionals, and others to manage the end-to-end lifecycle of machine learning projects.
- Supported projects:
    - Exploring data and preparing it for modeling.
    - Training and evaluating machine learning models.
    - Registering and managing trained models.
    - Deploying trained models for use by applications and services.
    - Reviewing and applying responsible AI principles and practices.

## Fature & Capabilities

- Centralized storage and management of datasets
- On-demand compute`
- Automated machine learning (AutoML)
- Visual Tools to define orchestrated pipelines
- Integration with common machine learning frameworks
- Built-in support for visualizing and evaluating metrics

## Provisioning Azure Machine Learning Resources

The primary resource required for Azure Machine Learning is an `Azure Machine Learning workspace`. Other supporting resources, including storage accounts, container registries, virtual machines, and others are created automatically as needed.

## Azure Machine Learning studio

- A browser-based portal for managing your machine learning resources and jobs.

## Azure AI Services

### Create Azure AI service resources

- Azure AI services are `cloud-based`.

#### AI Service Resources Types

Your development requirements and how you want costs to be billed determine the types of resources you need.

##### Multi-service resource

- A resource created in the Azure portal that `provides access to multiple Azure AI services with a single key and endpoint`.
- Use the resource Azure AI services when you need several AI services or are `exploring AI capabilities`.
- When you use an Azure AI services resource, all your AI services are `billed together`.
- Resource: `Azure AI Services`

##### Single-service resources

- A resource created in the Azure portal that `provides access to a single Azure AI service`, such as Speech, Vision, Language, etc.
- Each Azure AI service has a `unique key and endpoint`.
- These resources might be used when you `only require one AI service` or want to see `cost information separately`.
- Resource: Individual service like Face, Language, Content Saftey etc.

### Use Azure AI services

You can use Azure AI services using:
- REST API
- SDK
- Visual Studio 

#### Using service studio interfaces

- Studio interfaces provide a `friendly user interface` to explore Azure AI services.
- There are different studios for different Azure AI services
    - Vision Studio
    - Language Studio
    - Speech Studio
    - Content Safety Studio
- You can test out Azure AI services using the samples provided, or experiment with your own content.
- A studio-based approach allows you to explore, demo, and evaluate Azure AI services regardless of your experience with AI or coding.

##### Associate the AI service resource

- `Associate the service with the studio` to use the service.

### Understand authentication for Azure AI services

#### REST APIs

- Most Azure AI services are accessed through a `RESTful API`.
- The API defines what information is passed between two software components: the Azure AI service and whatever is using it.
- Part of what an API does is to handle authentication.
- This authentication process uses an endpoint and a resource key.
- The endpoint describes how to reach the AI service resource instance that you want to use.
When you use a studio interface with Azure AI services, your credentials are authenticated when you sign in, and a similar process is happening in the background.
- When you use a studio interface with Azure AI services, your credentials are authenticated when you sign in, and a similar process is happening in the background.


