Afficher les catégories:

SELECT (name) FROM category

Afficher les produits:

SELECT (name) FROM product

Affiche en détail un produit:

SELECT (barre_code, name, nutrition_grade, brand, ingredients, quantity) FROM product

Afficher une substitution :

SELECT (barre_code_to_substitute, barre_code_substitue) FROM substitution

Enregistrer une catégorie/produit:

INSERT INTO category (name) VALUES ("nom de la catégorie")
INSERT INTO product (barre_code, name, nutrition_grade, brand, ingredients, quantity) VALUES ("code barre", "nom", "nutriscore", "marque", "ingrédients", "quantité")
INSERT INTO category_and_products (name) VALUES (LAST_ROW_ID())

Enregistrer une substitution:

INSERT INTO substitution (barre_code_to_substitute, barre_code_substitue) VALUES ("vilain produit", "bon produit")

Trouver une substitution :

SELECT product.barre_code FROM product
INNER JOIN category_and_products
ON product.barre_code = category_and_products.product_barre_code
INNER JOIN category_and_products as c_a_p2
ON category_and_products.product_barre_code = c_a_p2.product_barre_code
WHERE product.nutrition_grade < "nutrition_grade_of_product_to_substitute";