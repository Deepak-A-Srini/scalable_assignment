import requests
import json
import requests
import os
from flask import Flask, jsonify, url_for
import database
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

class ShippingService:
    
    @app.route("/shipping_cost/<weight>/<distance>/<carrier>")
    def calculate_shipping_cost(weight, distance, carrier):
        shipping_cost = 0
        weight = int(weight)
        distance = int(distance)
        carrier = str(carrier)
        print(weight)
        if(carrier=="fedex"):
            shipping_cost = shipping_cost+100
        else:
            shipping_cost = shipping_cost+90
        if(weight<5):
             shipping_cost=shipping_cost+50
        else:
            shipping_cost=shipping_cost+60
        if(distance<50):
            shipping_cost = shipping_cost+50
        else:
            shipping_cost = shipping_cost+200
        
        ship_dict = {"weight":weight,"distance":distance,"carrier":carrier,"shipping_cost":shipping_cost}
        database.create_table_add(ship_dict)
        
        print(shipping_cost)
        return str(shipping_cost)
    
    @app.route("/shipping_generate_label/<weight>/<address>/<carrier>")
    def generate_shipping_label(weight, address, carrier):
        carrier = str(carrier)
        address = str(address)
        label_data = carrier[:3] + address[:3]
        
        ship_dict = {"weight":weight,"address":address,"carrier":carrier,"label_data":label_data}
        database.label_table_add(ship_dict)
        
        return label_data
    
    @app.route("/track_shipment/<tracking_number>/<carrier>/<flag>")
    def track_shipment(tracking_number, carrier, flag):
        tracking_status = "Delivered"
        if(flag):
            return tracking_status
        else:
            tracking_status = "Not Delivered"
            
        ship_dict = {"shipment":tracking_number,"carrier":carrier,"Delivery":tracking_status}
        database.track_table_add_update(ship_dict)
            
        return tracking_status

if __name__ == "__main__":
    app.run(debug=True, host="", port=port)


'''
# Example usage:

print("welcome")
#weight = 6
#distance = 100
#carrier = "fedex"

url = url_for('calculate_shipping_cost',weight=4, distance=100, carrier = "fedex" )
print(url)  # Output: /user/Alice/30   

url = url_for('generate_shipping_label',weight=6, address="123MainSt", carrier = "fedex")
print(url)  # Output: /user/Alice/30  

url = url_for('calculate_shipping_cost',shipment="1ZBE23456789012345", carrier="fedex", flag=True)
print(url)  # Output: /user/Alice/30  


#shipping_cost = ShippingService.calculate_shipping_cost(weight, distance, "fedex")
#shipping_cost.calculate_shipping_cost()
#print("Shipping cost:", shipping_cost)


shipment_details = {"weight": 2.5, "length": 10, "width": 8, "height": 6, "address": "123 Main St"}
label_data = ShippingService.generate_shipping_label(carrier, shipment_details)
#label_data.generate_shipping_label()
print("Label data:", label_data)

 
tracking_status = ShippingService.track_shipment("1ZBE23456789012345", carrier, True)
#tracking_status.track_shipment()
print("Tracking status:", tracking_status)
'''