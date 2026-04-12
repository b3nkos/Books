import { AfterViewInit, Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { APP_SETTINGS, appSettings } from './app.settings';
import { AuthComponent } from './auth/auth.component';
import { CopyrightDirective } from './copyright.directive';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    CopyrightDirective,
    AuthComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [{ provide: APP_SETTINGS, useValue: appSettings }],
})
export class AppComponent implements AfterViewInit {
  settings = inject(APP_SETTINGS);
  title = '';

  ngAfterViewInit(): void {
    this.title = this.settings.title;
  }
}
