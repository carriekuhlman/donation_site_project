--
-- PostgreSQL database dump
--

-- Dumped from database version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: donors; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.donors (
    donor_id integer NOT NULL,
    fname character varying(50) NOT NULL,
    lname character varying(50) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.donors OWNER TO vagrant;

--
-- Name: donors_donor_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.donors_donor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.donors_donor_id_seq OWNER TO vagrant;

--
-- Name: donors_donor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.donors_donor_id_seq OWNED BY public.donors.donor_id;


--
-- Name: items; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.items (
    item_id integer NOT NULL,
    item_name character varying(50) NOT NULL,
    condition_accepted character varying(50) NOT NULL,
    qty_needed integer,
    location_id integer NOT NULL
);


ALTER TABLE public.items OWNER TO vagrant;

--
-- Name: items_item_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.items_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_item_id_seq OWNER TO vagrant;

--
-- Name: items_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.items_item_id_seq OWNED BY public.items.item_id;


--
-- Name: locations; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.locations (
    location_id integer NOT NULL,
    phone character varying(50),
    street_address character varying(100) NOT NULL,
    city character varying(100) NOT NULL,
    state character varying(2) NOT NULL,
    zip_code character varying(10) NOT NULL,
    accept_in_person boolean NOT NULL,
    donation_hours character varying(50),
    org_id integer NOT NULL
);


ALTER TABLE public.locations OWNER TO vagrant;

--
-- Name: locations_location_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.locations_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.locations_location_id_seq OWNER TO vagrant;

--
-- Name: locations_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.locations_location_id_seq OWNED BY public.locations.location_id;


--
-- Name: orgs; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.orgs (
    org_id integer NOT NULL,
    org_name character varying(100) NOT NULL,
    org_description text,
    org_website character varying(100),
    user_id integer NOT NULL
);


ALTER TABLE public.orgs OWNER TO vagrant;

--
-- Name: orgs_org_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.orgs_org_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orgs_org_id_seq OWNER TO vagrant;

--
-- Name: orgs_org_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.orgs_org_id_seq OWNED BY public.orgs.org_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying(320) NOT NULL,
    password character varying(50) NOT NULL
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: donors donor_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.donors ALTER COLUMN donor_id SET DEFAULT nextval('public.donors_donor_id_seq'::regclass);


--
-- Name: items item_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.items ALTER COLUMN item_id SET DEFAULT nextval('public.items_item_id_seq'::regclass);


--
-- Name: locations location_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.locations ALTER COLUMN location_id SET DEFAULT nextval('public.locations_location_id_seq'::regclass);


--
-- Name: orgs org_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.orgs ALTER COLUMN org_id SET DEFAULT nextval('public.orgs_org_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: donors; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.donors (donor_id, fname, lname, user_id) FROM stdin;
1	Donor1	Lastname	6
2	Donor2	Lastname	9
3	Donor3	Lastname	8
4	Donor4	Lastname	3
5	Donor5	Lastname	7
7	Leila	Bird	15
8	Cool	Donor	20
9	Sandy	Kuhlman	21
10	Carrie	Mueller	24
11	Nick	Mueller	27
\.


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.items (item_id, item_name, condition_accepted, qty_needed, location_id) FROM stdin;
1	1_item	New	3	4
2	2_item	Lightly Used	14	3
3	3_item	New	19	2
4	4_item	Lightly Used	28	2
5	5_item	For Scraps	25	4
6	6_item	Lightly Used	24	2
7	7_item	New	13	5
8	8_item	For Scraps	14	5
9	9_item	New	15	4
10	10_item	Lightly Used	19	3
11	11_item	Lightly Used	5	5
12	12_item	For Scraps	17	5
13	13_item	Lightly Used	22	3
14	14_item	New	19	3
15	15_item	New	11	2
16	16_item	New	1	3
17	17_item	New	23	3
18	18_item	Lightly Used	6	1
19	19_item	New	9	1
20	20_item	New	10	1
21	Couch	New	10	8
22	Cart	For Scraps	1	5
23	Blanket	Lightly Used	20	9
24	Dog Bed	New	15	15
25	Blanket	For Scraps	1000	17
\.


--
-- Data for Name: locations; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.locations (location_id, phone, street_address, city, state, zip_code, accept_in_person, donation_hours, org_id) FROM stdin;
1	(111) 111-1111	111 Fake St.	Canoga Park	CA	91303	f	\N	5
2	(222) 222-2222	222 Fake St.	Canoga Park	CA	91303	t	2am to 2pm	3
3	(333) 333-3333	333 Fake St.	Canoga Park	CA	91303	t	3am to 3pm	1
4	(444) 444-4444	444 Fake St.	Canoga Park	CA	91303	f	\N	4
5	(555) 555-5555	555 Fake St.	Canoga Park	CA	91303	t	5am to 5pm	2
8	123-456-7890	12345 Fakest St.	Ever	CA	91505	t	10am-5pm	2
9	111-456-7609	1999 Also Fake Ave.	Faketown	TX	78006	f	\N	2
10	888-888-8888	1567 Conure Blvd.	Coolness	CA	91505	t	1pm to 5pm	8
11	111-999-0000	126 Fake Blvd.	Fake Town	CO	91303	t	MWF 9am to 2pm	9
12	444-444-4444	357 Fakest Blvd	Burbank	CA	91501	t	2pm-5pm	10
13	111-111-1111	356 Madeup Ave.	Burbank	CA	91501	t	8am-2pm	11
14	444-444-4444	8675309 Star Blvd.	Los Angeles	CA	91360	f	\N	12
15	555-555-5555	46809 New Fake Ave.	Burbank	CA	91501	t	10am-2pm	2
16	111-111-7777	4793 Somewhere Ave	Burbank	CA	91501	t	10am-2pm	13
17	444-444-4444	67890 Cool Blvd	Los Angeles	CA	91003	f	\N	13
\.


--
-- Data for Name: orgs; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.orgs (org_id, org_name, org_description, org_website, user_id) FROM stdin;
1	Org1	Org #1 is really cool.	www.org1.test	5
2	Org2	Org #2 is really cool.	www.org2.test	1
3	Org3	Org #3 is really cool.	www.org3.test	2
4	Org4	Org #4 is really cool.	www.org4.test	4
5	Org5	Org #5 is really cool.	www.org5.test	10
6	Life House	Hanging on every word you are saying.	www.life.house	17
7	Very Much Life House			18
8	The Boys are Back in Town	WOOOOOOOOOO	www.backintown.test	19
9	Cool Testing	We test. It's awesome!	www.test.test	22
10	Testing Again	Testing Again	www.test.test	23
11	The Kuhlest Org	We are so cool and need lots of things!              	www.needthings.com	25
12	Wow! An Org!	Can't believe it's another org!              	www.whatorgisthis.gov	26
13	Goldfish Unlimited	We have so many goldfish!              	whatacoolsite.biz	28
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, email, password) FROM stdin;
1	user1@test.test	test
2	user2@test.test	test
3	user3@test.test	test
4	user4@test.test	test
5	user5@test.test	test
6	user6@test.test	test
7	user7@test.test	test
8	user8@test.test	test
9	user9@test.test	test
10	user10@test.test	test
15	leila@justtesting.com	cookbird5
17	breathing@life.house	breathing123
18	wannabe@verymuchlife.house	yeah456
19	theboys@backintown.test	testing
20	donornew@test.test	test
21	testdonornew@test.test	test
22	testorgnew@test.test	test
23	newaccount@test.test	test
24	donor20@test.test	test
25	org20@test.test	test
26	org21@test.test	test
27	nick@myaccount.com	test
28	new_org@test.test	test
\.


--
-- Name: donors_donor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.donors_donor_id_seq', 11, true);


--
-- Name: items_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.items_item_id_seq', 25, true);


--
-- Name: locations_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.locations_location_id_seq', 17, true);


--
-- Name: orgs_org_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.orgs_org_id_seq', 13, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_user_id_seq', 28, true);


--
-- Name: donors donors_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.donors
    ADD CONSTRAINT donors_pkey PRIMARY KEY (donor_id);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (item_id);


--
-- Name: locations locations_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.locations
    ADD CONSTRAINT locations_pkey PRIMARY KEY (location_id);


--
-- Name: orgs orgs_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.orgs
    ADD CONSTRAINT orgs_pkey PRIMARY KEY (org_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: donors donors_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.donors
    ADD CONSTRAINT donors_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: items items_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.locations(location_id);


--
-- Name: locations locations_org_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.locations
    ADD CONSTRAINT locations_org_id_fkey FOREIGN KEY (org_id) REFERENCES public.orgs(org_id);


--
-- Name: orgs orgs_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.orgs
    ADD CONSTRAINT orgs_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

