import pymysql.cursors  
import configparser

 
# Connect to the database.
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',                             
                             db='',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")

try:
    with connection.cursor() as cursor:
        # SQL 
        sql = "select * from subscribers;"
         
        # Execute query.
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Close connection.
    connection.close()