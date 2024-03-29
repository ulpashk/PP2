-- DROP FUNCTION IF EXISTS public.query_data(integer, character varying);

CREATE OR REPLACE FUNCTION query_pagination(query_value VARCHAR(20), lim INT, offst INT)
    RETURNS TABLE(id INT, name VARCHAR(20), number VARCHAR(20))
	AS $$ BEGIN
		RETURN QUERY
			SELECT * FROM phonebook WHERE
			phonebook.name ILIKE '%' || query_value || '%' OR phonebook.number ILIKE '%' || query_value || '%'
			ORDER BY phonebook.id LIMIT lim OFFSET offst;
			
    END; $$
	LANGUAGE plpgsql