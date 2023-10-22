import oracledb
import json 
con = oracledb.connect(user="SYSTEM", password="welcome4i", dsn="localhost/XEPDB1", port="1521")

cur = con.cursor()
cur.execute("select * from customer_details")

for CUSTOMER_ID,CUSTOMER_NAME,E_MAIL,PHONE_NUMBER in cur:
    print("Customer ID: ", CUSTOMER_ID)
    print("CUSTOMER NAME: ", CUSTOMER_NAME)
    print("EMAIL: ", E_MAIL)
    print("Phone Number:", PHONE_NUMBER)

cursor = con.cursor()
cursor.execute('SELECT * FROM customer_details')
result = cursor.fetchall()
# Convert the result to a list of dictionaries
data = []
columns = [col[0] for col in cursor.description]
for row in result:
    data.append(dict(zip(columns, row)))

    # Close the database cursor and connection
cursor.close()
cur.close()
print(data)

json_object = json.dumps(data, indent = 4) 
print(json_object)


   

