#basic mysql connector

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host=" ",
  user=" ",
  passwd=" ",
  database=" "
)

mycursor = mydb.cursor()

#Query Here

mycursor.execute(
  "select food_id, food_request_created_at, food_request_origin_location_x, food_request_origin_location_y from DB")

myresult = mycursor.fetchall()

myData = pd.DataFrame(myresult)

myData.columns = \
['food_id', 'food_request_created_at','food_request_origin_location_x', 'food_request_origin_location_y']


myData['food_request_created_at'] = list(pd.to_datetime(myData['food_request_created_at']))

orders = myData

