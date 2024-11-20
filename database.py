# importing module 
from pymongo import MongoClient 
  
try:
    # creation of MongoClient 
    client=MongoClient() 
    
    # Connect with the portnumber and host 
    client = MongoClient("mongodb://localhost:27017/") 

    print("Connected")
except Exception as e:
    print(f"Error: {e}")
    
try:
    mydb = client["shipping_microservice"]
    print(mydb)
    
    def create_table_add(ship_dict):
        c_names = mydb.list_collection_names()
        c = "shippingcost"
        if c not in c_names:
            mycol = mydb.create_collection("shippingcost")  
        a = mydb.collection.insert_one(ship_dict)
        print("inserted", a.inserted_id)
        
        
    def label_table_add(ship_dict1):
        c_names = mydb.list_collection_names()
        c = "GenerateLabel"
        if c not in c_names:
            mycol = mydb["GenerateLabel"]
        a = mydb.collection.insert_one(ship_dict1)
        print("inserted", a.inserted_id)
        
    def track_table_add_update(ship_dict2):
        c_names = mydb.list_collection_names()
        c = "Trackship"
        if c in c_names:
            mycol = mydb["Trackship"]
            
        # Find if a product with the same product_code exists
        existing_shipment = mydb.collection.find_one({"shipment": ship_dict2["shipment"]})

        if existing_shipment:
            # Update the existing product's existing_value
            result = mydb.collection.update_one(
                {"shipment": ship_dict2["shipment"]},
                {"$set": {"Delivery": ship_dict2["Delivery"]}}
            )
            print(f"Updated {result.modified_count} document(s)")
        else:
            # Insert the new product
            result = mydb.collection.insert_one(ship_dict2)
            print(f"Inserted new product with ID: {result.inserted_id}")
        
    
except Exception as e:
    print(f"Error: {e}")
    
