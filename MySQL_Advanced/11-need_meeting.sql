-- A view of Students who have below an 80 and haven't had a meeting yet
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH))
