Azure AI Foundry
---

- The Azure AI Foundry portal brings together capabilities to provide a single, centralized workspace within which developers can collaborate with data scientists and others to build AI solutions.
- The Azure AI Foundry portal is a web portal that brings together multiple Azure AI-related services into a single, unified development environment.
- Specifically, Azure AI Foundry combines:
    - The model catalog and prompt flow development capabilities.
    - The generative AI model deployment, testing, and custom data integration capabilities of Azure OpenAI service.
    - Integration with Azure AI Services for speech, vision, language, document intelligence, and content safety.

## How does Azure AI Foundry work

- An `AI hub` provides a collaborative workspace for AI solution development and management.
- You need at least one Azure AI hub to use the solution development features and capabilities of AI Foundry.

### AI Hub

- Can host `one or more projects`.
- Each project encapsulates the tools and assets used to create a specific AI solution.

### Associated Azure resources

- You can use Azure AI Foundry to create an Azure AI hub in the Management center, or you can create one during the process of creating a new project.
- When you do so, an AI hub resource is created in your Azure subscription in the resource group you specify.
- This resource provides a collaborative workspace for AI development.
- In addition to the core AI hub resource, other Azure resources are created to provide supporting services, like:
    - `Storage account` in which the data for your AI projects is stored securely.
    - A `Key vault` in which credentials used to access external resources and other sensitive values are secured.
    - A `Container registry` to store Docker images used by your AI solutions.
    - An `Application insights` resource to record usage and performance metrics.
    - An `Azure OpenAI Service` resource that provides generative AI models for your applications.

### When to use Azure AI Foundry

- Azure AI Foundry provides everything developers and data scientists need to develop agents and cutting-edge, market-ready, responsible generative AI applications.
- It's the go-to platform when you need to:
    - Create and manage AI projects
        - Azure AI Foundry provides a centralized hub for all your AI projects, allowing you to manage resources, collaborate with team members, and streamline your workflow.
    - Develop generative AI applications
        - If your goal is to develop applications that can generate content or build your own prompt flow, Azure AI Foundry's generative AI capabilities are essential.
    - Explore available AI models: Experiment with various AI models from OpenAI, Microsoft, Hugging Face, and more in Azure AI Foundry's model catalog.
    - Leverage Retrieval Augmented Generation (RAG)
        - For projects that require combining the power of retrieval and generation, Azure AI Foundry's RAG features enhances the quality and relevance of the generated content.
    - Monitor and evaluate AI models
        - Azure AI Foundry provides robust tools for the evaluation and monitoring of your prompt flows and AI models, ensuring that they meet the desired performance metrics.
    - Integrate with Azure services
        - When your AI applications need to work seamlessly with other Azure services, Azure AI Foundry offers easy integration, making it a versatile choice for complex, multi-faceted projects.
    - Build responsibly
        - Azure AI Foundry emphasizes the responsible use of AI, providing guidance and tools to ensure that your applications adhere to ethical standards and best practices.
