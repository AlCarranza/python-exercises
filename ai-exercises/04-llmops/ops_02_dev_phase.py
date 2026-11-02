"""
Development Phase
    - Is the phase to develop and improve the application.

"""

"""
1. Prompt Engineering
    - Improve performance
    - Control over output
    - Avoid byass and hallicunations

    Anathomy of a prompt
        - Instructions
        - Examples / Context
        - Input data
        - Output indicator
    
    Finding the appropiate prompt
        - LLM settings, such as temperature, max tokens
        - In context learning and other prompt design patterns
    
    After we create a prompt we need,
    Prompt Managment
        - Crucial for efficiency, reproducibility and collaboration
        - Important to track
            * Prompt
            * Output
            * Model and settings
        - Use prompt manager version control
        - Begin creating a collection of good input/output pairs for evaluation
        - Make use of prompt templates for reusability
"""

"""
2. Chains and Agents
    - Chain also known as a pipeline or flow consist on connect the steps to receive the 
    inputs and provide the outputs

    Chains are crucial as:
        * Develop sophisticated applications
        * Establish a modular design, enhancing scalability and operational efficiency
        * Unlock endless posibilities for customization
    
    - Agents consist on:
        * Multiple actions or tools
        * An LLM deciding which action to take

        Useful when:
            - There are many actions
            - The optimal sequence of steps is unknown
            - We are uncertain about the inputs

    - Differences between chains and agents
        * Nature: Chains are deterministic; Agents adaptive
        * Complexity: Chains are simpler; Agents have more complex behavior
        * Flexibility: Chains are less flexible; Agents adjust to diverse inputs
        * Risk: Chains are less risky due to predictability; Agents might execute unpredictable actions resulting in unpredictable outcomes
"""

"""
Retrieve Argumented Generation (RAG)
    - Combine LLMs reasoning capabilities with external knowledge
    - Three steps in a chain
        1. Retrieve related documents
        2. Argument prompt with examples
        3. Generate output
    - Often implemented using vector databases

    1. Retrieve:
        * Generate embedding from input
        * Search vector database
        * Retrieve most similar documents
    2. Argument:
        * Combine input with top-k documents and create augmented prompt
    3. Generate:
        * Uses prompt to create an output

    Many implementation choices and embedding models
"""

"""
Fine-tuning
    - Adjusts the LLMs weights
    - Expand to specific tasks and domains:
        * Different languages
        * Specialized fields

There are two approaches to fine-tuning

    1. Supervised fine-tuning (transfer learning)
        - Demonstration data needed (inputs with desired outputs)
        - The approach is re-train (parts of) the model
    2. Reinforcement Learning from Human Feedback (RLHF)
        - Type of data needed is rankings or quality scores (obtained from likes and dislikes)
        - Optimize original LLM to maximize this

"""

"""
RAG vs fine-tuning

    RAG
        * Use when including factual knowledge
        * Keeps capabilities of LLM, easy to implement, always up-to-date
        * Adds extra components, requires careful engineering
    Fine-tuning
        * Use when specializing in new domain
        * Full control and no extra components
        * Needs labeled data & specialized knowledge, bias amplification, catastrophic forgetting
"""