🧮 Calci App — Serverless Calculator with Jenkins, Docker & AWS SAM
📘 Overview

Calci App is a serverless calculator that performs basic arithmetic operations — addition, subtraction, and multiplication.
The project demonstrates a full CI/CD pipeline using Jenkins, Docker, and AWS SAM to automate build, test, and deployment to AWS Lambda.

⚙️ Architecture
GitHub → Jenkins → Docker → AWS SAM → AWS Lambda


Code is pushed to GitHub.

Jenkins automatically pulls the latest changes.

Docker builds and tests the application in an isolated environment.

AWS SAM packages and deploys the Lambda function using CloudFormation.

The function runs serverlessly on AWS Lambda.

🧩 Components Used
Tool	Purpose
Python	Calculator logic and Lambda handler
Pytest	Unit testing for all operations
Docker	Containerized build/test environment
Jenkins	CI/CD automation (build → test → deploy)
AWS SAM	Serverless deployment framework
AWS Lambda	Executes the calculator function
CloudFormation & S3	Stack and artifact management
🚀 Implementation Steps
1️⃣ Application Setup

Created calci.py with basic arithmetic logic and a Lambda-compatible handler.

Added unit tests using pytest.

2️⃣ Docker Setup

Wrote a Dockerfile to containerize the app for consistent builds.

Built and ran the container locally to verify functionality.

3️⃣ AWS SAM Deployment

Created template.yaml defining the Lambda function and IAM role.

Ran:

sam build --use-container
sam deploy --guided


This deployed the Lambda function and created the required AWS resources.

4️⃣ Jenkins Pipeline

Configured Jenkins with Docker and AWS credentials.

Added a Jenkinsfile with stages:

Checkout (from GitHub)

Build (Docker image)

Test (run pytest)

Deploy (using sam deploy)

Connected Jenkins and GitHub via webhook for automatic builds on each commit.

5️⃣ Validation

Verified successful Lambda deployment through AWS Console and CLI:

aws lambda invoke --function-name CalculatorFunction \
--payload '{"a":5,"b":3,"operation":"add"}' response.json
cat response.json

🧱 Use Case

This project demonstrates how modern DevOps tools can be combined to:

Automate software delivery pipelines.

Deploy and manage serverless applications efficiently.

Integrate testing, containerization, and cloud deployment seamlessly.

🧼 Cleanup

To delete all resources after testing:

aws cloudformation delete-stack --stack-name calci-stack


Also remove associated S3 buckets and IAM roles if created.

📄 Summary

Fully automated CI/CD pipeline for a serverless Python app.

Built and tested inside Docker, deployed via AWS SAM.

Showcases practical DevOps integration of GitHub → Jenkins → AWS Lambda.