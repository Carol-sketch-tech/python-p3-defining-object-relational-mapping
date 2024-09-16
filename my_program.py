db_connection = sqlite3.connect('pets.db')
db_cursor = db_connection.cursor()

# # create an owners table and a cats table 
# db_cursor.execute('CREATE TABLE IF NOT EXISTS cats(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER)')
# db_cursor.execute('CREATE TABLE IF NOT EXISTS owners(id INTEGER PRIMARY KEY, name TEXT)')

# # INSERT New cats and owners into these tables.
# db_cursor.execute('INSERT INTO cats (name, breed, age) VALUES ("Maru","Scottish fold",3)')
# db_cursor.execute("INSERT INTO cats (name, breed, age) VALUES ('Hana', 'tortoiseshell', 1)")

# # notice that in the line above there is alot of repetion


# heres an example of a save method in the cat class the handles teh common action of INSERTing data into the database.

class Cat:
    all = []

    def __init__(self, name, breed, age):
        self.name = name 
        self.breed = breed
        self.age =age
        self.add_cat_to_all(self)

        @classmethod
        def add_cat_to_all(cls, cat):
            cls.all.append(cat)
        
        def save(self, cursor):
            cursor.execute(
                'INSERT INTO cats(name, breed, age) VALUES (?, ?, ?)',
                (self.name, self.breed, self.age)
            )
# now ceating instances of Cat class 

Maru = Cat('Maru', "scottish fold", 3)
Hana = Cat("Hana", "tortoiseshell", 1)

for cat in Cat.all:
    cat.save(db_cursor)
'''
Here we have established the connection to our databse, create two new cats and the iterate over our collection of cat instances stored in the Cat.all list.
Inside this iteration we use the save() method giving it arguments of the data specific to each cat to INSERT those cats into the cats table.

save () method allows us to avoind repetition and also have reusable code.
'''

# Note 
'''
WE only pass in a cursor as an argument for the save() method. where does save() gett he data to be inserted
into the cats table?
        answer:
            from the isntance that the method is being called on.
            instance methods receive self as an implicit argument when they are called.
            this allows any isntnace method to access all of an isntance attributes, like self.name, self.breed and self.age above.
'''