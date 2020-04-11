CREATE TABLE `students` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `lives_in_campus` boolean,
  `origin_city` varchar(255)
);

CREATE TABLE `professors` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `specialization` varchar(255),
  `office_room` varchar(255)
);

CREATE TABLE `thesis` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `student_id` int,
  `professor_id` int,
  `thesis_area` varchar(255),
  `thesis_title` varchar(255)
);

ALTER TABLE `thesis` ADD FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE CASCADE;

ALTER TABLE `thesis` ADD FOREIGN KEY (`professor_id`) REFERENCES `professors` (`id`) ON DELETE CASCADE;

