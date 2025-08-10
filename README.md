# Python-projects
## PostgreSQL Permissions Audit Tools
Overview

This repository contains scripts for managing and auditing PostgreSQL user permissions:

    pg_permissions.sql – Creates the pg_permissions table for storing user privileges on database objects.

    insert_permissions.py – Connects to all non-template databases on a PostgreSQL server, retrieves user permissions, and inserts them into the pg_permissions table.

2. insert_permissions.py — Permissions Collection Script
Purpose

    Retrieves a list of all non-template databases.

    Connects to each database and queries information_schema.role_table_grants.

    Inserts the results into the pg_permissions table in the target database.

Requirements

    Python 3.7+

    Required packages:

    pip install pandas sqlalchemy psycopg2

Configuration

Edit the script to set PostgreSQL connection parameters.


Notes

- Excludes system schemas: pg_catalog, information_schema.

- The user running the script must have access to:

   All target databases

   information_schema.role_table_grants in each database.

    Sensitive credentials should be kept outside the script (e.g., environment variables or .env file).
