#!/bin/bash

# Package Lambda function
zip -r function.zip lambda_handler.py java_learning_assistant.py

# Deploy to AWS Lambda (replace with your function name)
aws lambda update-function-code \
    --function-name JavaLearningAssistant \
    --zip-file fileb://function.zip

# Upload web interface to S3 (replace with your bucket name)
aws s3 cp index.html s3://your-bucket-name/ --acl public-read

echo "Deployment complete!"
