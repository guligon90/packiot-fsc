-- Removing previous data
DELETE FROM shifts;
DELETE FROM machines;
DELETE FROM "values";
DELETE FROM counters;

-- Resetting primary keys
alter sequence shifts_id_seq restart with 1;
alter sequence machines_id_seq restart with 1;
alter sequence counters_id_seq restart with 1;

-- Create type for dummy shift creation
DROP TYPE IF EXISTS shift;
CREATE TYPE shift AS (
    code varchar,
    start_hour time,
    end_hour time
);

CREATE OR REPLACE FUNCTION create_counter_and_machine(machine_code varchar(50))
returns setof void
AS $BODY$
declare
	counter_code varchar(50) := format('%s-COUNTER', UPPER(machine_code));
begin
	--Creating machine
	insert into counters (
		code
	) values (
		counter_code
	);

	--Creating PRESS machine
	insert into machines (
		code,
		counter_id
	) select
		upper(machine_code) as code,
		id
	from counters
	where code = counter_code;

	return;
end;
$BODY$
LANGUAGE plpgsql VOLATILE;


CREATE OR REPLACE FUNCTION create_shifts(machine_code varchar(50))
returns setof void
AS $BODY$
declare
	p shift;
	periods shift[] := array[
		('MORNING', '05:00', '10:00'),
		('AFTERNOON', '11:00', '16:00'),
		('NIGHT', '17:00', '22:00')
	];
	_machine_id integer;
begin
	select id
	into _machine_id
	from machines
	where code = upper(machine_code);

	IF _machine_id IS NULL THEN
		RAISE EXCEPTION 'Nonexistent machine with code %', upper(machine_code)
      		USING HINT = 'Please check your machine code.';
	else
		FOREACH p in array periods
		LOOP
			insert into shifts (
				code,
				machine_id,
				hour_start,
				hour_end
			) values (
				p.code,
				_machine_id,
				p.start_hour,
				p.end_hour
			);
		END LOOP;
    END IF;

	return;
end;
$BODY$
LANGUAGE plpgsql VOLATILE;


CREATE OR REPLACE FUNCTION create_counter_values(counter_code varchar(50))
returns setof void
as $BODY$
declare
	_d date;
	_s shift;
	_ts timestamp;
	_count integer := 0;
	_counter_id integer;
	_interval timestamp[];
	generated_days date[];
	generated_timestamps timestamp[];
	shift_list shift[];
	ts_format varchar := 'YYYY-MM-DD HH24:MI:SS';
begin
	--Fetches the counter ID
	select c.id
	into _counter_id
	from counters c
	inner join machines m on c.id = m.counter_id
	where c.code = upper(counter_code);

	--Fetches the shift list for the pair (machine, counter)
	shift_list := array(
		select (
			s.code,
			hour_start,
			hour_end
		)
		from shifts s
		inner join machines m on m.id = s.machine_id
		where m.counter_id = _counter_id
	);

	if array_length(shift_list, 1) = 0 then
		RAISE EXCEPTION 'Nonexistent shifts for matchine with counter %', upper(counter_code)
      		USING HINT = 'Please check your counter code.';
	else
		--Generates a list of days (by defaultn seven)
		generated_days := array(
			SELECT t.day::date
			FROM generate_series(
				current_date - interval '6 days',
				current_date,
				interval '1 day'
			) as t(day)
		);

		foreach _d in array generated_days
		loop
			foreach _s in array shift_list
			loop
				-- For each day, generates the minutes inside
				-- a time interval defined by each shift
				_interval = array(
					select t.ts
					from generate_series(
						TO_TIMESTAMP(format('%s %s', _d, _s.start_hour), ts_format),
						TO_TIMESTAMP(format('%s %s', _d, _s.end_hour), ts_format),
						interval '1 minute'
					) as t(ts)
				);

				--Inserts the counter values for the whole interval
				foreach _ts in array _interval
				loop
					insert into "values" (
						timestamp_value,
						counter_id,
						"value"
					) values (
						_ts,
						_counter_id,
						_count
					) on conflict do nothing;
					_count := _count + 1;
				end loop;
			end loop;
		
			-- The counter is restarted at each new day
			_count = 0;
		end loop;
	end if;
	return;
end;
$BODY$
LANGUAGE plpgsql VOLATILE;

-- Calling helper functions to create dummy data
SELECT create_counter_and_machine('press');
SELECT create_shifts('press');
SELECT create_counter_values('press-counter');
