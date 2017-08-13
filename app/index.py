
from __future__ import print_function
import boto3
import json

lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
	eve = {}
	eve['request']={}
	eve['request']['locale'] = "de-DE"
	invoke_response = lambda_client.invoke(FunctionName="myiss", InvocationType='RequestResponse', Payload=json.dumps(eve))
	data = invoke_response['Payload'].read()
	ret = json.loads(data)
	text = (ret['response'][u'outputSpeech'][u'text'])
	print(text)
	if "ISS" not in text:
		notify()
	#data()



def notify():
	client = boto3.client('sns')
	response = client.publish(
	    TargetArn="arn:aws:sns:eu-west-1:857162644792:alertISS",
	    Message="The ISS test on eu-west-1 lambda did not succeed",
	    MessageStructure='string'
	)





def data():
	from boto import dynamodb2
	from boto.dynamodb2.table import Table

	TABLE_NAME = "issdata"
	REGION = "us-west-1"

	conn = dynamodb2.connect_to_region(
	    REGION,
	    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
	    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
	)
	table = Table(
	    TABLE_NAME,
	    connection=conn
	)


	absolute_junk = {
    "favorite_color": "blue",
    "quest": "seek_holy_grail",
}


	with table.batch_write() as table_batch:
	    for example_counter in xrange(10):

	        required_hash_data = {
	            "user_id": 11,
	            "timestamp": datetime_to_timestamp_ms(datetime.datetime.utcnow())
	        }

	        final_dynamo_data = dict(absolute_junk.items() + required_hash_data.items())
	        table_batch.put_item(data=final_dynamo_data)
	        