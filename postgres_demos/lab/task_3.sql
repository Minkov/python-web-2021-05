--Select only the ids of the cats that are in rooms from the hotel with id=2

SELECT cr.cat_id
FROM hotel h
         JOIN cat_room cr
              ON h.hotel_id = cr.hotel_id
WHERE h.hotel_id = 2