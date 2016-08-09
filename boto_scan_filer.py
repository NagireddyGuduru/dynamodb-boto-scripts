import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('movieauto')

from boto3.dynamodb.conditions import Key, Attr

response = table.scan(
    FilterExpression=Attr('title').begins_with('L') & Attr('year').eq('1944')
)
items = response['Items']
print(items)
