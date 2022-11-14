import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductsResolver } from './guards/products.resolver';
import { ProductFormComponent } from './product-form/product-form.component';
import { ProductsComponent } from './products/products.component';

const routes: Routes = [
  { path: '', component: ProductsComponent },
  {
    path: 'new',
    component: ProductFormComponent,
    resolve: { product: ProductsResolver },
  },
  {
    path: 'edit/:id',
    component: ProductFormComponent,
    resolve: { product: ProductsResolver },
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ProductsRoutingModule {}
