CREATE DATABASE IF NOT EXISTS viaja_seguro_db;
USE viaja_seguro_db;

-- Tabla Empleado (Actualizada para Bcrypt)
CREATE TABLE IF NOT EXISTS Empleado (
    run VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL -- Aumentado para soportar Bcrypt
);

CREATE TABLE IF NOT EXISTS Cliente (
    run VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Vehiculo (
    patente VARCHAR(10) PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio INT NOT NULL,
    precio_dia_uf FLOAT NOT NULL,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS Arriendo (
    numArriendo INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE NOT NULL,
    fechaEntrega DATE NOT NULL,
    costoTotal_clp INT NOT NULL, 
    cliente_run VARCHAR(12) NOT NULL,
    empleado_run VARCHAR(12) NOT NULL,
    vehiculo_patente VARCHAR(10) NOT NULL,
    FOREIGN KEY (cliente_run) REFERENCES Cliente(run) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (empleado_run) REFERENCES Empleado(run) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (vehiculo_patente) REFERENCES Vehiculo(patente) ON DELETE RESTRICT ON UPDATE CASCADE
);