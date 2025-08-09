import ttkbootstrap as ttk


class MainView(ttk.Window):
    def __init__(self) -> None:
        super().__init__(
            title="PyWeather APP(MTMO)",
            themename="superhero",
            resizable=(False, False),
        )

        self.geometry("400x500")

        search_frame = ttk.Frame(self)
        search_frame.pack(fill="x", padx=10, pady=10)

        self.city_entry = ttk.Entry(search_frame, font=("Arial", 12))
        self.city_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.search_button = ttk.Button(search_frame, text="جستجوی شهر مورد نظر")
        self.search_button.pack(side="right")

        result_frame = ttk.Frame(self)
        result_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.location_label = ttk.Label(result_frame, font=("Arial", 20))
        self.location_label.pack(pady=13)

        self.temp_label = ttk.Label(result_frame, font=("Arial", 50, "bold"))
        self.temp_label.pack(pady=10)

        self.condition_label = ttk.Label(result_frame, font=("Arial", 16))
        self.condition_label.pack(pady=5)
