# Write your MySQL query statement below
delete a from Person a, Person  b
where a.Id > b.Id and a.Email = b.Email
