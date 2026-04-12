import { AsyncPipe, CurrencyPipe } from '@angular/common';
import {
  ChangeDetectionStrategy,
  Component,
  input,
  OnChanges,
  output,
  ViewEncapsulation,
} from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../product';
import { ProductsService } from '../products.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-product-detail',
  imports: [CurrencyPipe, AsyncPipe],
  templateUrl: './product-detail.component.html',
  styleUrl: './product-detail.component.css',
  encapsulation: ViewEncapsulation.Emulated,
  changeDetection: ChangeDetectionStrategy.Default,
})
export class ProductDetailComponent implements OnChanges {
  product$: Observable<Product> | undefined;
  added = output();
  id = input<number>();
  deleted = output();

  constructor(private productService: ProductsService, public authService: AuthService) {}

  ngOnChanges(): void {
    this.product$ = this.productService.getProduct(this.id()!);
  }

  addToCart() {
    this.added.emit();
  }

  changePrice(product: Product, price: string) {
    this.productService.updateProduct(product.id, Number(price)).subscribe();
  }

  remove(product: Product) {
    this.productService.deleteProduct(product.id).subscribe(() => {
      this.deleted.emit();
    });
  }
}
