CREATE TABLE "students" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "lives_in_campus" boolean,
  "origin_city" varchar
);

CREATE TABLE "professors" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "specialization" varchar,
  "office_room" varchar
);

CREATE TABLE "thesis" (
  "id" SERIAL PRIMARY KEY,
  "student_id" int,
  "professor_id" int,
  "thesis_area" varchar,
  "thesis_title" varchar
);

ALTER TABLE "thesis" ADD FOREIGN KEY ("student_id") REFERENCES "students" ("id") ON DELETE CASCADE;

ALTER TABLE "thesis" ADD FOREIGN KEY ("professor_id") REFERENCES "professors" ("id") ON DELETE CASCADE;

