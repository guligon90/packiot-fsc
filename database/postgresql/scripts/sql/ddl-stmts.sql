ALTER TABLE IF EXISTS "machines"
DROP CONSTRAINT fk_one_to_one_machine_counter;

ALTER TABLE IF EXISTS "values"
DROP CONSTRAINT fk_many_ot_one_counter_values;

ALTER TABLE IF EXISTS "shifts"
DROP CONSTRAINT fk_many_to_one_machine_shifts;

DROP TABLE IF EXISTS "values";
DROP TABLE IF EXISTS "shifts";
DROP TABLE IF EXISTS "machines";
DROP TABLE IF EXISTS "counters";

CREATE TABLE IF NOT EXISTS "counters" (
    "id" SERIAL PRIMARY KEY,
    "code" varchar(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS "machines" (
    "id" SERIAL PRIMARY KEY,
    "code" varchar(50) UNIQUE NOT NULL,
    --Must be unique, for the FK with counters be one-to-one
    "counter_id" int UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS "values" (
  "timestamp_value" timestamptz PRIMARY KEY DEFAULT CURRENT_TIMESTAMP,  --Could generate collisions for different values
  "counter_id" int NOT NULL,
  "value" int NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS "shifts" (
    "id" SERIAL PRIMARY KEY,
    "code" varchar(50) UNIQUE NOT NULL,
    "machine_id" int NOT NULL,
    "hour_start" time,
    "hour_end" time
);

ALTER TABLE IF EXISTS "machines"
ADD CONSTRAINT fk_one_to_one_machines_counters
FOREIGN KEY ("counter_id") REFERENCES "counters" ("id");

ALTER TABLE IF EXISTS "values"
ADD CONSTRAINT fk_many_ot_one_counters_values
FOREIGN KEY ("counter_id") REFERENCES "counters" ("id");

ALTER TABLE IF EXISTS "shifts"
ADD CONSTRAINT fk_many_to_one_machines_shifts
FOREIGN KEY ("machine_id") REFERENCES "machines" ("id");

COMMENT ON COLUMN "values"."value" IS 'Non-negative integer';
