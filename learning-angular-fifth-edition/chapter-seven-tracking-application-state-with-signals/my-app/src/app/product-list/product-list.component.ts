import {
  Component,
  inject
} from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { Observable } from 'rxjs';
import { Product } from '../product';
import { ProductDetailComponent } from '../product-detail/product-detail.component';
import { ProductsService } from '../products.service';
import { SortPipe } from '../sort.pipe';

@Component({
  selector: 'app-product-list',
  imports: [ProductDetailComponent, SortPipe],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css',
  providers: [ProductsService],
})
export class ProductListComponent {
  selectedProduct: Product | undefined;
  products = toSignal(inject(ProductsService).getProducts(), {
    initialValue: []
  });

  onAdded() {
    alert(`${this.selectedProduct?.title} added to the cart!`);
  }

}
