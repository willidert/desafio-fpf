import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';

import { Product } from '../model/product';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
})
export class ProductsComponent implements OnInit {
  products$: Observable<Product[]>;
  constructor(
    private service: ProductService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.products$ = this.service.get_products();
  }

  ngOnInit(): void {
    this.products$ = this.service.get_products();
  }

  onEdit(id: string): void {
    console.log(`product ${id} editado`);
  }

  onDelete(id: string): void {
    console.log(`product ${id} deletado`);
  }

  onAdd(): void {
    this.router.navigate(['new'], { relativeTo: this.route });
  }
}
