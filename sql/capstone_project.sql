ALTER TABLE team_jjat.olist_order_reviews_dataset
ALTER COLUMN review_comment_message TYPE VARCHAR(1000);

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'olist_order_reviews_dataset';

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.olist_order_reviews_dataset 
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.olist_products_dataset_translated 
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.olist_orders_customers_geo_states
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.prep_customers
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.prep_orders
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.prep_geolocation
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.prep_orders_customers_geolocation_population
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;

GRANT ALL PRIVILEGES 
ON TABLE team_jjat.prep_city_state_population
TO jingwang, anafilip, tetyanashcherbinina, janinacarus;