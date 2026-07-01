/* Write your T-SQL query statement below */
select Person.Firstname, Person.lastname,Address.city, Address. state
from Person
left join Address
on Person.PersonId = Address.PersonId