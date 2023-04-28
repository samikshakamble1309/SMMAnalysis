
-- average call length for each gender
SELECT customer_gender, AVG(call_length) AS avg_call_length
FROM AIdataset
GROUP BY customer_gender;

-- Calculate the correlation between call length and service agent voice hertz
SELECT 
    (SUM(call_length * service_agent_voice) - COUNT(*) * AVG(call_length) * AVG(service_agent_voice))
    / (SQRT((SUM(call_length * call_length) - COUNT(*) * AVG(call_length) * AVG(call_length))) 
    * SQRT((SUM(service_agent_voice * service_agent_voice) - 
    COUNT(*) * AVG(service_agent_voice) * AVG(service_agent_voice))))
    AS correlation
FROM AIdataset;



SELECT customer_service_location, COUNT(*) AS num_customers
FROM AIdataset
GROUP BY customer_service_location
ORDER BY num_customers DESC
LIMIT 1;

-- average online spending for customers who have installed similar AI app and for customers who have not installed similar AI app
SELECT prior_AI_experience, AVG(online_spending) as avg_online_spending
FROM AIdataset
GROUP BY prior_AI_experience;

SELECT customer_educ_level, customer_gender,  COUNT(*) AS num_purchased_loan
FROM AIdataset
WHERE purchase_decision = 1
GROUP BY customer_gender, customer_educ_level
ORDER BY 
    customer_educ_level ASC;


