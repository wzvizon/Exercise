/*
Write queries to answer the following questions
Save your work to this .sql file
Right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeId, FirstName, LastName, Title
FROM Employee WHERE Title LIKE '%IT%';

--2. List the names of all Artists and the titles of their albums
SELECT art.Name, alb.Title
FROM Artist art
    JOIN Album alb ON art.ArtistId = alb.ArtistId
ORDER BY art.Name;

--3. Which track is features on the greatest number of times in playlists and how many times is it included? (display Trac
SELECT t.Name, t.TrackId, COUNT( t.TrackId) AS NuMbers
FROM Track t
    JOIN PlaylistTrack PT on t.TrackId = PT.TrackId
GROUP BY t.TrackId
ORDER BY NuMbers DESC LIMIT 1;

--4. Provide a list of the number of tracks by each artist
SELECT art.Name, COUNT(t.AlbumId) AS Tracks
FROM Album alb
    JOIN Artist art on alb.ArtistId = art.ArtistId
    Join Track t on alb.AlbumId = t.AlbumId
GROUP BY art.Name;

--5. How much money has been invoiced for the artist Deep Purple? (display each line item from the invoices and the total amount)
SELECT art.Name, t.Name, IL.InvoiceLineId, IL.UnitPrice
FROM Track t
    JOIN InvoiceLine IL on t.TrackId = IL.TrackId
    JOIN Album alb on t.AlbumId = alb.AlbumId
    JOIN Artist art on alb.ArtistId = art.ArtistId WHERE art.Name = 'Deep Purple'
union
SELECT art.Name, COUNT(IL.InvoiceLineId), 'Total invoice', SUM(IL.UnitPrice)
FROM Track t
    JOIN InvoiceLine IL on t.TrackId = IL.TrackId
    JOIN Album alb on t.AlbumId = alb.AlbumId
    JOIN Artist art on alb.ArtistId = art.ArtistId WHERE art.Name = 'Deep Purple'