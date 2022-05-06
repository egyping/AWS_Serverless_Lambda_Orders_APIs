import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')


def lambda_handler(event, context):
    # (1)
    # event['body'] is json we need to deserialize using json.loads
    # order = json.loads(event['body'])
    # return{
    #     'statusCode': 201,
    #     'headers': {},
    #     'body': json.dumps({'message': 'Order Created'})
    # }
    
    # (3)
    order = json.loads(event['body'])
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=order)
    print(response)
    return{
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }