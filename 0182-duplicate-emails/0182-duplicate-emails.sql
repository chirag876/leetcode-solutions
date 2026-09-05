# Write your MySQL query statement below

select Email as Email from Person group by Email having count(*) > 1