DROP TABLE IF EXISTS registrations;

CREATE TABLE registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    name TEXT NOT NULL,
    aadhaar TEXT NOT NULL,
    mobile TEXT NOT NULL,
    skills TEXT,
    availability TEXT
);
