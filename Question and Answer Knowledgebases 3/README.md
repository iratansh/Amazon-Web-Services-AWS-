This Python script leverages AWS Bedrock and LangChain to retrieve and generate answers about Amazon's activities in generative AI. It uses the Bedrock Chat API and a retrieval system to fetch relevant documents and generate responses.

Technologies Used:
* Python Standard Libraries: json, pprint
* AWS Boto3: For connecting to AWS services and invoking Bedrock models
* LangChain: For managing language model interactions and prompt templates

Functionality:
* Setup AWS Bedrock Clients: Initializes clients for Bedrock and Bedrock Agent with custom configurations.
* Define Query and Knowledge Base ID: Sets up the input query and knowledge base ID for retrieving relevant information.
* Retrieve Contextual Information: Uses Bedrock Agent to retrieve relevant documents based on the query.
* Prepare and Invoke Model: Uses the Bedrock Chat API to generate a response based on the retrieved contexts and defined prompt.
* Print Results: Outputs the retrieved contexts and the generated response.
* LangChain Integration: Uses LangChain's RetrievalQA to combine retrieval and language model capabilities for more refined responses.
