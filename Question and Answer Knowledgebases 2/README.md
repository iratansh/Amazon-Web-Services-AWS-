This Python script utilizes AWS Bedrock to retrieve and generate answers based on a query about Amazon's activities in generative AI. It uses both bedrock-agent-runtime for retrieval and bedrock-runtime for text generation, integrating multiple language models to generate accurate and context-aware responses.

Technologies Used:
* Python Standard Libraries: json, pprint
* AWS Boto3: For connecting to AWS services and invoking Bedrock models
* LangChain: For handling interactions with Bedrock language models

Functionality:
* Setup AWS Bedrock Clients: Initializes clients for Bedrock and Bedrock Agent with custom configurations.
* Define Query and Knowledge Base ID: Sets up the input query and knowledge base ID for retrieving relevant information.
* Retrieve Contextual Information: Uses Bedrock Agent to retrieve relevant documents based on the query.
* Generate Response: Uses Bedrock language models to generate a response based on the retrieved information.
* Print Results: Outputs the retrieved contexts and the generated response.

