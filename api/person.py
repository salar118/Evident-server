import json
import boto3


def getAllPersons(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Evident')

    table.put_item(
        Item={
            'id': 'kdk1',
            'last_name': 'assswwb',
            'name': 'salar'
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "all the persons in evident",
            # "location": ip.text.replace("\n", "")
        }),
    }


def getPersonById(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "get person by id in evident",
            # "location": ip.text.replace("\n", "")
        }),
    }
