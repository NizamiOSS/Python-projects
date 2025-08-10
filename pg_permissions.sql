-- public.pg_permissions definition

-- Drop table

-- DROP TABLE public.pg_permissions;

CREATE TABLE public.pg_permissions (
	db_name text NULL,
	user_name text NULL,
	"permission" text NULL,
	schema_name text NULL,
	table_name text NULL
);
CREATE INDEX ix_db_name ON public.pg_permissions USING btree (db_name);