-- Create table
CREATE TABLE new_students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE house_assignments (
    id INTEGER,
    student_name INT,
    house INT,
    PRIMARY KEY(id)
);
