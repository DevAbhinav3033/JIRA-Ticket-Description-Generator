
# JIRA Ticket Description Generator 

This project involves creating an AWS Lambda function that processes POST requests from an API Gateway. The function extracts a JIRA ticket header from the request, generates a description using a machine learning model hosted on AWS Bedrock, and returns the generated description as the response.


## Features

- **AWS Lambda**: Serverless function to handle incoming requests and generate descriptions.
- **API Gateway**: RESTful API endpoint to invoke the Lambda function.
- **AWS Bedrock**: Machine learning model (`mistral.mistral-7b-instruct-v0:2`) to generate descriptions.
- **IAM Role**: Permissions to invoke the Bedrock model.

## Setup

### Prerequisites

- AWS Account
- AWS CLI configured
- Python 3.8 or later

### Steps

1. **Clone the Repository**

    ```sh
    git clone https://github.com/DevAbhinav3033/JIRA-Ticket-Description-Generator.git
    cd jira-ticket-description-generator
    ```

2. **Create Lambda Function**

    - Go to the AWS Lambda console.
    - Create a new Lambda function.
    - Choose Python as the runtime.

3. **Set Up API Gateway**

    - Go to the API Gateway console.
    - Create a new REST API.
    - Create a new resource and method (POST).
    - Integrate the POST method with the Lambda function.
    - Deploy the API to a stage.

4. **Update IAM Role**

    - Go to the IAM console.
    - Find the role associated with your Lambda function.
    - Attach a policy with the following permissions:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "bedrock:InvokeModel",
                "Resource": "arn:aws:bedrock:us-east-1::foundation-model/mistral.mistral-7b-instruct-v0:2"
            }
        ]
    }
    ```

5. **Test the API**

    - Use a tool like Postman to send a POST request to the API Gateway endpoint.
    - Include a JSON body with the `jira_ticket_header` field.

    Example POST request body:

    ```json
    {
        "jira_ticket_header": "Implement forget password functionality for the user."
    }
    ```

## Usage

Send a POST request to the API Gateway endpoint with the following JSON body:

```json
{
    "jira_ticket_header": "Your JIRA ticket header here."
}


