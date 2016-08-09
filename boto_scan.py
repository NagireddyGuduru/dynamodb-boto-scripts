import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('movieauto')

from boto3.dynamodb.conditions import Key, Attr
response = table.scan()
items = response['Items']
print(items)
