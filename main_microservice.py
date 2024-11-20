# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:17:14 2024

@author: I552743
"""
import requests
import json
import os
from flask import Flask, jsonify, url_for
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
import shipping_microservice
import notification_microservice
    
global mail
mail = False
    
print("welcome")

try:
    if __name__ == "__main__":
        app.run(debug=True, host="", port=port)
        
    url1 = url_for('calculate_shipping_cost',weight=2, distance=100, carrier ="bluedart" )
    print(url1)  # Output: /user/Alice/30   
    response1 = requests.get(url1)
    print(response1.text) 
    
    url2 = url_for('generate_shipping_label',weight=7, address="dDummy", carrier = "aws")
    print(url2)  # Output: /user/Alice/30  
    response2 = requests.get(url2)
    print(response2.text) 
    
    if(url2):
        mail = True
        url4 = url_for('send_email')
        print(url4)
        response4 = requests.get(url4)
        print(response4.text) 
        
    
    url3 = url_for('calculate_shipping_cost',shipment="1ZBE23456789012345", carrier="fedex", flag=True)
    print(url3)  # Output: /user/Alice/30 
    response3 = requests.get(url3)
    print(response3.text) 
 
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")