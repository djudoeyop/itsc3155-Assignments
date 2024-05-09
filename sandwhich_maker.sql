/*Gabriel Reeder 801186827*/
Create Database sandwich_maker;
Use sandwich_maker;

Create Table sandwiches (
sandwich_size varchar(50),
price decimal(5,2)
);

CREATE TABLE resources (
    Item VARCHAR(50),
    amount INT
);

CREATE TABLE recipes (
    sandwich_size VARCHAR(50),
    Item VARCHAR(50),
    amount INT
);

INSERT INTO resources (Item, amount) VALUES
('bread', 12),
('ham', 18),
('cheese', 24);

INSERT INTO sandwiches (sandwich_size, price) VALUES
('small',1.75),
('medium', 3.25),
('large',5.5);

INSERT INTO recipes (sandwich_size, Item, amount) VALUES
('small', 'bread', 2),
('small', 'ham', 4),
('small', 'cheese', 4),
('medium', 'bread', 4),
('medium', 'ham', 6),
('medium', 'cheese', 8),
('large', 'bread', 6),
('large', 'ham', 8),
('large', 'cheese', 12);

SELECT * FROM resources;
SELECT * FROM sandwiches;
SELECT * FROM recipes;