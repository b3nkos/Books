import { Component, computed, inject, Signal, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Observable } from 'rxjs';
import { APP_SETTINGS, appSettings } from './app.settings';
import { CopyrightDirective } from './copyright.directive';
import { ProductListComponent } from "./product-list/product-list.component";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ProductListComponent, CopyrightDirective],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [{ provide: APP_SETTINGS, useValue: appSettings }],
})
export class AppComponent {
  title: Signal<string> = signal('');
  description = 'Hello World';
  settings = inject(APP_SETTINGS);
  currentDate = signal(new Date());

  title$ = new Observable((observer) => {
    setInterval(() => {
      observer.next(true);
    }, 2000);
  });

  constructor() {
    this.title$.subscribe(this.setTitle);
    this.title = computed(() => {
      return `${this.settings.title} (${this.currentDate()})`
    });
  }

  private setTitle = () => {
    this.currentDate.set(new Date());
  };
}
