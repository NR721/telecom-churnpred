SELECT
    a.*,  -- alias for account, select everything
    au.*, 
    cs.*, 
    c.*, 
    cust.*
FROM 
    ai300_capstone.account a  -- base table: account
JOIN 
    ai300_capstone.account_usage au ON a.account_id = au.account_id  -- join account with account_usage on account_id
JOIN 
    ai300_capstone.churn_status cs ON a.customer_id = cs.customer_id  -- join account with churn_status on customer_id
JOIN 
    ai300_capstone.customer cust ON a.customer_id = cust.customer_id  -- join account with customer on customer_id
JOIN 
    ai300_capstone.city c ON c.zip_code = cust.zip_code;  -- join customer with city on zip_code

