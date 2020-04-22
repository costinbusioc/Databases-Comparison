SELECT professors.full_name, professors.office_room, thesis.thesis_area, thesis.thesis_title
FROM professors, thesis
WHERE professors.id = thesis.professor_id 
AND professors.office_room LIKE 'PR3%';
