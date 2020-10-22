import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="ariel",
    passwd="Arielmakovoz123",
    database="testdatabase"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE testdatabase")

#mycursor.execute('CREATE TABLE da (name VARCHAR(50) NOT NULL UNIQUE, age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)')
#mycursor.execute("INSERT INTO da (name, age) VALUES (%s, %s)", ("Tim", 19))

mycursor.execute("INSERT INTO da (name, age) VALUES (%s, %s)", ("bob", 19))


#mycursor.execute("SELECT * FROM da WHERE name = 'Tim' OR age=19")
#for x in mycursor:
#    print(x)



mycursor.execute("SELECT * FROM da")
for x in mycursor:
      print(x)

#mycursor.execute("SELECT * FROM Person")
 