# Use an official AWS Lambda base image for Python
FROM public.ecr.aws/lambda/python:3.12

# Copy function code and any necessary files to the container
COPY Python/ ${LAMBDA_TASK_ROOT}/

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

# Command to run your Lambda function
CMD ["lambda_function.lambda_handler"]
