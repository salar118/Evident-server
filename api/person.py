import boto3
import json
import os

from utilities.DecimalEncoder import DecimalEncoder

TABLE_NAME = os.environ['TABLE_NAME']
RESOURCE_TYPE = os.environ['RESOURCE_TYPE']

dynamodb = boto3.resource(RESOURCE_TYPE)
table = dynamodb.Table(TABLE_NAME)


def getAllPersons(event, context):
    response = table.scan()
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET"
        },
        "body":     json.dumps(response, indent=4, cls=DecimalEncoder)
    }


def getPersonById(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "get person by id in evident",
            # "location": ip.text.replace("\n", "")
        }),
    }
