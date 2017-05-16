from __future__ import print_function
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
'''
    This lambda function is for POST request using API gateway enpoint.
    Author:Priyanka Pednekar
    
    '''
print('Loading function')

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    
    table1 = dynamodb.Table('Order')
    
    order_id = event['order_id']
    menu_id =event['menu_id']
    customer_name=event['customer_name']
    customer_email=event['customer_email']
    
    response = table1.put_item(
                               Item={
                               'order_id': order_id,
                               'menu_id': menu_id,
                               "customer_name": customer_name,
                               "customer_email": customer_email,
                               "order_info":{}
                               }
                               )
        
        
                               message= 'Hi {} , please choose one of these selection: '.format(customer_name)
                               
                               
                               table2 = dynamodb.Table('Menu')
                               
                               
                               response2 = table2.get_item(
                                                           Key={
                                                           'menu_id': 'pizza4'
                                                           }
                                                           )
                               '''
                                   item = response2['Item']  
                                   selection = ' '.join(item['selection'])
                                   
                                   
                                   for x in item['selection']: 
                                   message+=' .{},'.format(x)
                                   '''
                               item = response2['Item']
                               dict1 = {}
                               
                               i=1
                               for x in item['selection']: 
                                   #message+=' .{},'.format(x)
                                   dict1[i]=x
                                       i+=1
                                   

for j in dict1:
    message+='{}.{}, '.format(j,dict1[j])
    
    
    return { 
        'message' : message
        }
