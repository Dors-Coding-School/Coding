-- Students table
-- Assuming id is already indexed as a primary key

-- Courses table
CREATE INDEX idx_courses_department ON courses(department);
CREATE INDEX idx_courses_dept_num_sem ON courses(department, number, semester);
CREATE INDEX idx_courses_title ON courses(title);

-- Enrollments table
CREATE INDEX idx_enrollments_student_course ON enrollments(student_id, course_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);

-- Requirements table
-- Assuming id is already indexed as a primary key

-- Satisfies table
CREATE INDEX idx_satisfies_course ON satisfies(course_id);
CREATE INDEX idx_satisfies_requirement ON satisfies(requirement_id);
