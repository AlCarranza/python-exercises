"""
Deployment is the phase where the model is made available for use in production. 
This phase involves setting up the necessary infrastructure, monitoring, and maintenance to ensure that the model performs well in real-world scenarios.

    * No one-size-fits-all solution: The deployment phase is highly dependent on the specific use case, 
        model architecture, and infrastructure requirements. Different models may require different deployment strategies, such as containerization, serverless deployment, or edge deployment.
    * An application may include a chain/agent logic, vector, database, LLM, and other components. 
        The deployment phase should consider the entire application architecture and ensure that all components work together seamlessly.
    * Each component needs to be deployed and work together. For example, if the application includes a vector database, it should be deployed and configured to work with the LLM and other components.
"""

"""
Step 1: Choice of hosting
    * Private or public cloud or on-premise hosting: The choice of hosting depends on factors such as data privacy, security, scalability, and cost. Private cloud or on-premise hosting may be preferred 
        for sensitive data, while public cloud hosting may offer better scalability and cost-effectiveness.
    * Many cloud providers offer solutions for LLM hosting and deployment, such as AWS SageMaker, Azure Machine Learning, and Google AI Platform. These platforms provide tools for model deployment, monitoring, and scaling.

Step 2: API design
    * APIs let different software talk to each other. In the context of LLM deployment, APIs allow applications to interact with the model and access its capabilities.
    * Design affects scalability, cost and infrastructure needs. A well-designed API can improve performance, reduce latency, and optimize resource usage. Consider factors such as request/response formats, authentication, rate limiting, and error handling when designing the API.
    * Security is crucial, controlled with API keys, OAuth, or other authentication methods. Ensure that only authorized users can access the model and its capabilities.

Step 3: How to run
    * Options:
        1. Containers
        2. Serverless functions
        3. Cloud managed services
    * Each option has its own advantages and trade-offs. Containers provide flexibility and portability, serverless functions offer scalability and cost-efficiency, and cloud managed services simplify deployment and management.
"""

"""
CI/CD (Continuous Integration/Continuous Deployment) is a set of practices that enable teams to deliver code changes more frequently and reliably. In the context of LLM deployment, CI/CD can help automate the process of building, testing, and deploying models.
    * Continuous Integration (CI):
        1. Source: Retrieve source code from a version control system (e.g., Git).
        2. Build: Create a container image containing the code.
        3. Test: Perform integration tests to ensure that the model works as expected.
        4. Register: Store the container in a resgitry.
    * Continuous Deployment (CD):
        1. Retrieve: Pull the container image from the registry.
        2. Test: Perfor, the deployment tests to ensure that the model works as expected in the production environment.
        3. Deploy: Deploy container to enviroments:
            - Staging: A pre-production environment where the model can be tested with real-world data and scenarios.
            - Production: The live environment where the model is made available to end-users.
"""

"""
Scaling
    * LLMs might need specialized GPU hardware.
    * Scaling strategies:
        1. Horizontal scaling: Add more instances of the model to handle increased load. This can be achieved by deploying multiple containers or serverless functions.
        2. Vertical scaling: Increase the resources (CPU, memory, GPU) of a single instance to handle increased load. This may involve upgrading the hardware or using more powerful cloud instances.
        3. Auto-scaling: Automatically adjust the number of instances based on demand. This can help optimize resource usage and reduce costs.
    * Horizontal for traffic, vertical for reliability and speed.
"""
