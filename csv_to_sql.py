import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='work')

# Insert data into MySQL
data = pd.read_csv('./dummy.csv')
data.to_sql(name='dummy', con=cnx, if_exists='append', index=False)

# Close the MySQL connection
cnx.close()
cnx.commit()
