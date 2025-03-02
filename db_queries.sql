SELECT * FROM expense_manager.expenses;
SELECT * FROM expense_manager.expenses where expense_date="2024-08-25";
DELETE FROM expenses WHERE expense_date="2024-08-25";

SELECT * FROM expenses 
WHERE expense_date 
BETWEEN "2024-08-01" AND "2024-08-05"
ORDER BY expense_date;

SELECT category,SUM(amount) as total
FROM expenses 
WHERE expense_date 
BETWEEN "2024-08-01" AND "2024-08-05"
GROUP BY category;

SELECT * FROM expenses;

INSERT INTO expenses (expense_date, amount, category, notes)
VALUES ('2024-08-15', 10.0, 'Shopping', 'Bought potatoes');


