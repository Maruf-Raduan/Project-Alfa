# Cloud Deployment Guide

## Option 1: AWS Lambda + API Gateway (Recommended)

### Quick Deploy
```bash
# 1. Create stack
aws cloudformation create-stack \
    --stack-name java-assistant \
    --template-body file://cloudformation.yaml \
    --capabilities CAPABILITY_IAM

# 2. Get API URL
aws cloudformation describe-stacks \
    --stack-name java-assistant \
    --query 'Stacks[0].Outputs'

# 3. Package and deploy code
chmod +x deploy.sh
./deploy.sh

# 4. Update index.html with your API URL
# 5. Upload to S3
```

### Manual Steps
1. Create Lambda function (Python 3.11)
2. Upload `function.zip` (lambda_handler.py + java_learning_assistant.py)
3. Create API Gateway HTTP API
4. Add POST route `/chat` → Lambda
5. Enable CORS
6. Host `index.html` on S3 or CloudFront

## Option 2: Docker + AWS ECS/Fargate

```bash
docker build -t java-assistant .
docker run -p 8080:8080 java-assistant
```

## Option 3: Heroku

```bash
git init
heroku create java-learning-assistant
git push heroku main
```

## Costs (AWS)
- Lambda: Free tier 1M requests/month
- API Gateway: $1/million requests
- S3: $0.023/GB/month
- **Estimated: ~$0-5/month for low traffic**
