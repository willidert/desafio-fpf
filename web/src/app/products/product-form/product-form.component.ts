import { Location } from '@angular/common';
import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../model/product';

import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-product-form',
  templateUrl: './product-form.component.html',
  styleUrls: ['./product-form.component.scss'],
})
export class ProductFormComponent implements OnInit {
  productForm: FormGroup;
  submitted = false;
  constructor(
    private service: ProductService,
    private location: Location,
    private route: ActivatedRoute
  ) {
    this.productForm = new FormGroup({
      id: new FormControl('', { nonNullable: true }),
      category: new FormControl('', {
        nonNullable: true,
        validators: [
          Validators.required,
          Validators.maxLength(225),
          Validators.minLength(2),
        ],
      }),
      description: new FormControl('', {
        nonNullable: true,
        validators: [Validators.required, Validators.maxLength(225)],
      }),
      price: new FormControl(0, {
        nonNullable: true,
        validators: [Validators.required],
      }),
      purchase_date: new FormControl<Date | null>(null, {
        validators: [Validators.required],
        nonNullable: true,
      }),
    });
  }

  ngOnInit(): void {
    const product: Product = this.route.snapshot.data['product'];
    // this.productForm.patchValue(product);
    this.productForm.setValue({
      purchase_date: product.purchase_date,
      id: product.id,
      description: product.description,
      price: product.price,
      category: product.category,
    });
  }

  onConfirm() {
    this.submitted = true;
    if (this.productForm.valid) {
      let product: Product = this.productForm.value;
      this.service.save(product).subscribe({
        next: () => {
          this.location.back();
        },
        error: (e: HttpErrorResponse) => {
          confirm('Failed to create the product. Is the backend up?');
        },
      });
    }
  }

  onCancel() {
    this.productForm.reset();
    this.submitted = false;
    this.location.back();
  }
}
