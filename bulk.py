import boto3
import json
import decimal
 
client = boto3.client('dynamodb')
 
with open("movie.json") as json_file:
    jq = json.load(json_file, parse_float = decimal.Decimal)
 
# print jq
 
for i in jq:
    air_date = i['air_date']
    answer = i['answer']
    category = i['category']
    question = i['question']
    rounds = i['round']
    show_number = i['show_number']
    value = i['value']
    if value is None:
        value = 'Null input'
        print(value)
    else:
        print(value)
    client.put_record(
        DeliveryStreamName='myDSRS',
        Record={
            "Data": air_date,
            "Data": answer,
            "Data": category,
            "Data": question,
            "Data": rounds,
            "Data": show_number,
            "Data": value
        }
    )
    print ( "Adding Jeoperdy answer:", air_date, answer, category, question, rounds, show_number, value)
 
