# establishing a connection to the db
import pymysql

#  function for always connecting to
def dataBaseConnector():
    schema_name = 'mydb'
    hostname = 'http://127.0.0.1'
    port = 3306
    user = 'user'
    password = 'passwd'

    conn = pymysql.connect(host=hostname, port=port, user=user, password=password, db=schema_name)
    return conn


def createRecords(userID, userName):
    connection = dataBaseConnector()
    cursor = connection.cursor()

# Create data in a table
    query = f'INSERT into mydb.users (id, name) VALUES (%s, %s)'
    cursor.execute(query, (userID, userName))

    # cursor.execute(f' INSERT into mydb.users (id, name) VALUES ('{userID}', {userName})')


# Save into database
    connection.commit()
    cursor.close()
    connection.close()
    return "Success"

def readRecord(userID):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {userID};")
    result = cursor.fetchone()
    cursor.close()
    return result

print(readRecord(userID = 2))
# print selected record


# Update Records in a db
def updateRecords(userID, userName = ('Peter')):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    query = f"UPDATE users SET name = %s WHERE id = %s"
    cursor.execute(query, userName, userID)
    connection.commit()
    cursor.close()
    connection.close()
    return userName

def deleteRecords(userID):
    connection = dataBaseConnector()
    cursor = connection.cursor()
    query = f"DELETE FROM users SET name = %s WHERE id = %s"
    cursor.execute(query, userName, userID)
    connection.commit()
    cursor.close()
    connection.close()
    return userID



print(readRecord(userID=2))
print(updateRecords(userID=13, userName='Peter'))
