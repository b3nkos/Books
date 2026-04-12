import { AsyncPipe, CurrencyPipe } from '@angular/common';
import {
  ChangeDetectionStrategy,
  Component,
  input,
  OnInit,
  output,
  ViewEncapsulation,
} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, switchMap } from 'rxjs';
import { AuthService } from '../auth.service';
import { Product } from '../product';
import { ProductsService } from '../products.service';

@Component({
  selector: 'app-product-detail',
  imports: [CurrencyPipe, AsyncPipe],
  templateUrl: './product-detail.component.html',
  styleUrl: './product-detail.component.css',
  encapsulation: ViewEncapsulation.Emulated,
  changeDetection: ChangeDetectionStrategy.Default,
})
export class ProductDetailComponent implements OnInit {
  product$: Observable<Product> | undefined;
  id = input<string>();

  constructor(
    private productService: ProductsService,
    public authService: AuthService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.product$ = this.productService.getProduct(Number(this.id()))
  }

  addToCart() {

  }

  changePrice(product: Product, price: string) {
    this.productService
      .updateProduct(product.id, Number(price))
      .subscribe(() => {
        this.router.navigate(['/products']);
      });
  }

  remove(product: Product) {
    this.productService.deleteProduct(product.id).subscribe(() => {
      this.router.navigate(['/products']);
    });
  }
}
