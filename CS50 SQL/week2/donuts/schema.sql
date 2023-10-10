-- donuts/schema.sql

-- Create Ingredients table
CREATE TABLE Ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price_per_unit REAL NOT NULL,
    unit TEXT NOT NULL  -- e.g. pound, gram, etc.
);

-- Create Donuts table
CREATE TABLE Donuts (
    donut_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    is_gluten_free BOOLEAN NOT NULL,
    price REAL NOT NULL
);

-- Association table to represent the many-to-many relationship between Donuts and Ingredients
CREATE TABLE DonutIngredients (
    donut_id INTEGER,
    ingredient_id INTEGER,
    PRIMARY KEY (donut_id, ingredient_id),
    FOREIGN KEY (donut_id) REFERENCES Donuts(donut_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

-- Create Customers table
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Association table to represent the many-to-many relationship between Orders and Donuts
CREATE TABLE OrderDonuts (
    order_id INTEGER,
    donut_id INTEGER,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (order_id, donut_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (donut_id) REFERENCES Donuts(donut_id)
);
