SELECT professors.full_name, students.full_name, thesis.thesis_title
FROM professors, students, thesis
WHERE professors.id = thesis.professor_id AND students.id = thesis.student_id
