import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

# Create the DynamoDB table.
response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
	{
	    'AttributeName': 'role',
	    'AttributeType': 'S'
	},
	{
	    'AttributeName': 'origin',
	    'AttributeType': 'S'
	}
    ],
    TableName='single',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'
        },
	{
            'AttributeName': 'role',
            'AttributeType': 'RANGE'
        }
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'lsi',
            'KeySchema': [
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                },
		{
		    'AttributeName': 'role',
     		    'KeyType' : 'RANGE'
		}
            ],
            'Projection': {
                'ProjectionType': 'ALL',
            }
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
)
