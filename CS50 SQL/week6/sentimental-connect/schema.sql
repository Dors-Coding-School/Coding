CREATE DATABASE linkedin;
USE linkedin;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password CHAR(128) NOT NULL
);

-- Schools table
CREATE TABLE schools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    location VARCHAR(255) NOT NULL,
    founding_year YEAR
);

-- Companies table
CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    industry ENUM('Technology', 'Education', 'Business') NOT NULL,
    location VARCHAR(255) NOT NULL
);

-- Connections between users
CREATE TABLE connections (
    user1_id INT,
    user2_id INT,
    PRIMARY KEY (user1_id, user2_id),
    FOREIGN KEY (user1_id) REFERENCES users(id),
    FOREIGN KEY (user2_id) REFERENCES users(id)
);

-- Connections between users and schools
CREATE TABLE user_schools (
    user_id INT,
    school_id INT,
    start_date DATE,
    end_date DATE,
    degree VARCHAR(255),
    PRIMARY KEY (user_id, school_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

-- Connections between users and companies
CREATE TABLE user_companies (
    user_id INT,
    company_id INT,
    start_date DATE,
    end_date DATE,
    title VARCHAR(255),
    PRIMARY KEY (user_id, company_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
