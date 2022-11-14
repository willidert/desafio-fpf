CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e2a16a925892

CREATE TABLE products (
    id INTEGER NOT NULL, 
    purchase_date DATETIME NOT NULL, 
    price FLOAT NOT NULL, 
    description VARCHAR(225) NOT NULL, 
    category VARCHAR(225) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_products_id ON products (id);

INSERT INTO alembic_version (version_num) VALUES ('e2a16a925892');

