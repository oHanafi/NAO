
use master;

if db_id('NAO_Robot') is not null
  drop database NAO_Robot; 
go

create DATABASE NAO_Robot
go

use NAO_Robot
go

create table Opleiding(
OpleidingID	int,
Naam	Varchar(20),

Constraint PK_Opleiding
	primary key(OpleidingID)
);

create table Studenten(
StudentID	Int,
OpleidingID	Int,
Naam		Varchar(50) not null,
Geboortedatum	Date not null,
Studentnummer	Int not null,

Constraint PK_StudentID
	primary key(StudentID),

Constraint FK_Student_Opleiding
	foreign key(OpleidingID)
	references Opleiding(OpleidingID)

);



