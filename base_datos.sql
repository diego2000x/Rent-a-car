-- 1. Creación de la Base de Datos
CREATE DATABASE IF NOT EXISTS viaja_seguro_rentacar;
USE viaja_seguro_rentacar;

-- 2. Tabla Sucursal
-- Según el diagrama: tiene lista de empleados y vehículos (relación 1 a muchos)
CREATE TABLE Sucursal (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    direccion VARCHAR(100) NOT NULL,
    fono VARCHAR(20) NOT NULL,
    correo VARCHAR(100) NOT NULL
);

-- 3. Tabla Empleado
-- Hereda de Persona (run, nombre, apellido) y tiene atributos propios.
-- Relación: Pertenece a una Sucursal.
CREATE TABLE Empleado (
    codigo INT PRIMARY KEY AUTO_INCREMENT,
    run VARCHAR(12) NOT NULL UNIQUE, -- Formato 12345678-9
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL, -- Ej: Gerente, Vendedor
    password VARCHAR(255) NOT NULL, -- Longitud 255 para guardar el Hash seguro 
    sucursal_codigo INT,
    FOREIGN KEY (sucursal_codigo) REFERENCES Sucursal(codigo)
);

-- 4. Tabla Cliente
-- Hereda de Persona (run, nombre, apellido) y tiene atributos propios.
-- Se usa el RUN como identificador único para operaciones CRUD[cite: 58].
CREATE TABLE Cliente (
    run VARCHAR(12) PRIMARY KEY, -- Usamos RUN como PK para facilitar búsquedas
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

-- 5. Tabla Vehiculo
-- Relación: Es parte de una Sucursal.
-- El precio se guarda en UF (decimal).
CREATE TABLE Vehiculo (
    patente VARCHAR(10) PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL, -- Precio en UF (ej: 1.50)
    disponible VARCHAR(20) DEFAULT 'S', -- 'S' para Sí, 'N' para No (Arrendado)
    sucursal_codigo INT,
    FOREIGN KEY (sucursal_codigo) REFERENCES Sucursal(codigo)
);

-- 6. Tabla Arriendo
-- Es la tabla central que une Cliente, Empleado y Vehículo.
-- Costo total se guarda en pesos (INT).
CREATE TABLE Arriendo (
    numArriendo INT PRIMARY KEY AUTO_INCREMENT,
    fechaInicio DATE NOT NULL,
    fechaEntrega DATE NOT NULL,
    costoTotal INT NOT NULL, -- En Pesos Chilenos calculado al día del arriendo
    cliente_run VARCHAR(12) NOT NULL,
    empleado_codigo INT NOT NULL,
    vehiculo_patente VARCHAR(10) NOT NULL,
    
    -- Definición de Claves Foráneas (Relaciones del diagrama)
    FOREIGN KEY (cliente_run) REFERENCES Cliente(run),
    FOREIGN KEY (empleado_codigo) REFERENCES Empleado(codigo),
    FOREIGN KEY (vehiculo_patente) REFERENCES Vehiculo(patente)
);

-- ==========================================
-- DATOS DE PRUEBA (Para facilitar tus test)
-- ==========================================

-- Insertar una Sucursal
INSERT INTO Sucursal (direccion, fono, correo) VALUES 
('Av. Siempre Viva 123', '22334455', 'contacto@viajaseguro.cl');

-- Insertar un Empleado (Gerente)
-- NOTA: En la app real, la password debe insertarse ya hasheada. 
-- Aquí ponemos 'admin123' solo por prueba inicial.
INSERT INTO Empleado (run, nombre, apellido, cargo, password, sucursal_codigo) VALUES 
('11111111-1', 'Juan', 'Perez', 'Gerente', 'admin123', 1);

-- Insertar un Cliente
INSERT INTO Cliente (run, nombre, apellido, direccion, telefono) VALUES 
('22222222-2', 'Maria', 'Gonzalez', 'Calle Falsa 123', '987654321');

-- Insertar un Vehículo
INSERT INTO Vehiculo (patente, marca, modelo, anio, precio, disponible, sucursal_codigo) VALUES 
('ABCD-12', 'Toyota', 'Yaris', 2023, 1.50, 'S', 1);



########clave gerente: administrador123 #######usar bcrypt para esa clave