DELETE thesis 
FROM thesis
INNER JOIN professors ON professors.id = thesis.professor_id
WHERE professors.specialization = 'Distributed Systems'
