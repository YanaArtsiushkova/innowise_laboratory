-- Create tables students and grades.
CREATE TABLE students (
id INT IDENTITY(1,1) PRIMARY KEY,
full_name TEXT,
birth_year INTEGER
);

CREATE TABLE grades (
id INT IDENTITY(1,1) PRIMARY KEY,
student_id INTEGER,
subject TEXT,
grade INTEGER,
FOREIGN KEY(student_id) REFERENCES students(id),
CHECK(grade >=0 AND grade <=100)
);

-- Insert data.
INSERT INTO students (full_name, birth_year) 
VALUES 
('Alice Jhonson', 2005), 
('Brian Smith', 2004), 
('Carla Reyes', 2006), 
('Daniel Kim', 2005), 
('Eva Thompson', 2003), 
('Felix Nguyen', 2007), 
('Grace Patel', 2005), 
('Henry Lopez', 2004), 
('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) 
VALUES 
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75), 
(2, 'History', 83),
(2, 'English', 79), 
(3, 'Science', 95),
(3, 'Math', 91), 
(3, 'Art', 89),
(4, 'Math', 84), 
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90), 
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78), 
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90), 
(8, 'History', 77), 
(8, 'Math', 83),
(8, 'Science', 80), 
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- All grades for a specific student.
SELECT full_name, grade FROM grades
JOIN students ON grades.student_id = students.id
WHERE full_name = 'Alice Jhonson';

-- The average grade per student.
SELECT full_name, ROUND(AVG(grade)) AS avg_grade FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY full_name;

-- All student born after 2004.
SELECT full_name FROM students
WHERE birth_year > 2004;

-- All subjects and their average grades.
SELECT subject, ROUND(AVG(grade)) AS average_grade 
FROM grades
GROUP BY subject;

-- Top 3 students
SELECT TOP 3 full_name, ROUND(AVG(grade)) AS avg_grade FROM students
JOIN grades ON grades.student_id = students.id
GROUP BY full_name
ORDER BY avg_grade DESC;

-- All students who have scored below 80 in any subject 
SELECT full_name From students
JOIN grades ON grades.student_id = students.id
WHERE grade < 80
GROUP BY full_name;
