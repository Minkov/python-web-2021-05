PGDMP     $                    y           pet_hotel_db    13.3 (Debian 13.3-1.pgdg100+1)    13.3 $    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16861    pet_hotel_db    DATABASE     `   CREATE DATABASE pet_hotel_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';
    DROP DATABASE pet_hotel_db;
                postgres    false            ?            1259    16879    cat    TABLE     ?   CREATE TABLE public.cat (
    cat_id bigint NOT NULL,
    cat_name character varying(20) NOT NULL,
    cat_age integer,
    owner_id integer NOT NULL
);
    DROP TABLE public.cat;
       public         heap    postgres    false            ?            1259    16877    cat_cat_id_seq    SEQUENCE     w   CREATE SEQUENCE public.cat_cat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.cat_cat_id_seq;
       public          postgres    false    205            ?           0    0    cat_cat_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.cat_cat_id_seq OWNED BY public.cat.cat_id;
          public          postgres    false    204            ?            1259    16923    cat_room    TABLE     ?   CREATE TABLE public.cat_room (
    cat_room_id bigint NOT NULL,
    register_date date NOT NULL,
    unregister_date date NOT NULL,
    hotel_id integer NOT NULL,
    cat_id integer NOT NULL
);
    DROP TABLE public.cat_room;
       public         heap    postgres    false            ?            1259    16921    cat_room_cat_room_id_seq    SEQUENCE     ?   ALTER TABLE public.cat_room ALTER COLUMN cat_room_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.cat_room_cat_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    211            ?            1259    16892    dog    TABLE     ?   CREATE TABLE public.dog (
    dog_id bigint NOT NULL,
    dog_name character varying(20) NOT NULL,
    dog_age integer NOT NULL,
    owner_id integer NOT NULL
);
    DROP TABLE public.dog;
       public         heap    postgres    false            ?            1259    16890    dog_dog_id_seq    SEQUENCE     w   CREATE SEQUENCE public.dog_dog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.dog_dog_id_seq;
       public          postgres    false    207            ?           0    0    dog_dog_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.dog_dog_id_seq OWNED BY public.dog.dog_id;
          public          postgres    false    206            ?            1259    16905    dog_room    TABLE     ?   CREATE TABLE public.dog_room (
    dog_room_id bigint NOT NULL,
    register_date date NOT NULL,
    unregister_date date NOT NULL,
    hotel_id integer NOT NULL,
    dog_id integer NOT NULL
);
    DROP TABLE public.dog_room;
       public         heap    postgres    false            ?            1259    16903    dog_room_dog_room_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.dog_room_dog_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.dog_room_dog_room_id_seq;
       public          postgres    false    209            ?           0    0    dog_room_dog_room_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.dog_room_dog_room_id_seq OWNED BY public.dog_room.dog_room_id;
          public          postgres    false    208            ?            1259    16864    hotel    TABLE     ?   CREATE TABLE public.hotel (
    hotel_id bigint NOT NULL,
    hotel_name character varying(25) NOT NULL,
    hotel_stars integer NOT NULL
);
    DROP TABLE public.hotel;
       public         heap    postgres    false            ?            1259    16862    hotel_hotel_id_seq    SEQUENCE     ?   ALTER TABLE public.hotel ALTER COLUMN hotel_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.hotel_hotel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    201            ?            1259    16871    owner    TABLE     ?   CREATE TABLE public.owner (
    owner_id bigint NOT NULL,
    owner_name character varying(15) NOT NULL,
    owner_age integer
);
    DROP TABLE public.owner;
       public         heap    postgres    false            ?            1259    16869    owner_owner_id_seq    SEQUENCE     {   CREATE SEQUENCE public.owner_owner_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.owner_owner_id_seq;
       public          postgres    false    203            ?           0    0    owner_owner_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.owner_owner_id_seq OWNED BY public.owner.owner_id;
          public          postgres    false    202                       2604    16882 
   cat cat_id    DEFAULT     h   ALTER TABLE ONLY public.cat ALTER COLUMN cat_id SET DEFAULT nextval('public.cat_cat_id_seq'::regclass);
 9   ALTER TABLE public.cat ALTER COLUMN cat_id DROP DEFAULT;
       public          postgres    false    205    204    205                       2604    16895 
   dog dog_id    DEFAULT     h   ALTER TABLE ONLY public.dog ALTER COLUMN dog_id SET DEFAULT nextval('public.dog_dog_id_seq'::regclass);
 9   ALTER TABLE public.dog ALTER COLUMN dog_id DROP DEFAULT;
       public          postgres    false    207    206    207                       2604    16908    dog_room dog_room_id    DEFAULT     |   ALTER TABLE ONLY public.dog_room ALTER COLUMN dog_room_id SET DEFAULT nextval('public.dog_room_dog_room_id_seq'::regclass);
 C   ALTER TABLE public.dog_room ALTER COLUMN dog_room_id DROP DEFAULT;
       public          postgres    false    208    209    209                       2604    16874    owner owner_id    DEFAULT     p   ALTER TABLE ONLY public.owner ALTER COLUMN owner_id SET DEFAULT nextval('public.owner_owner_id_seq'::regclass);
 =   ALTER TABLE public.owner ALTER COLUMN owner_id DROP DEFAULT;
       public          postgres    false    202    203    203                       2606    16884 
   cat cat_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.cat
    ADD CONSTRAINT cat_pk PRIMARY KEY (cat_id);
 4   ALTER TABLE ONLY public.cat DROP CONSTRAINT cat_pk;
       public            postgres    false    205                        2606    16927    cat_room cat_room_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_pkey PRIMARY KEY (cat_room_id);
 @   ALTER TABLE ONLY public.cat_room DROP CONSTRAINT cat_room_pkey;
       public            postgres    false    211                       2606    16897 
   dog dog_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.dog
    ADD CONSTRAINT dog_pk PRIMARY KEY (dog_id);
 4   ALTER TABLE ONLY public.dog DROP CONSTRAINT dog_pk;
       public            postgres    false    207                       2606    16910    dog_room dog_room_pk 
   CONSTRAINT     [   ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_pk PRIMARY KEY (dog_room_id);
 >   ALTER TABLE ONLY public.dog_room DROP CONSTRAINT dog_room_pk;
       public            postgres    false    209                       2606    16868    hotel hotel_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_pkey PRIMARY KEY (hotel_id);
 :   ALTER TABLE ONLY public.hotel DROP CONSTRAINT hotel_pkey;
       public            postgres    false    201                       2606    16876    owner owner_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pk PRIMARY KEY (owner_id);
 8   ALTER TABLE ONLY public.owner DROP CONSTRAINT owner_pk;
       public            postgres    false    203            !           2606    16885    cat cat_owner__fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.cat
    ADD CONSTRAINT cat_owner__fk FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ;   ALTER TABLE ONLY public.cat DROP CONSTRAINT cat_owner__fk;
       public          postgres    false    2840    203    205            %           2606    16928    cat_room cat_room_cat__fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_cat__fk FOREIGN KEY (cat_id) REFERENCES public.cat(cat_id) ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.cat_room DROP CONSTRAINT cat_room_cat__fk;
       public          postgres    false    2842    211    205            &           2606    16933    cat_room cat_room_hotel__fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_hotel__fk FOREIGN KEY (hotel_id) REFERENCES public.hotel(hotel_id) ON UPDATE CASCADE ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.cat_room DROP CONSTRAINT cat_room_hotel__fk;
       public          postgres    false    201    211    2838            "           2606    16898    dog dog_owner_owner_id_fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.dog
    ADD CONSTRAINT dog_owner_owner_id_fk FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id) ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.dog DROP CONSTRAINT dog_owner_owner_id_fk;
       public          postgres    false    2840    207    203            $           2606    16916    dog_room dog_room_dog__fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_dog__fk FOREIGN KEY (dog_id) REFERENCES public.dog(dog_id) ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.dog_room DROP CONSTRAINT dog_room_dog__fk;
       public          postgres    false    209    2844    207            #           2606    16911    dog_room dog_room_hotel__fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_hotel__fk FOREIGN KEY (hotel_id) REFERENCES public.hotel(hotel_id) ON UPDATE CASCADE ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.dog_room DROP CONSTRAINT dog_room_hotel__fk;
       public          postgres    false    2838    201    209           