UPDATE professors
SET specialization = 'Super cool new specialization'
WHERE id IN (
	SELECT professor_id
	FROM thesis
	WHERE thesis_area = 'Semantic Web'
);
