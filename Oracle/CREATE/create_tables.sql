CREATE TABLE students (
  id number(10),
  full_name varchar(255),
  lives_in_campus number(1, 0),
  origin_city varchar(255),
  CONSTRAINT students_pk PRIMARY KEY (id)
);

CREATE TABLE professors (
  id number(10),
  full_name varchar(255),
  specialization varchar(255),
  office_room varchar(255),
  CONSTRAINT professors_pk PRIMARY KEY (id)
);

CREATE TABLE thesis (
  id number(10),
  student_id number(10),
  professor_id number(10),
  thesis_area varchar(255),
  thesis_title varchar(255),
  CONSTRAINT thesis_pk PRIMARY KEY (id),
  CONSTRAINT fk_professor FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE CASCADE,
  CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

