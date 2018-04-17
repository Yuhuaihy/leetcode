# Write your MySQL query statement below
delete a from Person a, Person  b
where a.Id > b.Id and a.Email = b.Email


#####group by
delete from Person
where Id not in(
select * from (
select min(Id) from Person
    Group by Email
)temp
)
