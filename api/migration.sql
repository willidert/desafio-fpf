BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e2a16a925892

CREATE TABLE products (
    id SERIAL NOT NULL, 
    purchase_date TIMESTAMP WITH TIME ZONE NOT NULL, 
    price FLOAT(2) NOT NULL, 
    description VARCHAR(225) NOT NULL, 
    category VARCHAR(225) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_products_id ON products (id);

INSERT INTO alembic_version (version_num) VALUES ('e2a16a925892') RETURNING alembic_version.version_num;

COMMIT;

