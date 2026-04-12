import { Component, inject } from '@angular/core';
import { MatBadge } from '@angular/material/badge';
import { MatButton } from '@angular/material/button';
import { MatToolbar, MatToolbarRow } from '@angular/material/toolbar';
import { RouterLink, RouterOutlet } from '@angular/router';
import { APP_SETTINGS, appSettings } from './app.settings';
import { AuthComponent } from './auth/auth.component';
import { CartService } from './cart.service';
import { CopyrightDirective } from './copyright.directive';
import { FeaturedComponent } from './featured/featured.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    RouterLink,
    CopyrightDirective,
    AuthComponent,
    MatToolbar,
    MatToolbarRow,
    MatButton,
    MatBadge,
    FeaturedComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [{ provide: APP_SETTINGS, useValue: appSettings }],
})
export class AppComponent {
  settings = inject(APP_SETTINGS);
  title = '';
  cartService = inject(CartService);
}
