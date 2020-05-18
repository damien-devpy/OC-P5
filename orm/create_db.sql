CREATE DATABASE IF NOT EXISTS alimentation CHARACTER SET 'UTF8MB4';
USE alimentation;
CREATE TABLE IF NOT EXISTS category (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, barre_code BIGINT NOT NULL, name VARCHAR(200) NOT NULL, nutrition_grade CHAR(1) NOT NULL, brand VARCHAR(200), ingredients VARCHAR(3000), quantity CHAR(50));
CREATE TABLE IF NOT EXISTS product_category (product_id INT NOT NULL, category_id INT NOT NULL, PRIMARY KEY (product_id, category_id), CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES category(id), CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product(id));
CREATE TABLE IF NOT EXISTS substitution (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_to_substitute INT NOT NULL, id_substitute INT NOT NULL, CONSTRAINT fk_to_substitute FOREIGN KEY (id_to_substitute) REFERENCES product(id), CONSTRAINT fk_substitute FOREIGN KEY (id_substitute) REFERENCES product(id), UNIQUE KEY (id_to_substitute, id_substitute));
