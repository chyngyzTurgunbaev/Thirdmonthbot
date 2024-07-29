class Queries:
    CREATE_TABLE_REVIEW = '''CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER,
    name VARCHAR(255),
    instagram_username VARCHAR(255),
    visit_date VARCHAR(255),
    food_rating VARCHAR(255),
    cleanliness_rating VARCHAR(255),
    extra_comments TEXT
    )'''

    CREATE_TABLE_CATEGORIES = '''
    CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    UNIQUE(name))'''

    CREATE_TABLE_DISHES = '''
    CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    price INTEGER(255),
    photo TEXT,
    category_id INTEGER,
    UNIQUE(title),
    FOREIGN KEY(category_id) REFERENCES categories(id))'''

    INSERT_INTO_CAT = '''
    INSERT OR IGNORE INTO categories (name) VALUES ("drinks"),("first_meal"),("second_meal")'''
    INSERT_INTO_DISHES = '''
    INSERT OR IGNORE INTO dishes (title,price,photo,category_id) VALUES ("Pizza",280,"images/pizza.jpeg",2),
    ("shaurma",200,"images/shaurma.jpg",3),
    ("milkshake",100,"images/milkshake.jpeg",1)'''
