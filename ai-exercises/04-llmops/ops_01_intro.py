"""
LLMOps Introduction
    - Helps to effectively manage, deploy and maintain large language model applications

    Recap: What are LLMs:
        - Trained on extensive text data
        - Can understand and generate human-like text
        - Represent an AI breakthrough

        - Typically pre-trained
        - Massive number of parameters
        - Significant computational resources
        - Unpredictable

    The need for LLMOps
        - Seamless integration
        - Smooth lifecycle transitions
        - Efficient, scalable management

    LLMOps vs MLOps
                    LLMOps                  MLOps
    Model size      Large                   Typically smaller
    Data            Text                    Any data
    Pre-trained     Typically yes           Typically no
        models
    Model           Prompt engineeting &    Feature engineering % model
        improvement     fine-tunning                            selecion
    Generalization  General-purpose         Fixed scope
    Unpredictability High                   Low
    Output          Primarily text          Task-specific
"""

"""
LLMOps phases: Helps to prioritize activities, allocate resources effectively, set realistic timelines,
                identify potential bottlenecks
    Ideation Phase
        - Data Sourcing
        - Base Model Selection
    Development Phase
        - Prompt Engineering: Crafting effective prompts to ensure accurate outputs
        - Chains and agents
        - RAG vs fine-tuning: Boost model's performance
        - Testing
    Operational Phase
        - Deployment
        - Monitoring & observability
        - Cost managment
        - Governance and security: Access control, measures to mitigate threats
"""

"""
Ideation phase - Understanding the business problem through data sourcing and base model selection

    - Data sourcing
        * Identifying needs
        * Finding sources
        * Ensuring accessibility

        Some questions will help us to identify the topics for data sourcing
            1. Is the data relevant?
            2. Is the data available?
                * Transform the data
                * Set up additional databases
                * Evaluate costs
                * Consider other access limitations
            3. Does the data meet standards?
                * Concerns quality and governance
        
    - Selecting the base model
        * Pre-trained models: already have been trained on significant amount of data text
        * Propietary or open-source?

        * Propietary models (privately owned):
            - Advantages:
                * Ease of set-up and use
                * Quality assurance
                * Reliability, speed and availability
            - Limitations:
                * Require exposing data
                * Customization
            - Examples:
                * ChatGPT
                * Claude 3
                * PaLM2
                * Gemini
        * Open-sourced (publicly accessible)
            - Advantages:
                * In-house hosting
                * Trasnsparency
                * Full customizability
            - Limitations:
                * Support
                * Commercial use
            - Examples:
                * Meta Llama 3

        * Factors in model selection
            1. Performance
                * Response quality
                * Speed
            2. Model Characteristics
                * Data used to train the model
                * Context window size
                * Fine-tunability
            3. Practical considerations
                * Licence
                * Cost
                * Enviromental impact
            4. Secondary factors
                * Number of parameters
                * Popularity
"""