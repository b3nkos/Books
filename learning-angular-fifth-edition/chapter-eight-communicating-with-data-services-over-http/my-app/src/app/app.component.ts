import { Component, inject } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { APP_SETTINGS, appSettings } from './app.settings';
import { CopyrightDirective } from './copyright.directive';
import { ProductListComponent } from "./product-list/product-list.component";
import { AuthComponent } from './auth/auth.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ProductListComponent, CopyrightDirective, AuthComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [{ provide: APP_SETTINGS, useValue: appSettings }],
})
export class AppComponent {
  settings = inject(APP_SETTINGS);
}
