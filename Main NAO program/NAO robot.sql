use master;

if db_id('NAO_Robot') is not null
  drop database NAO_Robot; 
go

create DATABASE NAO_Robot
go

use NAO_Robot
go


create table Opleiding(
OpleidingID	Int,
Naam	Varchar(20),

Constraint PK_Opleiding
	primary key(OpleidingID)
);

create table Studenten(
StudentID	Int,
OpleidingID	Int,
Voornaam		Varchar(50) not null,
Achternaam		Varchar(50) not null,
Geboortedatum	Date not null,
Studentnummer	Int not null,

Constraint PK_StudentID
	primary key(StudentID),

Constraint FK_Student_Opleiding
	foreign key(OpleidingID)
	references Opleiding(OpleidingID)

);
GO


INSERT INTO Opleiding (OpleidingID, Naam) VALUES (1, 'Business');
INSERT INTO Opleiding (OpleidingID, Naam) VALUES (2, 'Technology');
INSERT INTO Opleiding (OpleidingID, Naam) VALUES (3, 'Software engineering');
INSERT INTO Opleiding (OpleidingID, Naam) VALUES (4, 'Media');

INSERT INTO Studenten (StudentID, OpleidingID, Voornaam, Achternaam, Geboortedatum, Studentnummer) VALUES (1, 1, 'Omar', 'Hanafi', '1994-10-23', 2333678);
INSERT INTO Studenten (StudentID, OpleidingID, Voornaam, Achternaam, Geboortedatum, Studentnummer) VALUES (2, 2, 'Niek', 'Nieuwenhuisen', '1997-04-15', 2587645);








