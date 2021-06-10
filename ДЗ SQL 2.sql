use Academy ;
CREATE TABLE Groups 
(
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(10) NOT NULL UNIQUE,
Rating int NOT NULL 
check (0 <= Rating and Rating <= 5),
"YEAR" int NOT NULL 
check (1 <= "YEAR" and "YEAR" <= 5),
);
CREATE TABLE Departments
(
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Financing money NOT NULL  default(0)
check (Financing >= 0),
"Name" nvarchar(100) NOT NULL UNIQUE,
);
CREATE TABLE Faculties
(
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(100) NOT NULL UNIQUE,
);
CREATE TABLE Teachers 
(
id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
EmploymentDate date NOT NULL 
check (EmploymentDate >= '1990.01.01' ),
"Name" nvarchar(max) NOT NULL ,
Premium money NOT NULL default(0)
check (Premium >= 0),
Salary money NOT NULL 
check (Salary >= 0),
Surname nvarchar(max) NOT NULL,
);

