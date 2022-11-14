import { Pipe, PipeTransform } from '@angular/core';
import { Product } from 'src/app/products/model/product';

@Pipe({
  name: 'searchFilter',
})
export class SearchFilterPipe implements PipeTransform {
  transform(productList: Product[], search: string): Product[] {
    if (productList) {
      const regexp = new RegExp(search, 'i');
      const properties = Object.keys(productList[0]);
      return [
        ...productList.filter((product) => {
          return properties.some(() => regexp.test(product.category));
        }),
      ];
    }
    return productList;
  }
}
