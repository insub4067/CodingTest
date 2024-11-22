-- 1193. Monthly Transactions I
-- https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&envId=top-sql-50

select 
    date_format(trans_date, "%Y-%m") as month,
    country, 
    count(*) as trans_count,
    sum(if(state = "approved", 1, 0)) as approved_count,
    sum(amount) as trans_total_amount,
    sum(if(state = "approved", amount, 0)) as approved_total_amount
from 
    Transactions
group by 
    country, date_format(trans_date, "%Y-%m")