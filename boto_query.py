import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('movieauto')

from boto3.dynamodb.conditions import Key, Attr
response = table.query(
    KeyConditionExpression=Key('title').eq('Lifeboat')
)
items = response['Items']
print(items)
