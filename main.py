import customtkinter
import json
# from UI import UI_init, app
# from logic import data_load
import os



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry("620x390")
app.title('3D_price')
app.iconbitmap('icon.ico')

def btn_click():
    mass = int(mass_input.get())
    time_h = int(time_h_input.get())
    time_m = int(time_m_input.get())
    price_fl = float(price_fl_input.get())
    price_energy = float(price_energy_input.get())
    price_printer = float(price_printer_input.get())
    power = int(power_input.get())
    ratio = float(ratio_input.get())

    result = int(((mass / 1000 * price_fl) + (power / 1000 * price_energy * ((time_m / 60)+time_h)) + (((time_m / 60 + time_h)) * (price_printer/365/8))) * 3 * ratio)
    result_output.configure(text=str(result)+' руб')

    data = {
    "price_fl":price_fl,
    "price_energy":price_energy,
    "price_printer":price_printer,
    "power":power,
    "ratio":ratio
    }

    with open('data.json', 'w') as f:
        json.dump(data, f,indent=2)

def data_load():
    if (os.path.isfile('data.json'))!=True:
        data = {
            "price_fl":1500,
            "price_energy":4,
            "price_printer":20000,
            "power":300,
            "ratio":1
            }
        with open('data.json', 'w') as f:
            json.dump(data, f,indent=2)

    with open('data.json', 'r') as f:
        data_dict=json.load(f)

    price_fl_input.insert(0,data_dict.get('price_fl'))
    price_energy_input.insert(0,data_dict.get('price_energy'))
    price_printer_input.insert(0,data_dict.get('price_printer'))
    power_input.insert(0,data_dict.get('power'))
    ratio_input.insert(0,data_dict.get('ratio'))

padx_label=(20,10)
padx_entry=10

frame = customtkinter.CTkFrame(master=app)
frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

heading = customtkinter.CTkLabel(frame, text='Введите параметры:',font=customtkinter.CTkFont(size=20, weight="bold"),justify=customtkinter.CENTER)
heading.grid(column=0, row=0,pady=(15,15),columnspan=2)

mass_title = customtkinter.CTkLabel(frame, text='Вес модели, гр',font=customtkinter.CTkFont(size=16, weight="normal"))
mass_title.grid(column=0, row=1,sticky='w',padx=padx_label)

mass_input=customtkinter.CTkEntry(frame,justify=customtkinter.CENTER)
mass_input.grid(ipadx=70,columnspan=2,column=1, row=1,padx=(2,padx_entry))

time_title = customtkinter.CTkLabel(frame, text='Время печати',font=customtkinter.CTkFont(size=16, weight="normal"))
time_title.grid(column=0, row=2,sticky='w',padx=padx_label)

time_input=customtkinter.CTkFrame(master=frame)
time_input.grid(column=1, row=2)

time_h_input=customtkinter.CTkEntry(time_input,justify=customtkinter.CENTER,placeholder_text='часов')
time_h_input.grid(column=0, row=0)

time_m_input=customtkinter.CTkEntry(time_input,justify=customtkinter.CENTER,placeholder_text='минут')
time_m_input.grid(column=1, row=0)

price_fl_title = customtkinter.CTkLabel(frame, text='Цена пластика, руб/кг',font=customtkinter.CTkFont(size=16, weight="normal"))
price_fl_title.grid(column=0, row=3,sticky='w',padx=padx_label)

price_fl_input=customtkinter.CTkEntry(frame,justify=customtkinter.CENTER)
price_fl_input.grid(ipadx=70,columnspan=2,column=1, row=3,padx=(2,padx_entry))

price_energy_title = customtkinter.CTkLabel(frame, text='Цена электроэнергии, руб/час',font=customtkinter.CTkFont(size=16, weight="normal"))
price_energy_title.grid(column=0, row=4,sticky='w',padx=padx_label)

price_energy_input=customtkinter.CTkEntry(frame,justify=customtkinter.CENTER)
price_energy_input.grid(ipadx=70,columnspan=2,column=1, row=4,padx=(2,padx_entry))

price_printer_title = customtkinter.CTkLabel(frame, text='Цена 3D принтера, руб',font=customtkinter.CTkFont(size=16, weight="normal"))
price_printer_title.grid(column=0, row=5,sticky='w',padx=padx_label)

price_printer_input=customtkinter.CTkEntry(frame,justify=customtkinter.CENTER)
price_printer_input.grid(ipadx=70,columnspan=2,column=1, row=5,padx=(0,padx_entry))

power_title = customtkinter.CTkLabel(frame, text='Мощность принтера, Вт',font=customtkinter.CTkFont(size=16, weight="normal"))
power_title.grid(column=0, row=6,sticky='w',padx=padx_label)

power_input=customtkinter.CTkEntry(frame,justify=customtkinter.CENTER)
power_input.grid(ipadx=70,columnspan=2,column=1, row=6,padx=(2,padx_entry))

ratio_title = customtkinter.CTkLabel(frame, text='Коэффициент сложности',font=customtkinter.CTkFont(size=16, weight="normal"))
ratio_title.grid(column=0, row=7,sticky='w',padx=padx_label)

ratio_input=customtkinter.CTkEntry(frame,justify=customtkinter.CENTER)
ratio_input.grid(ipadx=70,columnspan=2,column=1, row=7,padx=(2,padx_entry))

result_title = customtkinter.CTkLabel(frame, text='Итоговая цена:',font=customtkinter.CTkFont(size=16, weight="normal"))
result_title.grid(column=0, row=8,sticky='w',padx=padx_label)

result_output=customtkinter.CTkLabel(frame,justify=customtkinter.CENTER,text='0 руб',font=customtkinter.CTkFont(size=16, weight="bold"))
result_output.grid(columnspan=2,column=1, row=8,padx=padx_label,pady=(10,0))

button = customtkinter.CTkButton(frame, text='Рассчитать',command=btn_click,font=customtkinter.CTkFont(size=16, weight="bold"))
button.grid(column=0, row=9,pady=(15,15),columnspan=2)

data_load()

app.mainloop()
