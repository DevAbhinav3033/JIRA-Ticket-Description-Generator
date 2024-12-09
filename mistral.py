import boto3
import json

def lambda_handler(event, context):
    # Extract JIRA ticket header from the event
    jira_ticket_header = event.get('jira_ticket_header', '')

    if not jira_ticket_header:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing jira_ticket_header in request'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    # Define the prompt data
    prompt_data = """
    Write a description for the JIRA ticket below:
    """

    # Initialize the boto3 client
    bedrock = boto3.client(service_name="bedrock-runtime")

    # Create the payload
    payload = {
        "prompt": "<s>[INST]" + prompt_data + jira_ticket_header + "[/INST]",
        "max_tokens": 512,
        "temperature": 0.8,
        "top_p": 0.8,
        "top_k": 50
    }
    body = json.dumps(payload)
    model_id = "mistral.mistral-7b-instruct-v0:2"

    # Invoke the model
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json",
    )

    # Parse the response
    response_body = json.loads(response.get("body").read())
    response_text = response_body.get("outputs")[0].get("text")

    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps({'description': response_text}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }