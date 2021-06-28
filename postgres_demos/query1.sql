
SELECT t.title, t.state, t.description, p.name
FROM todos_person p
         LEFT JOIN todos_todo t
                   ON t.owner_id = p.id
WHERE NOT t.state
    AND lower(t.description) LIKE '%desc%'
ORDER BY title;

