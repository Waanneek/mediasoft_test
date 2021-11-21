docker run --rm ^
    --name myPGAdmin ^
    -p 80:80 -p 443:443^
    -e "PGADMIN_DEFAULT_EMAIL=user@domain.com" ^
    -e "PGADMIN_DEFAULT_PASSWORD=SuperSecret" ^
    -v C:\PGAdmin:/var/lib/pgadmin ^
    -d dpage/pgadmin4
pause