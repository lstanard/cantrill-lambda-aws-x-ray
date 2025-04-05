import io # python standard library
import os # python standard library
import base64 # python standard library
import mimetypes # python standard library
import boto3 # available in Lambda
import requests
import aws_xray_sdk.core

from aws_xray_sdk.core import patch_all
patch_all()

def lambda_handler(event, context):
    with aws_xray_sdk.core.xray_recorder.capture('get_dog_images'):
        # Create an S3 client
        session = boto3.session.Session()
        s3 = session.client('s3')
        bucket_name = os.getenv('BUCKET_NAME')

        with aws_xray_sdk.core.xray_recorder.capture('call_dog_api'):
            endpoint = 'https://dog.ceo/api/breeds/image/random'
            response = requests.get(endpoint)
            image_url = response.json()['message']
            image_name = str(response.json()['message']).split('/')[-1]
            image = requests.get(image_url, stream=True).content

        with aws_xray_sdk.core.xray_recorder.capture('save_dog_to_s3'):
            contenttype = mimetypes.types_map['.' + image_name.split('.')[-1]]
            s3.upload_fileobj(io.BytesIO(image), bucket_name, image_name, ExtraArgs={'ContentType': contenttype})

    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/jpeg'
        },
        'body': base64.b64encode(image),
        'isBase64Encoded': True
    }
    return response

