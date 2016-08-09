import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
