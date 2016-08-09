import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')
table.put_item(
   Item={
        'username': 'senthil',
        'first_name': 'sen',
        'last_name': 'pal',
        'age': 37,
        'account_type': 'standard_user',
    }
)
