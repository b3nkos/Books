import { inject, Injectable } from '@angular/core';
import { Cart } from './cart';
import { APP_SETTINGS } from './app.settings';
import { HttpClient } from '@angular/common/http';
import { defer, map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CartService {
  cart: Cart | undefined;
  private cartUrl = `${inject(APP_SETTINGS).apiUrl}/carts`;

  constructor(private http: HttpClient) {}

  addProduct(id: number): Observable<Cart> {
    const cartProduct = { productId: id, quantity: 1 };

    return defer(() => {
      if (this.cart) {
        return this.http.put<Cart>(`${this.cartUrl}/${this.cart.id}`, {
          products: [...this.cart.products, cartProduct],
        });
      }
      return this.http.post<Cart>(this.cartUrl, { products: [cartProduct] });
    }).pipe(map((cart) => (this.cart = cart)));
  }
}
