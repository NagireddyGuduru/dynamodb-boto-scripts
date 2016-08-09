import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('movieauto')

response = table.get_item(
    Key={
        'year': '2013',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)
