CREATE DATABASE alimentation CHARACTER SET 'UTF8MB4';

USE alimentation;

CREATE TABLE category (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL);

CREATE TABLE product (barre_code BIGINT NOT NULL PRIMARY KEY, name VARCHAR(100) NOT NULL, nutrition_grade CHAR(1) NOT NULL, brand VARCHAR(50), ingredients VARCHAR(300), quantity CHAR(50));

CREATE TABLE category_and_products (category_id INT NOT NULL, product_barre_code BIGINT NOT NULL, PRIMARY KEY (category_id, product_barre_code), CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES category(id), CONSTRAINT fk_product_barre_code FOREIGN KEY (product_barre_code) REFERENCES product(barre_code));

CREATE TABLE substitution (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, barre_code_to_substitute BIGINT NOT NULL, barre_code_substitute BIGINT NOT NULL, CONSTRAINT fk_to_substitute FOREIGN KEY (barre_code_to_substitute) REFERENCES product(barre_code), CONSTRAINT fk_substitute FOREIGN KEY (barre_code_substitute) REFERENCES product(barre_code));