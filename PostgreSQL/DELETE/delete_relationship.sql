DELETE 
FROM thesis
USING professors
WHERE professors.id = thesis.professor_id
AND professors.specialization = 'Distributed Systems'
