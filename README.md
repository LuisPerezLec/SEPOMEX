Crear el contenedor de PostgreSQL
`docker run --name sepomex -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=root_password -d -p 5432:5432 postgres`

Conectarnos al contenedor
`docker exec -it sepomex psql -U postgres`

Crear base de datos
`CREATE DATABASE sepomex;`

Conectarnos a la base de datos
`\c sepomex`

Insertar la base de datos sepomex.sql

Insertar datos de Estados

Generar tipos de asentamiento con tipo_asentamiento.py e insertarlos.

Generar municipios con municipio.py e insertar el archivo generado `municipios.sql` en el contenedor con:
`docker exec -i sepomex psql -U postgres -d sepomex -f /dev/stdin < inserciones_municipios.sql`

Generar las ciudades con ciudad.py e insertar el archivo generado `ciudades.sql` en el contenedor con:
`docker exec -i sepomex psql -U postgres -d sepomex -f /dev/stdin < inserciones_ciudades.sql`

Generar los códigos postales con codigo.py e insertar el archivo generado `codigos.sql` en el contenedor con:
`docker exec -i sepomex psql -U postgres -d sepomex -f /dev/stdin < inserciones_codigos.sql`

Generar los asentamientos con asentamiento.py e insertar el archivo generado `asentamientos.sql` en el contenedor con:
`docker exec -i sepomex psql -U postgres -d sepomex -f /dev/stdin < inserciones_asentamientos.sql`