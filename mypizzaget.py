from __future__ import print_function
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

'''
    This lambda function is for GET request using API gateway enpoint.
    Author:Priyanka Pednekar
    
    '''

print('Loading function')

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    
    table = dynamodb.Table('Order')
    
    response = table.get_item(
                              Key={
                              'order_id': event['order_id']
                              }
                              )
        
                              item = response['Item']  
                              
                              
    return item
