docker run -d --rm ^
    -p 8080:8080 -p 5432:5432 ^
    --name myPostgres ^
    -e POSTGRES_PASSWORD=1 ^
    -e PGDATA=/var/lib/postgresql/data/pgdata ^
    -v C:\PG:/var/lib/postgresql/data ^
    postgres
pause