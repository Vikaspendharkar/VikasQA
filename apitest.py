import requests
import json
import time
import datetime
import random
import csv

		
pstapi = requests.post('https://api.omniparcel.com/ratesqueryv1/availablerates',
headers={"Content-Type" : "application/json", "access_key" : "2CE65CF79145B4F946928266284319CBE2C6A86E4675F7C79F"},
   		json={
      "Origin":{
      "Name":"Omni Test",
      "ContactPerson":"Omni User",
      "phonenumber":"123456789",
      "email":"sstech.vikas@yopmail.com",
      "Address":{
         "BuildingName":"AVENU BUILD",
            "StreetAddress":"PARK LAND STREET",
            "Suburb":"Carson",
            "City":"California",
            "PostCode":"90745",
            "CountryCode":"US"
      }
      },
      "Destination":{
         "Id":0,
         "Name":"TEST RECEIVER * DO NOT PRINT *",
         "ContactPerson":"",
         "PhoneNumber":"9825098250",
         "Email":"sstech.vikas@gmail.com",
         "DeliveryInstructions":"",
         "CostCentreName":"OMNI TEST ACCOUNT",
         "Address":{
         "BuildingName":"AVENU BUILD",
            "StreetAddress":"PARK LAND STREET",
            "Suburb":"Carson",
            "City":"California",
            "PostCode":"90745",
            "CountryCode":"US"
         }
      },"Commodities": [
        {
            "Description": "abc",
            "Units": "1",
            "UnitValue": 1,
            "UnitKg": 1,
            "Currency": "NZD"
            }
        ],
      "Packages":[
         {
            "Height":"1",
            "Width":"1",
            "Kg":1,
            "Length":"1"
         }
      ],
      "PrintToPrinter":False,
      "CarrierLogo":True,
      "Outputs":[
         "LABEL_PNG_100X150"
      ],
      "Carrier":"",
      "Service":"",
      "SendTrackingEmail":False,
      "ShipType":"OUTBOUND",
      "IncludeLineDetails":True,
      "DeliveryReference":"",
      "Reference2":"",
      "Reference3":"",
      "IsSignatureRequired":False,
      "IsSaturdayDelivery":False,
      "DutiesAndTaxesByReceiver":False
      }
            )


abc = (pstapi.json())
print(abc)
                        
         