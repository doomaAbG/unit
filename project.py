import tkinter as tk
from tkinter import ttk

# Хэш-таблица с единицами преобразования
conversion_map = {
    "Miles": {"Kilometers": lambda x: x * 1.60934},
    "Kilometers": {"Miles": lambda x: x / 1.60934},
    "Meters": {"Feet": lambda x: x * 3.28084, "Yards": lambda x: x / 0.9144},
    "Feet": {"Meters": lambda x: x / 3.28084},
    "Yards": {"Meters": lambda x: x * 0.9144},
    "Inches": {"Centimeters": lambda x: x * 2.54},
    "Centimeters": {"Inches": lambda x: x / 2.54},
    "Pounds": {"Kilograms": lambda x: x * 0.453592},
    "Kilograms": {"Pounds": lambda x: x / 0.453592, "Tons": lambda x: x / 1000},
    "Grams": {"Ounces": lambda x: x * 0.035274},
    "Ounces": {"Grams": lambda x: x / 0.035274},
    "Tons": {"Kilograms": lambda x: x * 1000},
    "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9},
    "Celsius": {"Fahrenheit": lambda x: (x * 9/5) + 32},
    "Liters": {"Gallons": lambda x: x * 0.264172},
    "Gallons": {"Liters": lambda x: x / 0.264172},
    "Cubic Meters": {"Cubic Feet": lambda x: x * 35.3147},
    "Cubic Feet": {"Cubic Meters": lambda x: x / 35.3147},
    "Kilometers per Hour": {"Miles per Hour": lambda x: x * 0.621371},
    "Miles per Hour": {"Kilometers per Hour": lambda x: x / 0.621371},
    "Square Meters": {"Square Feet": lambda x: x * 10.7639},
    "Square Feet": {"Square Meters": lambda x: x / 10.7639},
}

def update_to_units(event):
    selected_unit = unit_from_var.get()
    if selected_unit in conversion_map:
        combo_to["values"] = list(conversion_map[selected_unit].keys())
        combo_to.set("")
    else:
        combo_to["values"] = []
        combo_to.set("")

def convert():
    unit_from = unit_from_var.get()
    unit_to = unit_to_var.get()
    try:
        value = float(entry_value.get())
    except ValueError:
        label_result.config(text="Invalid input. Please enter a number.")
        return
    if unit_from in conversion_map and unit_to in conversion_map[unit_from]:
        result = conversion_map[unit_from][unit_to](value)
        result_text = f"{value} {unit_from} = {result:.2f} {unit_to}"
        label_result.config(text=result_text)
        history_listbox.insert(0, result_text)
    else:
        label_result.config(text="Invalid conversion")

def clear():
    entry_value.delete(0, tk.END)
    unit_from_var.set("")
    unit_to_var.set("")
    label_result.config(text="")
    combo_to["values"] = []
    combo_to.set("")

# Создание главного окна
root = tk.Tk()
root.title("Russian Converter")
root.geometry("400x500")  # Увеличили высоту до 500 пикселей
root.configure(bg="#f0f4f7")

# Основной фрейм
input_frame = ttk.Frame(root, padding="10", relief="solid", borderwidth=1)
input_frame.pack(pady=10, padx=10, fill="x")
result_frame = ttk.Frame(root, padding="10", relief="solid", borderwidth=1)
result_frame.pack(pady=10, padx=10, fill="x")
history_frame = ttk.Frame(root, padding="10", relief="solid", borderwidth=1)
history_frame.pack(pady=10, padx=10, fill="x", expand=True)  # Добавили expand=True

# Поле ввода значения
label_value = ttk.Label(input_frame, text="Значение которое нужно изменить", background="#f0f4f7")
label_value.pack(pady=5)
entry_value = ttk.Entry(input_frame, font=("Arial", 12))
entry_value.pack(pady=5)

# Поле "Конвертировать из"
label_from = ttk.Label(input_frame, text="Конвертировать из:", background="#f0f4f7")
label_from.pack(pady=5)
unit_from_var = tk.StringVar()
combo_from = ttk.Combobox(input_frame, textvariable=unit_from_var, font=("Arial", 10))
combo_from["values"] = list(conversion_map.keys())
combo_from.bind("<<ComboboxSelected>>", update_to_units)
combo_from.pack(pady=5)

# Поле "Конвертировать в"
label_to = ttk.Label(input_frame, text="Конвертировать в:", background="#f0f4f7")
label_to.pack(pady=5)
unit_to_var = tk.StringVar()
combo_to = ttk.Combobox(input_frame, textvariable=unit_to_var, font=("Arial", 10))
combo_to.pack(pady=5)

# Стили для кнопок
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5, background="#007bff", foreground="#000000")
style.map("TButton",
          background=[("active", "#0056b3"), ("!active", "#007bff")],
          foreground=[("active", "#000000"), ("!active", "#000000")],
          relief=[("active", "sunken"), ("!active", "raised")])

style.configure("Clear.TButton", font=("Arial", 12), padding=5, background="#007bff", foreground="#000000", 
                borderwidth=2, relief="solid")
style.map("Clear.TButton",
          background=[("active", "#0056b3"), ("!active", "#007bff")],
          foreground=[("active", "#000000"), ("!active", "#000000")],
          relief=[("active", "solid"), ("!active", "solid")],
          bordercolor=[("active", "#ff0000"), ("!active", "#ff0000")])

# Кнопки
button_frame = ttk.Frame(input_frame)
button_frame.pack(pady=10)
button_convert = ttk.Button(button_frame, text="Конвертация", command=convert, style="TButton")
button_convert.pack(side="left", padx=5)
button_clear = ttk.Button(button_frame, text="Очистить", command=clear, style="Clear.TButton")
button_clear.pack(side="left", padx=5)

# Результат
label_result = ttk.Label(result_frame, text="", font=("Arial", 14), background="#f0f4f7", foreground="#000000")
label_result.pack(pady=10)

# История
label_history = ttk.Label(history_frame, text="История:", background="#f0f4f7")
label_history.pack(pady=5)
history_listbox = tk.Listbox(history_frame, height=5, font=("Arial", 10))
history_listbox.pack(fill="x", expand=True)  # Добавили expand=True

root.mainloop()