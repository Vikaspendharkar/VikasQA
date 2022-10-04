import requests
import json
import time
import datetime
import csv
import pandas
import openpyxl

number = 1
rows = []
File_path = "C:/Users/NISHITA-PC/Documents/Javascript_V/Omninet/Excel&CSV/"




File_Name = "Seko create shipment via API - Format for create shipment.csv"




with open(File_path+File_Name, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        

for row in rows[0:]:
#   print(row)
      false = False
      true = True
      named_tuple = time.localtime() # get struct_time
      start_time = time.strftime("%H:%M:%S", named_tuple)
      pstapi = requests.post('http://api.omniparcel.com/labels/printshipment',
      headers={"Content-Type" : "application/json", "access_key" : "2CE65CF79145B4F946928266284319CBE2C6A86E4675F7C79F"},
		json={
      "Origin":{
               "Name":row[10],
               "ContactPerson": row[11],
               "phonenumber": row[12],
               "email": row[13],
               "Address":{
                  "BuildingName":row[14],
                  "StreetAddress":row[15],
                  "Suburb":row[16],
                  "City":row[17],
                  "PostCode":row[18],
                  "CountryCode":row[19]
               
      }
      },
      "Destination":{
               "Id":0,
               "Name":row[0],
               "ContactPerson":row[1],
               "PhoneNumber":row[2],
               "Email":row[3],
               "DeliveryInstructions":"",
               "CostCentreName":"",
               "Address":{
                  "BuildingName":row[4],
                  "StreetAddress":row[5],
                  "Suburb":row[6],
                  "City":row[7],
                  "PostCode":row[8],
                  "CountryCode":row[9]
               }
            },
         "Commodities": [
            {
            "Description": row[20],
            "ItemSKU": row[25],
            "Units": row[21],
            "UnitValue": row[22],
            "UnitKg": row[23],
            "Currency": row[24]
            }
        ],
      "Packages":[
         {
            "Height":row[26],
            "Width":row[27],
            "Kg":row[28],
            "Length":row[29]
         }
      ],
      "PrintToPrinter":false,
      "CarrierLogo":true,
      "Outputs":[
         "LABEL_PNG_100X150"
      ],
            
            "CarrierName": row[30], 
            "Service":row[31],
            "SendTrackingEmail":false,
            "ShipType":row[32],
            "IncludeLineDetails":true,
            "DeliveryReference":row[33],
            "Reference2":"",
            "Reference3":"",
            "IsSignatureRequired":row[34],
            "IsSaturdayDelivery":false,
            "DutiesAndTaxesByReceiver":row[35]
         }
                  )
      named_tuple1 = time.localtime() # get struct_time
      end_time = time.strftime("%H:%M:%S", named_tuple1)
      print(number)
      # print(start_time)
      abc = (pstapi.json())
      # print(abc)
      api_data = abc["Consignments"]
      # print(end_time)

      start_x = time.strptime(start_time.split(',')[0],'%H:%M:%S')
      start_sec = datetime.timedelta(hours=start_x.tm_hour,minutes=start_x.tm_min,seconds=start_x.tm_sec).total_seconds()
      end_x = time.strptime(end_time.split(',')[0],'%H:%M:%S')
      end_sec = datetime.timedelta(hours=end_x.tm_hour,minutes=end_x.tm_min,seconds=end_x.tm_sec).total_seconds()

      time_calcu = end_sec - start_sec
      # print(time_calcu)
      try:
         print("Connote No:-",api_data[0]['Connote'])
         print("Carrier Name:-",abc['CarrierName'])

      except:
         print(abc['Errors'])
         
      number+=1
