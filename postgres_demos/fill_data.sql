--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.3

-- Started on 2021-06-28 21:26:43 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2988 (class 0 OID 16871)
-- Dependencies: 203
-- Data for Name: owner; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.owner (owner_id, owner_name, owner_age) FROM stdin;
1	Peter	26
2	George	32
3	Amy	67
\.


--
-- TOC entry 2990 (class 0 OID 16879)
-- Dependencies: 205
-- Data for Name: cat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cat (cat_id, cat_name, cat_age, owner_id) FROM stdin;
2	Jessy	7	3
3	Bubbles	3	2
\.


--
-- TOC entry 2986 (class 0 OID 16864)
-- Dependencies: 201
-- Data for Name: hotel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hotel (hotel_id, hotel_name, hotel_stars) FROM stdin;
1	Hotel 1	3
2	Grand Pets Hotel	5
3	Pets Heaven	2
\.


--
-- TOC entry 2996 (class 0 OID 16923)
-- Dependencies: 211
-- Data for Name: cat_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cat_room (cat_room_id, register_date, unregister_date, hotel_id, cat_id) FROM stdin;
2	2020-06-10	2020-06-15	2	2
3	2020-06-20	2020-06-23	2	3
\.


--
-- TOC entry 2992 (class 0 OID 16892)
-- Dependencies: 207
-- Data for Name: dog; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dog (dog_id, dog_name, dog_age, owner_id) FROM stdin;
2	Bully	3	3
3	Rousey	5	1
\.


--
-- TOC entry 2994 (class 0 OID 16905)
-- Dependencies: 209
-- Data for Name: dog_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dog_room (dog_room_id, register_date, unregister_date, hotel_id, dog_id) FROM stdin;
2	2020-06-10	2020-06-15	2	2
3	2020-06-20	2020-06-23	2	3
\.


--
-- TOC entry 3002 (class 0 OID 0)
-- Dependencies: 204
-- Name: cat_cat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cat_cat_id_seq', 3, true);


--
-- TOC entry 3003 (class 0 OID 0)
-- Dependencies: 210
-- Name: cat_room_cat_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cat_room_cat_room_id_seq', 3, true);


--
-- TOC entry 3004 (class 0 OID 0)
-- Dependencies: 206
-- Name: dog_dog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_dog_id_seq', 3, true);


--
-- TOC entry 3005 (class 0 OID 0)
-- Dependencies: 208
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dog_room_dog_room_id_seq', 3, true);


--
-- TOC entry 3006 (class 0 OID 0)
-- Dependencies: 200
-- Name: hotel_hotel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hotel_hotel_id_seq', 3, true);


--
-- TOC entry 3007 (class 0 OID 0)
-- Dependencies: 202
-- Name: owner_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.owner_owner_id_seq', 3, true);


-- Completed on 2021-06-28 21:26:43 EEST

--
-- PostgreSQL database dump complete
--

