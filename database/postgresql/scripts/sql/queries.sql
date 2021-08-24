drop function if exists total_production;

CREATE OR REPLACE FUNCTION total_production(
    machine_code varchar(50) default NULL,
    shift_code varchar(50) default NULL,
    target_date date default current_date,
    prev_days integer default 7
)
-- Return type
returns table (
    "date" text,
    "machine" varchar(50),
    "shift" varchar(50),
    "start" time without time zone,
    "end" time without time zone,
    "total_produced" bigint
)
as
$body$
begin
	/*
    Function that evaluates the total production of parts, per day, machine and shift.

    Params:
        machine_code: a unique alphanumeric code, that uniquely identifies the machine
        shift_code: a unique alphanumeric code, that uniquely identifies the shift
        target_date: the current date
        prev_days: number of past days in which the query will base itself to get the data

    Usage:
        select * from total_production();       -- Complete report

        select * from total_production(         -- For the PRESS machine, at the NIGHT shift, for the last 2 days
            machine_code => 'press',
            prev_days => 2,
            shift_code => 'night'
        );
	*/
	return query
		select
			to_char(timestamp_value::date, 'YYYY-MM-DD') as "date",
			m.code as "machine",
			s.code as "shift",
			s.hour_start as "start",
			s.hour_end as "end",
			SUM("value") as "total_produced"
		FROM "values" v
		INNER JOIN machines m ON m.id = v.counter_id
		INNER JOIN counters c ON c.id = m.counter_id
		inner join shifts s on s.machine_id = m.id
        -- Date range filter
		where timestamp_value::date
			between (target_date - interval '1 day' * prev_days) and target_date
        -- Time range (shift) filter
		and timestamp_value::time
            between s.hour_start and s.hour_end
		-- Conditional filtering for both machine and shift codes
		and (machine_code IS NULL OR upper(m.code) = upper(machine_code))
		and (shift_code IS NULL OR upper(s.code) = upper(shift_code))
		GROUP BY (
			"date",
			"machine",
			"shift",
			"start",
			"end"
		)
		order by "date" desc;
end;
$body$
language plpgsql volatile;
