from __future__ import print_function
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
import time
import datetime

'''
    This lambda function is for PUT request using API gateway enpoint.
    Author:Priyanka Pednekar
    
    '''

print('Loading function')

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    
    table1 = dynamodb.Table('Order')
    table2 = dynamodb.Table('Menu')
    
    response1 = table1.get_item(
                                Key={
                                'order_id': event['order_id']
                                }
                                )
        
                                item1 = response1['Item']
                                
                                
                                #current date and time
                                date_format='%m-%d-%Y@%H:%M:%S'
                                now = datetime.datetime.now()
                                date_val='{}'.format(now.strftime(date_format))
                                
                                try:
                                    arg=item1['order_status']
                                except:
                                    arg=''
                                        
                                        
                                        if (arg==''):
                                            message= 'Which size do you want? '
                                                response2 = table2.get_item(
                                                                            Key={
                                                                            'menu_id': 'pizza4'
                                                                            }
                                                                            )
                                                    
                                                    #for posting message
                                                    item = response2['Item']
                                                        dict1 = {}
                                                            
                                                            i=1
                                                                for x in item['size']:
                                                                    dict1[i]=x
                                                                        i+=1
                                                                            
                                                                            
                                                                            for j in dict1:
                                                                                message+='{}.{}, '.format(j,dict1[j])
                                                                                    
                                                                                    
                                                                                    #for updating table
                                                                                    dict2={}
                                                                                        i=1
                                                                                            for x in item['selection']:
                                                                                                dict2[i]=x
                                                                                                    i+=1
                                                                                                        
                                                                                                        
                                                                                                        val=int(event['body'])
                                                                                                            
                                                                                                            update_selection_value='{}'.format(dict2[val])
                                                                                                                
                                                                                                                response3 = table1.update_item(
                                                                                                                                               Key={
                                                                                                                                               'order_id': event['order_id']
                                                                                                                                               },
                                                                                                                                               UpdateExpression="set order_status=:b, order_info.selection=:a, order_info.order_time=:c",
                                                                                                                                               ExpressionAttributeValues={
                                                                                                                                               ':b': "processing",
                                                                                                                                               ':a': update_selection_value,
                                                                                                                                               ':c': date_val
                                                                                                                                               },
                                                                                                                                               ReturnValues="UPDATED_NEW"
                                                                                                                                               )
                                                                                                                    else:
                                                                                                                        message= 'Your order costs '
                                                                                                                            response2 = table2.get_item(  
                                                                                                                                                        Key={
                                                                                                                                                        'menu_id': 'pizza4'
                                                                                                                                                        }
                                                                                                                                                        )
                                                                                                                                
                                                                                                                                #for posting message
                                                                                                                                item = response2['Item']
                                                                                                                                    dict1 = {}
                                                                                                                                        
                                                                                                                                        i=1
                                                                                                                                            for x in item['price']:
                                                                                                                                                dict1[i]=x
                                                                                                                                                    i+=1
                                                                                                                                                        
                                                                                                                                                        j=1
                                                                                                                                                            price='{}'.format(dict1[j])
                                                                                                                                                                message+=price
                                                                                                                                                                    
                                                                                                                                                                    
                                                                                                                                                                    #for updating table
                                                                                                                                                                    dict2={}
                                                                                                                                                                        i=1
                                                                                                                                                                            for x in item['size']: 
                                                                                                                                                                                dict2[i]=x
                                                                                                                                                                                    i+=1
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                        val=int(event['body'])
                                                                                                                                                                                            
                                                                                                                                                                                            update_size_value='{}'.format(dict2[val])
                                                                                                                                                                                                
                                                                                                                                                                                                
                                                                                                                                                                                                response3 = table1.update_item(
                                                                                                                                                                                                                               Key={
                                                                                                                                                                                                                               'order_id': event['order_id']
                                                                                                                                                                                                                               },
                                                                                                                                                                                                                               UpdateExpression="set order_status=:b, order_info.size=:a, order_info.order_time=:c, order_info.costs=:d",
                                                                                                                                                                                                                               ExpressionAttributeValues={
                                                                                                                                                                                                                               ':b': "processing",
                                                                                                                                                                                                                               ':a': update_size_value,
                                                                                                                                                                                                                               ':c': date_val,
                                                                                                                                                                                                                               ':d': price
                                                                                                                                                                                                                               },
                                                                                                                                                                                                                               ReturnValues="UPDATED_NEW"
                                                                                                                                                                                                                               )
                                                                                                                                                                                                    
                                                                                                                                                                                                    message+= '. We will email you when the order is ready. Thank you!'
                                                                                                                                                                                                        
                                                                                                                                                                                                        return { 
                                                                                                                                                                                                            'message' : message
                                                                                                                                                                                                            }
