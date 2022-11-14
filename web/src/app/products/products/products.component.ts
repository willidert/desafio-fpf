import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';

import { Product } from '../model/product';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
})
export class ProductsComponent implements OnInit {
  products$: Product[] = [];

  searchForm: FormGroup;
  constructor(
    private service: ProductService,
    private route: ActivatedRoute,
    private router: Router,
    public dialog: MatDialog
  ) {
    this.searchForm = new FormGroup({
      search: new FormControl<string>(''),
    });

    this.service.get_products().subscribe((data) => (this.products$ = data));
  }

  ngOnInit(): void {
    this.service.get_products().subscribe((data) => (this.products$ = data));
  }

  onEdit(id: string): void {
    this.router.navigate(['edit', id], { relativeTo: this.route });
  }

  onDelete(id: string): void {
    if (confirm('Are you sure you want to delete this?')) {
      this.service.remove(id).subscribe(() => {
        this.service
          .get_products()
          .subscribe((data) => (this.products$ = data));
      });
    }
  }

  onAdd(): void {
    this.router.navigate(['new'], { relativeTo: this.route });
  }
}
