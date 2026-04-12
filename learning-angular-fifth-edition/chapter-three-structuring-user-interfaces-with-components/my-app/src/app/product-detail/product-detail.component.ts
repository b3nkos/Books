import {
  ChangeDetectionStrategy,
  Component,
  input,
  OnChanges,
  OnDestroy,
  OnInit,
  output,
  SimpleChanges,
  ViewEncapsulation,
} from '@angular/core';
import { Product } from '../product';

@Component({
  selector: 'app-product-detail',
  imports: [],
  templateUrl: './product-detail.component.html',
  styleUrl: './product-detail.component.css',
  encapsulation: ViewEncapsulation.Emulated,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ProductDetailComponent implements OnInit, OnDestroy, OnChanges {
  product = input<Product>();
  added = output<Product>();

  constructor() {
    console.log('Product:', this.product());
  }

  ngOnInit(): void {
    console.log('Product:', this.product());
  }

  ngOnDestroy(): void {
    throw new Error('Method not implemented.');
  }

  ngOnChanges(changes: SimpleChanges): void {
    const product = changes['product'];

    if (product.isFirstChange()) {
      return;
    }
    
    const oldValue = product.previousValue;
    const newValue = product.currentValue;
    console.log('Old Value', oldValue);
    console.log('New Value', newValue);
  }

  get productTitle() {
    return this.product()!.title;
  }

  addToCart() {
    this.added.emit(this.product()!);
  }
}
