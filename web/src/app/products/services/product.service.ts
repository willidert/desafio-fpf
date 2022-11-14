import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { Product } from '../model/product';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  private readonly API_URL = 'http://localhost:8000/api/products/';
  constructor(private client: HttpClient) {}

  get_products(): Observable<Product[]> {
    return this.client.get<Product[]>(this.API_URL);
  }

  get_product_by_id(id: number): Observable<Product> {
    return this.client.get<Product>(`${this.API_URL}${id}`);
  }

  save(product: Partial<Product>) {
    if (product.id) {
      return this.update(product);
    }

    return this.create(product);
  }

  remove(id: string): Observable<Product> {
    return this.client.delete<Product>(`${this.API_URL}${id}`);
  }

  private create(product: Partial<Product>) {
    return this.client.post(this.API_URL, product);
  }

  private update(product: Partial<Product>) {
    return this.client.put<Product>(`${this.API_URL}${product.id}`, product);
  }
}
