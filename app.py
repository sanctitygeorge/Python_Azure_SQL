# Import libraries
import pyodbc
import pandas as pd

# Configure SQL Server Connections Parameters
server = 'SQL Server Name'
database = 'Database Name'
username = 'SQL Server Username'
password = 'SQL Server Password'
driver= '{ODBC Driver 18 for SQL Server}'

# cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Connect to the SQL Server and test the connection
cnxn = pyodbc.connect(connection_string)
print(cnxn)


# use the cursor function to query top 5 records from the DB
cursor = cnxn.cursor()
cursor.execute("SELECT TOP 5 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " : " + str(row[1]))
    row = cursor.fetchone()
 
# Export the Azure SQL query result as a CSV file

queryOutput = pd.read_sql_query("SELECT * FROM [SalesLT].[Product]", cnxn)
df = pd.DataFrame(queryOutput)
df.to_csv (r'exported_sql_data3.csv', index = False) 
