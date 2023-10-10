-- schema.sql

-- Create Passengers table
CREATE TABLE Passengers (
    passenger_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- Create Airlines table
CREATE TABLE Airlines (
    airline_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    concourse TEXT NOT NULL
);

-- Create Flights table
CREATE TABLE Flights (
    flight_id INTEGER PRIMARY KEY,
    flight_number INTEGER NOT NULL,
    airline_id INTEGER,
    departing_airport_code TEXT NOT NULL,
    arriving_airport_code TEXT NOT NULL,
    departure_datetime DATETIME NOT NULL,
    arrival_datetime DATETIME NOT NULL,
    FOREIGN KEY (airline_id) REFERENCES Airlines(airline_id)
);

-- Create CheckIns table
CREATE TABLE CheckIns (
    checkin_id INTEGER PRIMARY KEY,
    passenger_id INTEGER,
    flight_id INTEGER,
    checkin_datetime DATETIME NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id)
);
