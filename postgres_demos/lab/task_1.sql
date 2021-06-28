INSERT INTO owner (owner_name, owner_age)
VALUES ('Peter', 26),
       ('George', 32),
       ('Amy', 67);

INSERT INTO dog(owner_id, dog_name, dog_age)
VALUES (1, 'Fluffy', 2),
       (3, 'Bully', 3),
       (1, 'Rousey', 5);

INSERT INTO cat(owner_id, cat_name, cat_age)
VALUES (2, 'Tommy', 1),
       (3, 'Jessy', 7),
       (2, 'Bubbles', 3);

INSERT INTO hotel(hotel_name, hotel_stars)
VALUES ('Grand Pets Hotel', 5),
       ('Pets Heaven', 2);

INSERT INTO dog_room(dog_id, hotel_id, register_date, unregister_date)
VALUES (1, 1, '2020-06-08', '2020-06-10'),
       (2, 2, '2020-06-10', '2020-06-15'),
       (3, 2, '2020-06-20', '2020-06-23');

INSERT INTO cat_room(cat_id, hotel_id, register_date, unregister_date)
VALUES (1, 1, '2020-06-08', '2020-06-10'),
       (2, 2, '2020-06-10', '2020-06-15'),
       (3, 2, '2020-06-20', '2020-06-23');
