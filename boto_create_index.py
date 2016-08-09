import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='bototable',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
{
   "AttributeDefinitions": [ 
      { 
         "AttributeName": "lsi-primary",
         "AttributeType": "string"
      }
   ],
   "GlobalSecondaryIndexes": [ 
      { 
         "IndexName": "lsi-index",
         "KeySchema": [ 
            { 
               "AttributeName": "lsi-primary",
               "KeyType": "string"
            }
         ],
         "Projection": { 
            "NonKeyAttributes": [ "something" ],
            "ProjectionType": "string"
         },
         "ProvisionedThroughput": { 
            "ReadCapacityUnits": 4,
            "WriteCapacityUnits": 4
         }
      }
   ]
]
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)

