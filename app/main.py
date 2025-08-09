from .models.weather_service import WeatherService
from .views.main_view import MainView
from .controllers.app_controller import AppController


class App:
    def __init__(self) -> None:
        self.model = WeatherService()
        self.view = MainView()

        self.controller = AppController(self.model, self.view)

        self.view.mainloop()


if __name__ == "__main__":
    app = App()
