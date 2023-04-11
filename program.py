import oracledb
import pymssql  

# BEFORE YOU RUN THE PROGRAM, you must CHANGE this information 
# to match the required information for your Oracle server!
ORACLE_HOST = "your_server.campus-quest.com"
ORACLE_PORT = 1521 # your port here
ORACLE_USER = "database_name_goes_here"
ORACLE_PASSWORD = "database_password_goes_here"
ORACLE_SID = 'xe' # this can be left alone

# BEFORE YOU RUN THE PROGRAM, you must CHANGE this information 
# to match the required information for your Oracle server!
MSSQL_HOST = "your_server.campus-quest.com"
MSSQL_PORT = 1433
MSSQL_USER = "username_goes_here"
MSSQL_PASSWORD = "password_goes_here"
MSSQL_DB = "database_goes_here"

# BEFORE YOU RUN THE PROGRAM, you must COMMENT OUT OR REMOVE
# this line! Only do this after you have updated the above
# lines to point to YOUR database server!
raise SystemError("You did not read the instructions!")

conn_error = False

try:
    # Enable "Thick Mode" to allow connection to Oracle 11g
    oracledb.init_oracle_client(lib_dir="instantclient_19_18")
    conn_oracle = oracledb.connect(user=ORACLE_USER,password=ORACLE_PASSWORD,host=ORACLE_HOST,port=ORACLE_PORT,service_name=ORACLE_SID)
    print("Oracle connected OK.")
except Exception as e:
    print(f"Exception connecting to Oracle: {e}")
    conn_error = True

try:
    conn_mssql = pymssql.connect(server=MSSQL_HOST, user=MSSQL_USER, password=MSSQL_PASSWORD, port=MSSQL_PORT, database=MSSQL_DB)
    print("MSSQL connected OK.")
except Exception as e:
    print(f"Exception connecting to MSSQL: {e}")
    conn_error = True

if conn_error:
    print("There were connection errors. Aborting execution.")
    exit(1)

print("Connections were made successfully.")
print()

# Get a cursor for Oracle
o_cursor = conn_oracle.cursor()

# Query some data from Oracle
print("Oracle: select P#, PNAME from P:")
for row in o_cursor.execute('select P#, PNAME from P'):
    print(row)
print()

# Get a cursor for MSSQL
m_cursor = conn_mssql.cursor()

print("MSSQL: select S#, SNAME from S:")
m_cursor.execute("select S#, SNAME from S")
row = m_cursor.fetchone()
while row:
    print(row)
    row = m_cursor.fetchone()
print()

