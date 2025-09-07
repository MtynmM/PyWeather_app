from typing import TYPE_CHECKING
from PIL import ImageTk, Image 
import requests

if TYPE_CHECKING:
    from ..models.weather_service import WeatherService
    from ..views.main_view import MainView


class AppController:
    def __init__(self, model: "WeatherService", view: "MainView") -> None:
        self.model = model
        self.view = view
        self._bind_event()

    def _bind_event(self) -> None:
        self.view.search_button.config(command=self._on_search)

    def _on_search(self) -> None:
        location = self.view.city_entry.get()
        weather_data = self.model.get_weather(location)

        if weather_data:
            icon_url = weather_data["current"]["condition"]["icon"]
            image_response = requests.get(f"https:{icon_url}", stream=True)
            image_response.raise_for_status()
            
            image_data = Image.open(image_response.raw)
            photo = ImageTk.PhotoImage(image_data)
            
            self.view.icon_label.config(image=photo)
            self.view.icon_label.image = photo

            location_name = weather_data["location"]["name"]
            temp_c = weather_data["current"]["temp_c"]
            condition_text = weather_data["current"]["condition"]["text"]

            self.view.location_label.config(text=location_name)
            self.view.temp_label.config(text=f"{temp_c}°C")
            self.view.condition_label.config(text=condition_text)
        else:
             self.view.location_label.config(text="شهر یافت نشد")
             self.view.temp_label.config(text="")
             self.view.condition_label.config(
             text="لطفا نام شهر را صحیح و به انگلیسی وارد کنید"
             )
             self.view.icon_label.config(image="")
             self.view.icon_label.image = None
