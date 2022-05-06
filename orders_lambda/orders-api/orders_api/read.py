import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')


def lambda_handler(event, context):
    #(1)
    # order = {
    #     'id': 147,
    #     'name': 'item 1',
    #     'quantity': 5,
    # }
    # return{
    #     'statusCode': 200,
    #     'headers': {},
    #     'body': json.dumps(order)
    # }
    
    #(3)
    table = dynamodb.Table(table_name)
    order_id = int(event['pathParameters']['id'])
    response = table.query(KeyConditionExpression=Key('id').eq(order_id))
    return{
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }