-- connect/schema.sql

-- Create Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL  -- Note: In real-world scenarios, you'd store a hash here
);

-- Create Schools table
CREATE TABLE Schools (
    school_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    school_type TEXT NOT NULL,
    location TEXT NOT NULL,
    founding_year INTEGER
);

-- Create Companies table
CREATE TABLE Companies (
    company_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    industry TEXT NOT NULL,
    location TEXT NOT NULL
);

-- Create Connections between Users
CREATE TABLE UserConnections (
    user1_id INTEGER,
    user2_id INTEGER,
    PRIMARY KEY (user1_id, user2_id),
    FOREIGN KEY (user1_id) REFERENCES Users(user_id),
    FOREIGN KEY (user2_id) REFERENCES Users(user_id)
);

-- Create User-School affiliations
CREATE TABLE UserSchools (
    user_id INTEGER,
    school_id INTEGER,
    start_date DATE,
    end_date DATE,
    degree TEXT,
    PRIMARY KEY (user_id, school_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (school_id) REFERENCES Schools(school_id)
);

-- Create User-Company affiliations
CREATE TABLE UserCompanies (
    user_id INTEGER,
    company_id INTEGER,
    start_date DATE,
    end_date DATE,
    title TEXT,
    PRIMARY KEY (user_id, company_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);
