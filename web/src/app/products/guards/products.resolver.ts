import { Injectable } from '@angular/core';
import {
  Router,
  Resolve,
  RouterStateSnapshot,
  ActivatedRouteSnapshot,
} from '@angular/router';
import { Observable, of } from 'rxjs';
import { Product } from '../model/product';
import { ProductService } from '../services/product.service';

@Injectable({
  providedIn: 'root',
})
export class ProductsResolver implements Resolve<Product> {
  constructor(private service: ProductService) {}
  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<Product> {
    if (route.params && route.params['id']) {
      return this.service.get_product_by_id(route.params['id']);
    }
    return of({
      id: '',
      category: '',
      price: 0,
      purchase_date: new Date(),
      description: '',
    });
  }
}
