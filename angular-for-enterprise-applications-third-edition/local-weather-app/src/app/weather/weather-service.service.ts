import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { CurrentWeather } from '../interfaces';
import { environment } from '../../environments/environment';

interface CurrentWeatherData {
  weather: [
    {
      description: string
      icon: string
    }
  ]
  main: {
    temp: number
  }
  sys: {
    country: string
  }
  dt: number
  name: string
}

@Injectable({
  providedIn: 'root'
})
export class WeatherServiceService {

  constructor(private httpClient: HttpClient) {}

  getCurrentWeather(city: string, country: string): Observable<CurrentWeather> {
    const uriParams = new HttpParams()
    .set('q', `${city},${country}`)
    .set('appid', environment.appId);

    return this.httpClient.get<CurrentWeatherData>(`${environment.baseUrl}`, {params: uriParams})
    .pipe(map((data) => this.transformToCurrentWeather(data)));
  }

  private transformToCurrentWeather(data: CurrentWeatherData): CurrentWeather {
    return {
      city: data.name,
      country: data.sys.country,
      date: data.dt * 1000,
      image: `http://openweathermap.org/img/w/${data.weather[0].icon}.png`,
      temperature: this.convertKelvinToFahrenheit(data.main.temp),
      description: data.weather[0].description
    }
  }

  private convertKelvinToFahrenheit(kelvin: number): number {
    return (kelvin * 9) / 5 - 459.67;
  }
}
