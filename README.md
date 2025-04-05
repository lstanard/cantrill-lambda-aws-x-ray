# learn.cantrill.io Lambda & AWS X-Ray Demo

[Original demo lesson notes](https://github.com/acantril/learn-cantrill-io-labs/tree/master/00-aws-simple-demos/aws-lambda-xray)

This is an updated version of the Lambda & AWS X-Ray Demo for the learn.cantrill.io AWS Certified Developer Associate exam training course. The API for the AWS X-Ray SDK and S3 clients have changed an the original demo lesson no longer works. This is an updated and working version for 2025.

## Requirements

* Python 3.9 (recommend installing with pyenv)
* pip

## Instructions

This repo contains a bash script which can be used to automatically install dependencies and bundle the code into a ZIP file which can be uploaded to AWS Lambda.

From the command line, run:
```
$ ./package.sh
```

Which will create `lambda_function_bundle.zip`.
