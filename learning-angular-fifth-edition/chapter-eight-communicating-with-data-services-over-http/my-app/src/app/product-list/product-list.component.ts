import { AsyncPipe } from '@angular/common';
import {
  Component,
  OnInit
} from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../product';
import { ProductDetailComponent } from '../product-detail/product-detail.component';
import { ProductsService } from '../products.service';
import { SortPipe } from '../sort.pipe';
import { ProductCreateComponent } from '../product-create/product-create.component';

@Component({
  selector: 'app-product-list',
  imports: [ProductDetailComponent, SortPipe, AsyncPipe, ProductCreateComponent],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css',
  providers: [ProductsService],
})
export class ProductListComponent implements OnInit {
  selectedProduct: Product | undefined;
  products$: Observable<Product[]> | undefined;

  constructor(private productService: ProductsService) {}

  onAdded() {
    alert(`${this.selectedProduct?.title} added to the cart!`);
  }

  ngOnInit(): void {
    this.getProducts();
  }

  private getProducts() {
    this.products$ = this.productService.getProducts();
  }

}
