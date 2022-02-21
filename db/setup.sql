-- =========== Customers ===========
CREATE TABLE IF NOT EXISTS customers(
  customer_id INTEGER PRIMARY KEY autoincrement,
  first_name TEXT,
  last_name TEXT,
  phone INTEGER
);

INSERT INTO customers (first_name, last_name, phone) VALUES ('Delcine', 'Stouther', 270258927026);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Sandy', 'Yeo', 413027221465);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Dori', 'Orleton', 415806176140);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Astrix', 'Skelding', 054434875061);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Dillie', 'Ashley', 685113945511);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Gwen', 'McPartlin', 225190001904);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Thatcher', 'Trevallion', 880504669989);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Sarena', 'Elvy', 423151998309);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Olimpia', 'Goadsby', 253995597653);
INSERT INTO customers (first_name, last_name, phone) VALUES ('Alida', 'Samper', 617645980881);

SELECT '=== Customers ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(customers);
SELECT '=> Data' AS ' ';
SELECT * FROM customers;

-- =========== Orders ===========
CREATE TABLE IF NOT EXISTS orders(
  order_id INTEGER PRIMARY KEY autoincrement,
  customer_id INTEGER not null,
  total float,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders (customer_id) VALUES (7);
INSERT INTO orders (customer_id) VALUES (8);
INSERT INTO orders (customer_id) VALUES (8);
INSERT INTO orders (customer_id) VALUES (8);
INSERT INTO orders (customer_id) VALUES (5);
INSERT INTO orders (customer_id) VALUES (7);
INSERT INTO orders (customer_id) VALUES (7);
INSERT INTO orders (customer_id) VALUES (1);
INSERT INTO orders (customer_id) VALUES (6);
INSERT INTO orders (customer_id) VALUES (3);

SELECT '=== Orders ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(orders);
SELECT '=> Data' AS ' ';
SELECT * FROM orders;

-- =========== Order Items ===========
CREATE TABLE IF NOT EXISTS orderitems (
  order_id INTEGER not null,
  customer_id INTEGER not null,
  isbn VARCHAR not null,
  purchased_on DATETIME not null,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (isbn) REFERENCES books(isbn)
);

INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (7, 3, '036229545-X', '2021-09-01 10:37:39');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (4, 1, '586064084-6', '2022-02-01 09:48:35');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (8, 7, '862108064-8', '2021-06-01 13:20:53');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (5, 2, '862108064-8', '2022-01-20 04:14:15');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (1, 9, '490568805-1', '2021-08-26 23:37:34');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (6, 6, '617781295-3', '2021-12-16 01:25:02');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (1, 9, '928380563-1', '2021-05-17 09:19:47');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (2, 3, '586041181-2', '2021-04-25 13:10:56');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (6, 1, '501676410-7', '2021-08-12 03:55:43');
INSERT INTO orderitems (order_id, customer_id, isbn, purchased_on) VALUES (3, 10, '510806946-4', '2021-02-14 10:18:53');

SELECT '=== Order Items ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(orderitems);
SELECT '=> Data' AS ' ';
SELECT * FROM orderitems;

-- =========== Publishers ===========
CREATE TABLE IF NOT EXISTS publishers(
  publisher_id INTEGER PRIMARY KEY,
  name TEXT
);

INSERT INTO publishers (name) VALUES ('Dibbert, Sporer and Smitham');
INSERT INTO publishers (name) VALUES ('Ryan, Rau and Mayert');
INSERT INTO publishers (name) VALUES ('Davis Group');
INSERT INTO publishers (name) VALUES ('Jones, Nikolaus and Windler');
INSERT INTO publishers (name) VALUES ('Reichel-Stamm');
INSERT INTO publishers (name) VALUES ('Shanahan-O''Keefe');
INSERT INTO publishers (name) VALUES ('Moen-Stiedemann');
INSERT INTO publishers (name) VALUES ('Howe LLC');
INSERT INTO publishers (name) VALUES ('McCullough-Monahan');
INSERT INTO publishers (name) VALUES ('Bosco, Herzog and Hermiston');

SELECT '=== Publishers ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(publishers);
SELECT '=> Data' AS ' ';
SELECT * FROM publishers;

-- =========== Inventory ===========
CREATE TABLE IF NOT EXISTS inventory(
  isbn VARCHAR PRIMARY KEY,
  sold INTEGER,
  total INTEGER,
  last_updated DATETIME,
  FOREIGN KEY (isbn) REFERENCES books(isbn)
);

INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('036229545-X', 6, 24, '2021-09-01 10:37:39');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('586064084-6', 4, 17, '2022-02-01 09:48:35');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('862108064-8', 8, 58, '2021-06-01 13:20:53');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('596975602-4', 6, 28, '2022-01-20 04:14:15');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('490568805-1', 8, 18, '2021-08-26 23:37:34');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('617781295-3', 9, 44, '2021-12-16 01:25:02');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('928380563-1', 2, 97, '2021-05-17 09:19:47');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('586041181-2', 7, 16, '2021-04-25 13:10:56');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('501676410-7', 5, 52, '2021-08-12 03:55:43');
INSERT INTO inventory (isbn, sold, total, last_updated) VALUES ('510806946-4', 5, 57, '2021-02-14 10:18:53');

SELECT '=== Inventory ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(inventory);
SELECT '=> Data' AS ' ';
SELECT * FROM inventory;

-- =========== Authors ===========
CREATE TABLE IF NOT EXISTS authors(
  author_id INTEGER PRIMARY KEY autoincrement,
  name VARCHAR not null
);

INSERT INTO authors (name) VALUES ('Dalis Barca');
INSERT INTO authors (name) VALUES ('Donetta Milner');
INSERT INTO authors (name) VALUES ('Horatius Pawelec');
INSERT INTO authors (name) VALUES ('Kay Djokovic');
INSERT INTO authors (name) VALUES ('Aloise O'' Faherty');
INSERT INTO authors (name) VALUES ('Etti McKeney');
INSERT INTO authors (name) VALUES ('Kirk Ert');
INSERT INTO authors (name) VALUES ('Emmie Littrik');
INSERT INTO authors (name) VALUES ('Andie Haney');
INSERT INTO authors (name) VALUES ('Donni Pettit');

SELECT '=== Authors ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(authors);
SELECT '=> Data' AS ' ';
SELECT * FROM authors;

-- =========== Books ===========
CREATE TABLE IF NOT EXISTS books(
  isbn VARCHAR PRIMARY KEY,
  name VARCHAR,
  author_id INTEGER,
  publisher_id INTEGER,
  order_id INTEGER,
  FOREIGN KEY(author_id) REFERENCES author(author_id),
  FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id),
  FOREIGN KEY(order_id) REFERENCES orders(order_id)
  FOREIGN KEY(isbn) REFERENCES inventory(isbn)
);

INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('036229545-X', 'Streptopelia decipiens', 10, 6, 8);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('586064084-6', 'Choloepus hoffmani', 7, 6, 9);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('862108064-8', 'Pavo cristatus', 4, 10, 4);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('596975602-4', 'Bubalornis niger', 6, 2, 1);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('490568805-1', 'Acrobates pygmaeus', 7, 9, 3);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('617781295-3', 'Prionace glauca', 1, 4, 8);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('928380563-1', 'Phascogale calura', 7, 10, 1);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('586041181-2', 'Alligator mississippiensis', 2, 10, 2);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('501676410-7', 'Gyps bengalensis', 9, 3, 2);
INSERT INTO books (isbn, name, author_id, publisher_id, order_id) VALUES ('510806946-4', 'Paradoxurus hermaphroditus', 6, 1, 4);


SELECT '=== Books ===' AS ' ';
SELECT '=> Schema' AS ' ';
PRAGMA table_info(books);
SELECT '=> Data' AS ' ';
SELECT * FROM books;

-- =========== Sample Statements ===========
SELECT '=== Find Book ===' AS ' ';
SELECT b.isbn, b.name, a.name
FROM books AS b 
  INNER JOIN authors AS a ON b.author_id = a.author_id
  where b.isbn='862108064-8';

SELECT '=== Find Order Items ===' AS ' ';
SELECT b.isbn, b.name, c.customer_id
FROM orderitems AS oi
  INNER JOIN books AS b on b.isbn = oi.isbn
  INNER JOIN customers AS c on c.customer_id = oi.customer_id
  where oi.isbn = '862108064-8';

SELECT '=== Find Customers ===' AS ' ';
SELECT c.customer_id, c.first_name, c.last_name
FROM customers AS c
  INNER JOIN orders AS o ON o.customer_id = c.customer_id
  where c.first_name='Delcine' AND c.last_name='Stouther';