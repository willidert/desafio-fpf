import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Product } from '../model/product';

@Component({
  selector: 'app-product-form',
  templateUrl: './product-form.component.html',
  styleUrls: ['./product-form.component.scss'],
})
export class ProductFormComponent implements OnInit {
  productForm: FormGroup;
  constructor() {
    this.productForm = new FormGroup({
      id: new FormControl('', { nonNullable: true }),
      category: new FormControl('', {
        nonNullable: true,
        validators: [Validators.required, Validators.maxLength(225)],
      }),
      description: new FormControl('', {
        nonNullable: true,
        validators: [Validators.required, Validators.maxLength(225)],
      }),
      price: new FormControl(0, {
        nonNullable: true,
        validators: [Validators.required],
      }),
      purchaseDate: new FormControl<Date | null>(null, {
        validators: [Validators.required],
        nonNullable: true,
      }),
    });
  }

  ngOnInit(): void {}
}
