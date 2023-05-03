from tkinter import *
import json
import os

root = Tk()

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
    result_output['text']=str(result)+' руб'

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



root['bg'] = '#008080'
root.title('3D_price')
root.geometry('600x400')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=400, width=600)

frame = Frame(root, bg='#008080')
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

heading = Label(frame, text='Введите параметры:',
                bg='#008080', font='Times 20')
heading.grid(column=0, row=0)

mass_title = Label(frame, text='Вес модели, гр',
                   bg='#008080', font='Times 14')
mass_title.grid(column=0, row=1,sticky='w')

mass_input=Entry(frame,justify='center')
mass_input.grid(ipadx=63,columnspan=2,column=1, row=1,sticky='e')

time_title = Label(frame, text='Время печати',
                   bg='#008080', font='Times 14')
time_title.grid(column=0, row=2,sticky='w')

time_h_input=Entry(frame,justify='center',text='часов')
time_h_input.grid(column=1, row=2,sticky='e')
time_h_input.insert(0,'часов')

time_m_input=Entry(frame,justify='center',text='минут')
time_m_input.grid(column=2, row=2,sticky='e')
time_m_input.insert(0,'минут')

price_fl_title = Label(frame, text='Цена пластика, руб/кг',
                       bg='#008080', font='Times 14')
price_fl_title.grid(column=0, row=3,sticky='w')

price_fl_input=Entry(frame,justify='center')
price_fl_input.grid(ipadx=63,columnspan=2,column=1, row=3,sticky='e')

price_energy_title = Label(frame, text='Цена электроэнергии, руб/час',
                           bg='#008080', font='Times 14')
price_energy_title.grid(column=0, row=4,sticky='w')

price_energy_input=Entry(frame,justify='center')
price_energy_input.grid(ipadx=63,columnspan=2,column=1, row=4,sticky='e')

price_printer_title = Label(frame, text='Цена 3D принтера, руб',
                            bg='#008080', font='Times 14')
price_printer_title.grid(column=0, row=5,sticky='w')

price_printer_input=Entry(frame,justify='center')
price_printer_input.grid(ipadx=63,columnspan=2,column=1, row=5,sticky='e')

power_title = Label(frame, text='Мощность принтера, Вт',
                    bg='#008080', font='Times 14')
power_title.grid(column=0, row=6,sticky='w')

power_input=Entry(frame,justify='center')
power_input.grid(ipadx=63,columnspan=2,column=1, row=6,sticky='e')

ratio_title = Label(frame, text='Коэффициент сложности',
                    bg='#008080', font='Times 14')
ratio_title.grid(column=0, row=7,sticky='w')

ratio_input=Entry(frame,justify='center')
ratio_input.grid(ipadx=63,columnspan=2,column=1, row=7,sticky='e')

result_title = Label(frame, text='Итоговая цена:',
                     bg='#008080', font='Times 14')
result_title.grid(column=0, row=8,sticky='w')

result_output=Label(frame,justify='left',bg='#008080',font='Times 14')
result_output.grid(columnspan=2,column=1, row=8,sticky='w')

button = Button(frame, text='Рассчитать',
                    bg='#007380', font='Times 14',command=btn_click)
button.grid(column=0, row=9,sticky='w')

data_load()

root.mainloop()
