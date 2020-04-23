Afficher les catégories:

SELECT (name) FROM category

Afficher les produits d''une catégorie:

SELECT (name) FROM product
INNER JOIN category_and_products
ON product.barre_code = category_and_products.product_barre_code
WHERE category_and_products.category_id = "choix_de_la_catégorie_par_utilisateur"

SELECT (name) FROM product

Affiche en détail un produit:

SELECT (barre_code, name, nutrition_grade, brand, ingredients, quantity) FROM product

Afficher une substitution :

SELECT (barre_code_to_substitute, barre_code_substitue) FROM substitution

Enregistrer une catégorie/produit:

INSERT INTO category (name) VALUES ("nom de la catégorie")
INSERT INTO product (barre_code, name, nutrition_grade, brand, ingredients, quantity) VALUES ("code barre", "nom", "nutriscore", "marque", "ingrédients", "quantité")

Enregistrer une substitution:

INSERT INTO substitution (barre_code_to_substitute, barre_code_substitue) VALUES ("vilain produit", "bon produit")

Trouver une substitution :

SELECT barre_code, MIN(nutrition_grade)
FROM (
SELECT product.barre_code, product.nutrition_grade FROM product
INNER JOIN category_and_products
ON product.barre_code = category_and_products.product_barre_code
INNER JOIN category_and_products as c_a_p2
ON category_and_products.product_barre_code = c_a_p2.product_barre_code
WHERE product.nutrition_grade < "nutrition_grade_from_product_to_substitute") as minimal_nutriscore;