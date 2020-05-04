CREATE DATABASE alimentation CHARACTER SET 'UTF8MB4';
USE alimentation;
CREATE TABLE category (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL);
CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, barre_code BIGINT NOT NULL, name VARCHAR(100) NOT NULL, nutrition_grade CHAR(1) NOT NULL, brand VARCHAR(50), ingredients VARCHAR(300), quantity CHAR(50));
CREATE TABLE product_category (product_id INT NOT NULL, category_id INT NOT NULL, PRIMARY KEY (product_id, category_id), CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES category(id), CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product(id));
CREATE TABLE substitution (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_to_substitute BIGINT NOT NULL, id_substitute BIGINT NOT NULL, CONSTRAINT fk_to_substitute FOREIGN KEY (id_to_substitute) REFERENCES product(id), CONSTRAINT fk_substitute FOREIGN KEY (id_substitute) REFERENCES product(id));
/* CREATE TRIGGER after_insert_product AFTER INSERT ON product FOR EACH ROW BEGIN INSERT INTO category_and_products (category_id, product_barre_code) VALUES (LAST_INSERT_ID(), NEW.barre_code); END */
