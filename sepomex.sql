-- Tabla: estado
CREATE TABLE estado (
    id_estado SERIAL PRIMARY KEY,
    codigo_estado VARCHAR(10) UNIQUE NOT NULL, -- Índice único para codigo_estado
    clave_renapo VARCHAR(10) UNIQUE NOT NULL, -- Índice único para clave_renapo
    descripcion_estado VARCHAR(255)
);

-- Tabla: municipio
CREATE TABLE municipio (
    id_municipio SERIAL PRIMARY KEY,
    codigo_municipio VARCHAR(10),
    descripcion_municipio VARCHAR(255),
    id_estado INT REFERENCES estado(id_estado)
);

-- Índice para codigo_municipio
CREATE INDEX idx_municipio_codigo ON municipio(codigo_municipio);

-- Tabla: ciudad
CREATE TABLE ciudad (
    id_ciudad SERIAL PRIMARY KEY,
    codigo_cve_ciudad VARCHAR(10),
    descripcion_ciudad VARCHAR(255),
    id_estado INT REFERENCES estado(id_estado)
);

-- Índice para codigo_cve_ciudad
CREATE INDEX idx_ciudad_cve_ciudad ON ciudad(codigo_cve_ciudad);

-- Tabla: codigo_postal
CREATE TABLE codigo_postal (
    id_codigo SERIAL PRIMARY KEY,
    codigo_codigo VARCHAR(10) UNIQUE,  -- Índice único para codigo_codigo
    id_municipio INT REFERENCES municipio(id_municipio)
);

-- Índice para codigo_codigo
CREATE INDEX idx_codigo_postal_codigo ON codigo_postal(codigo_codigo);

-- Tabla: tipo_asentamiento
CREATE TABLE tipo_asentamiento (
    id_tipo_asenta SERIAL PRIMARY KEY,
    codigo_tipo_asenta VARCHAR(10) UNIQUE, -- Índice único para codigo_tipo_asenta
    descripcion_tipo_asenta VARCHAR(255)
);

-- Índice para codigo_tipo_asenta
CREATE INDEX idx_tipo_asentamiento_codigo ON tipo_asentamiento(codigo_tipo_asenta);

-- Tabla: zona
CREATE TABLE zona (
    id_zona SERIAL PRIMARY KEY,
    descripcion_zona VARCHAR(255) UNIQUE
);

-- Tabla: asentamiento
CREATE TABLE asentamiento (
    id_asentamiento SERIAL PRIMARY KEY,
    id_codigo INT REFERENCES codigo_postal(id_codigo),
    id_ciudad INT REFERENCES ciudad(id_ciudad),
    id_tipo_asenta INT REFERENCES tipo_asentamiento(id_tipo_asenta),
    id_zona INT REFERENCES zona(id_zona),
    id_asenta_cpcons VARCHAR(10),
    descripcion_asentamiento VARCHAR(255)
);

-- Crear índice
CREATE INDEX idx_asentamiento_cpcons ON asentamiento(id_asenta_cpcons);

-- Insertar zonas
INSERT INTO zona (descripcion_zona)
VALUES ('Urbano'), ('Semiurbano'), ('Rural')
ON DUPLICATE KEY UPDATE descripcion_zona = descripcion_zona;

-- Insertar estados
INSERT INTO estado (codigo_estado, descripcion_estado, clave_renapo) VALUES
(1, 'Aguascalientes', 'AS'),
(2, 'Baja California', 'BC'),
(3, 'Baja California Sur', 'BS'),
(4, 'Campeche', 'CC'),
(5, 'Coahuila de Zaragoza', 'CL'),
(6, 'Colima', 'CM'),
(7, 'Chiapas', 'CS'),
(8, 'Chihuahua', 'CH'),
(9, 'Ciudad de México', 'DF'),
(10, 'Durango', 'DG'),
(11, 'Guanajuato', 'GT'),
(12, 'Guerrero', 'GR'),
(13, 'Hidalgo', 'HG'),
(14, 'Jalisco', 'JC'),
(15, 'México', 'MC'),
(16, 'Michoacán de Ocampo', 'MN'),
(17, 'Morelos', 'MS'),
(18, 'Nayarit', 'NT'),
(19, 'Nuevo León', 'NL'),
(20, 'Oaxaca', 'OC'),
(21, 'Puebla', 'PL'),
(22, 'Querétaro', 'QT'),
(23, 'Quintana Roo', 'QR'),
(24, 'San Luis Potosí', 'SP'),
(25, 'Sinaloa', 'SL'),
(26, 'Sonora', 'SR'),
(27, 'Tabasco', 'TC'),
(28, 'Tamaulipas', 'TS'),
(29, 'Tlaxcala', 'TL'),
(30, 'Veracruz de Ignacio de la Llave', 'VZ'),
(31, 'Yucatán', 'YN'),
(32, 'Zacatecas', 'ZS');

-- Insertar Asentamientos
INSERT INTO tipo_asentamiento (codigo_tipo_asenta, descripcion_tipo_asenta) VALUES
(1, 'Aeropuerto'),
(2, 'Barrio'),
(4, 'Campamento'),
(9, 'Colonia'),
(10, 'Condominio'),
(12, 'Conjunto habitacional'),
(15, 'Ejido'),
(17, 'Equipamiento'),
(18, 'Exhacienda'),
(20, 'Finca'),
(21, 'Fraccionamiento'),
(23, 'Granja'),
(24, 'Hacienda'),
(28, 'Pueblo'),
(29, 'Ranchería'),
(31, 'Unidad habitacional'),
(33, 'Zona comercial'),
(34, 'Zona federal'),
(37, 'Zona industrial'),
(40, 'Puerto'),
(46, 'Zona naval'),
(47, 'Zona militar');
