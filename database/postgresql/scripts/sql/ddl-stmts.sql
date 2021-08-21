CREATE TABLE IF NOT EXISTS "counters" (
  "id" SERIAL PRIMARY KEY,
  "code" varchar(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS "machines" (
  "id" SERIAL PRIMARY KEY,
  "code" varchar(50) UNIQUE NOT NULL,
  "counter_id" int
);

CREATE TABLE IF NOT EXISTS "values" (
  "timestamp_value" timestamptz PRIMARY KEY,
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

ALTER TABLE "machines" ADD FOREIGN KEY ("counter_id") REFERENCES "counters" ("id");

ALTER TABLE "values" ADD FOREIGN KEY ("counter_id") REFERENCES "counters" ("id");

ALTER TABLE "shifts" ADD FOREIGN KEY ("machine_id") REFERENCES "machines" ("id");

COMMENT ON COLUMN "values"."value" IS 'Non-negative integer';
