CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    CGPA DECIMAL(10,2) NOT NULL
);

INSERT INTO user (id, name, department, age, CGPA)
VALUES
    (101, 'Vanch Gupta', 'AIML', 19, 9.95),
    (102, 'John Doe', 'AIML', 21, 9.925);