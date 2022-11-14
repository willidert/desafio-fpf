from fastapi.testclient import TestClient
from decimal import Decimal
from pytest import approx

from src.test.utils import generate_random_datetime, generate_random_str, generate_random_float

def test_get_products(client: TestClient) -> None:
    response = client.get('/api/products/')
    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)

def test_create_product(client: TestClient) -> None:
    product = {
        "category": generate_random_str(),
        "description": generate_random_str(),
        "price": generate_random_float(),
        "purchase_date": generate_random_datetime().isoformat(),
    }

    response = client.post('/api/products/', json=product)
    assert response.status_code == 201, response.text
    data = response.json()

    assert "category" in data
    assert data["category"] == product["category"]
    assert data["description"] == product["description"]
    assert data["price"] == product["price"]
    assert data["purchase_date"] == product["purchase_date"]

def test_get_product_by_id(client: TestClient) -> None:
    response = client.get('/api/products/')
    data = response.json()

    data = data[0]

    response = client.get(f'/api/products/{data["id"]}')

    assert response.status_code == 200, response.text

    product = response.json()

    assert product["id"] == data["id"]
    assert product["category"] == data["category"]
    assert product["description"] == data["description"]
    assert product["purchase_date"] == data["purchase_date"]
    assert product["price"] == data["price"]

def test_get_product_by_invalid_id(client: TestClient) -> None:
    response = client.get(f'/api/products/{-1}')

    assert response.status_code == 404, response.text
    
    data = response.json()

    assert data["detail"] == "Product not found."

def test_update_product(client: TestClient) -> None:
    response = client.get(f'/api/products/{1}')

    assert response.status_code == 200, response.text

    product_db = response.json()

    print(product_db)

    product_update = {
        "id": product_db["id"],
        "category": generate_random_str(),
        "description": product_db["description"],
        "price": product_db["price"],
        "purchase_date": product_db["purchase_date"],
    }

    print(product_update)

    response = client.put(f'/api/products/{1}', json=product_update)

    assert response.status_code == 204

    response = client.get(f'/api/products/{1}')

    assert response.status_code == 200, response.text

    product_updated = response.json()

    assert product_updated
    assert product_updated["category"] == product_update["category"]
    assert product_updated["description"] == product_update["description"]
    assert product_updated["price"] == product_update["price"]
    assert product_updated["purchase_date"] == product_update["purchase_date"]

def test_delete_product(client: TestClient) -> None:
    response = client.delete(f'/api/products/{1}')

    assert response.status_code == 204

    response = client.get(f'/api/products/{1}')

    assert response.status_code == 404, response.text

    data = response.json()

    assert data["detail"] == "Product not found."
