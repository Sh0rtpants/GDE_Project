# establishing a connection to the db
import pymysql

#  function for always connecting to
def dataBaseConnector():
    # schema_name = 'mydb'
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'mysql'
    database = 'mydb'

    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
    return conn


def createRecord(userName):
    connection = dataBaseConnector()
    cursor = connection.cursor()

# Create data in a table
    query = f"INSERT into mydb.users (name) VALUES (%s)"
    query_result = cursor.execute(query, userName)

    # cursor.execute(f' INSERT into mydb.users (id, name) VALUES ('{userID}', {userName})')


# Save into database
    connection.commit()
    cursor.close()
    connection.close()
    return query_result

def readRecord(userID):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {userID};")
    query_result = cursor.fetchone()
    cursor.close()
    connection.close()
    return query_result

# print(readRecord(userID = 2))
# print selected record


# Update Records in a db
def updateRecord(userID, userName):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    query = f"UPDATE users SET name = %s WHERE id = %s"
    cursor.execute(query, (userID, userName))
    connection.commit()
    cursor.close()
    connection.close()
    return 'Success'

def deleteRecord(userID):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    query = f"DELETE FROM users SET name = %s WHERE id = %s"
    cursor.execute(query, userID)
    connection.commit()
    cursor.close()
    connection.close()
    return 'Success'


# print(createRecords(userID=1, userName="Charles"))



print(readRecord(userID=2))
# print(updateRecords(userID=13, userName='Peter'))
