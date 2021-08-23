-- Resetting primary keys
ALTER SEQUENCE shifts_id_seq RESTART WITH 1;
ALTER SEQUENCE machines_id_seq RESTART WITH 1;
ALTER SEQUENCE counters_id_seq RESTART WITH 1;

-- Creating counters and machines
CREATE OR REPLACE FUNCTION generate_counters_and_machines(quantity integer)
returns setof void
AS $BODY$
declare
	f record;
begin
	for f in select i from generate_series(1, quantity) as i
	LOOP
		--RAISE NOTICE '%', f.i;
		insert into counters (code) values (format('COUNTER-%s', f.i));
		insert into machines (code, counter_id) values (format('MACHINE-%s', f.i), f.i);
	END LOOP;
return;
end;
$BODY$
LANGUAGE plpgsql VOLATILE;

SELECT generate_counters_and_machines(3);
