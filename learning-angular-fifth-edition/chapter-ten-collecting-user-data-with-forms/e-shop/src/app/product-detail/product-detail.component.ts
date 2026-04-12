import { AsyncPipe, CurrencyPipe } from '@angular/common';
import {
  ChangeDetectionStrategy,
  Component,
  input,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../auth.service';
import { CartService } from '../cart.service';
import { PriceMaximumDirective } from "../price-maximum.directive";
import { Product } from '../product';
import { ProductsService } from '../products.service';

@Component({
  selector: 'app-product-detail',
  imports: [CurrencyPipe, AsyncPipe, FormsModule, PriceMaximumDirective],
  templateUrl: './product-detail.component.html',
  styleUrl: './product-detail.component.css',
  encapsulation: ViewEncapsulation.Emulated,
  changeDetection: ChangeDetectionStrategy.Default,
})
export class ProductDetailComponent implements OnInit {
  product$: Observable<Product> | undefined;
  id = input<string>();
  price: number | undefined;

  constructor(
    private productService: ProductsService,
    public authService: AuthService,
    private router: Router,
    private cartService: CartService
  ) {}

  ngOnInit(): void {
    this.product$ = this.productService.getProduct(Number(this.id()))
  }

  addToCart(id: number) {
    this.cartService.addProduct(id).subscribe();
  }

  changePrice(product: Product) {
    this.productService
      .updateProduct(product.id, this.price!)
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
