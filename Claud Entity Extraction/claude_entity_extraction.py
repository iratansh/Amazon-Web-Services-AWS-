import json
import os
import sys
import boto3
import botocore
from langchain.llms.bedrock import Bedrock
from pathlib import Path
from bs4 import BeautifulSoup

boto3_bedrock = boto3.client('bedrock-runtime')

llm = Bedrock(
    model_id="anthropic.claude-v2",
    client=boto3_bedrock,
    model_kwargs={
        "max_tokens_to_sample": 200,
        "temperature": 0, # Using 0 to get reproducible results
        "stop_sequences": ["\n\nHuman:"]
    }
)

emails_dir = Path(".") / "emails"
with open(emails_dir / "00_treasure_island.txt") as f:
    book_question_email = f.read()

print(book_question_email)

query = f"""

Human: Given the email inside triple-backticks, please read it and analyse the contents.
If a name of a book is mentioned, return it, otherwise return nothing.

Email: ```
{book_question_email}
```

Assistant:"""

result = llm(query)
print(result.strip())

prompt = """

Human: Given the email provided, please read it and analyse the contents.
If a name of a book is mentioned, return it.
If no name is mentioned, return empty string.
The email will be given between <email></email> XML tags.

<email>
{email}
</email>

Return the name of the book between <book></book> XML tags.

Assistant:"""

query = prompt.format(email=book_question_email)
result = llm(query)
print(result.strip())

def extract_by_tag(response: str, tag: str, extract_all=False) -> str | list[str] | None:
    soup = BeautifulSoup(response)
    results = soup.find_all(tag)
    if not results:
        return
        
    texts = [res.get_text() for res in results]
    if extract_all:
        return texts
    return texts[-1]

with open(emails_dir / "01_return.txt") as f:
    return_email = f.read()

print(return_email)
print(extract_by_tag(result, "book"))


query = prompt.format(email=return_email)
result = llm(query)
print(result.strip())

print(extract_by_tag(result, "question", extract_all=True))
print(extract_by_tag(result, "name"))
print(extract_by_tag(result, "book", extract_all=True))