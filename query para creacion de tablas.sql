CREATE DATABASE zoo;
GO

USE zoo;
GO

CREATE TABLE Continentes(
	idContinente INTEGER PRIMARY KEY IDENTITY,
	nombre VARCHAR(50) UNIQUE,
);

CREATE TABLE Paises(
	idPais INTEGER PRIMARY KEY IDENTITY,
	nombre VARCHAR(50) UNIQUE,
	idContinente INTEGER REFERENCES Continentes(idContinente)
);

CREATE TABLE ciudades(
	idCiudad INTEGER PRIMARY KEY IDENTITY,
	nombre VARCHAR(50),
	lat FLOAT,
	lon FLOAT,
	idPais INTEGER REFERENCES Paises(idPais)
);

CREATE TABLE Especies(
	idEspecie INTEGER PRIMARY KEY IDENTITY,
	nombre VARCHAR(100),
);

CREATE TABLE informacionAnimales(
	numIdentificacion INTEGER PRIMARY KEY,
	genero VARCHAR(10),
	anio INTEGER,
	idEspecie INTEGER REFERENCES Especies(idEspecie),
	idPais INTEGER REFERENCES Paises(idPais)
);

CREATE TABLE especieAnimales(
	idEspecie INTEGER PRIMARY KEY,
	nombreVulgar VARCHAR(60),
	nombreCientifico VARCHAR(100),
	familia VARCHAR(50),
	peligro BIT,
	idInformacionEspecie INTEGER REFERENCES informacionAnimales(numIdentificacion)
);

CREATE TABLE zoologicos (
	idZoo INTEGER PRIMARY KEY,
	nombre VARCHAR(200),
	tamanio DECIMAL,
	presupuesto MONEY,
	idCiudad INTEGER UNIQUE REFERENCES Ciudades(idCiudad)
);


--/"
--CREATE TABLE espciesZoologicos(
	--idEspecimenZoo INTEGER PRIMARY KEY,
	--idZoo INTEGER REFERENCES zoologicos(idZoo),
	--idEspecie INTEGER REFERENCES especieAnimales(idEspecie)
--); 

-- Insersion de datos

SELECT * FROM Continentes;
GO
--Ingresar continentes
INSERT INTO Continentes VALUES ('AMERICA'),('EUROPA'),('ASIA'),('OCEANIDA');

SELECT * FROM Paises;
--Ingresar Paises
INSERT INTO Paises VALUES('ALEMANIA',2),('ESPANIA', 2),('PANAMA',1),('CHINA',3),('AUSTRALIA',4)

SELECT * FROM ciudades;
--Ingresar Ciudades
INSERT INTO ciudades VALUES('BERLIN', 123.2332323232, 124.432432432, 1), ('MADRID', 150.21321321, 154.1321321, 2)

SELECT * FROM zoologicos;
--Ingresar Zoologico
INSERT INTO zoologicos VALUES (3, 'La Joya', 2500, 400000000, 1)
