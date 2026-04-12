import { Component, inject } from '@angular/core';
import { MatButton } from '@angular/material/button';
import { MatToolbar, MatToolbarRow } from '@angular/material/toolbar';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { APP_SETTINGS, appSettings } from './app.settings';
import { AuthComponent } from './auth/auth.component';
import { CopyrightDirective } from './copyright.directive';
import { MatBadge } from '@angular/material/badge';
import { CartService } from './cart.service';

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
    MatBadge
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
