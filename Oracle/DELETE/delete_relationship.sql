DELETE
FROM thesis
WHERE EXISTS
( 
	SELECT professors.id
	FROM professors
	WHERE professors.id = thesis.professor_id
	AND specialization = 'Distributed Systems'
);

