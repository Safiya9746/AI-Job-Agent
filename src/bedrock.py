import boto3
import json
from config import AWS_REGION, MODEL_ID

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)

def summarize_jobs(jobs):

    prompt = f"""
You are an AI Career Coach.

Summarize these jobs into a professional morning email.

Jobs:

{json.dumps(jobs, indent=2)}

Give:
1. Short Summary
2. Top Skills
3. Career Advice
"""

    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    return response["body"].read().decode()