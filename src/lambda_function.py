import json
from jobs import get_jobs
from bedrock import summarize_jobs

def lambda_handler(event, context):
    jobs = get_jobs()

    summary = summarize_jobs(jobs)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "jobs": jobs,
            "summary": summary
        })
    }