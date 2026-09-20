-- SELECT

SELECT * FROM user;

SELECT name FROM user;

SELECT department FROM user;

SELECT CGPA FROM user;

SELECT name
FROM user
WHERE department = 'AIML';

SELECT name
FROM user
WHERE CGPA > 9.9;

SELECT name
FROM user
WHERE department = 'AIML'
AND CGPA > 9.9;

SELECT name
FROM user
WHERE id = 101;


-- UPDATE

UPDATE user
SET department = 'CYBER'
WHERE name = 'Vanch Gupta';

UPDATE user
SET age = 20
WHERE name = 'John Doe';

UPDATE user
SET CGPA = 9.95
WHERE name = 'John Doe';


-- DELETE

DELETE FROM user
WHERE name = 'Vanch Gupta';