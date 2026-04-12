import { DatePipe, DecimalPipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { noop } from 'rxjs';
import { CurrentWeather } from '../interfaces';
import { WeatherServiceService } from '../weather/weather-service.service';

@Component({
  selector: 'app-current-weather',
  standalone: true,
  imports: [DecimalPipe, DatePipe],
  templateUrl: './current-weather.component.html',
  styleUrl: './current-weather.component.css'
})
export class CurrentWeatherComponent implements OnInit {
  currentWeather!: CurrentWeather

  constructor(private weatherService: WeatherServiceService) {}

  ngOnInit(): void {
    noop()
  }

}
