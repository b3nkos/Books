import { Component, OnInit } from '@angular/core';
import { FormArray, FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatFormField, MatInput, MatLabel } from '@angular/material/input';
import { CartService } from '../cart.service';
import { Product } from '../product';
import { ProductsService } from '../products.service';

@Component({
  selector: 'app-cart',
  imports: [
    ReactiveFormsModule,
    MatInput,
    MatFormField,
    MatLabel
],
  templateUrl: './cart.component.html',
  styleUrl: './cart.component.css',
})
export class CartComponent implements OnInit {
  cartForm = new FormGroup({
    products: new FormArray<FormControl<number>>([]),
  });
  products: Product[] = [];

  constructor(
    private cartService: CartService,
    private productsService: ProductsService
  ) {}

  ngOnInit(): void {
    this.getProducts();
    this.buildForm();
  }

  private getProducts() {
    this.productsService.getProducts().subscribe((products) => {
      this.cartService.cart?.products.forEach((item) => {
        const product = products.find(
          (product) => product.id === item.productId
        );

        if (product) {
          this.products.push(product);
        }
      });
    });
  }

  private buildForm() {
    this.products.forEach(() => {
      this.cartForm.controls.products.push(
        new FormControl(1, { nonNullable: true })
      );
    });
  }
}
