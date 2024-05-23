This Python script uses AWS Bedrock to generate a summary of a given text using a large language model. The script prepares the input prompt, invokes the model, and prints the generated summary. Error handling is included to manage common issues such as access denial.

Technologies Used:
* Python Standard Libraries: json, os, sys
* AWS Boto3: For connecting to AWS services and invoking Bedrock models
* Botocore: For handling AWS-specific errors

Functionality:
* Setup AWS Bedrock Client: Initializes the Bedrock client for invoking models.
* Define Prompt: Sets up the input prompt for generating a summary.
* Invoke Model: Uses the Bedrock API to invoke the model and generate a response.
* Print Results: Outputs the generated summary.
* Error Handling: Catches and handles specific AWS errors.
