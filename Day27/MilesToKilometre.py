import tkinter

def calculate():
    miles = int(entry_unit.get())
    km = miles * 1.60934
    km_int["text"] = km

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

equal_to = tkinter.Label(text="is equal to")
equal_to.grid(row=1, column=0)

entry_unit = tkinter.Spinbox(width=5, from_=0, to=1000000000, command=calculate)
entry_unit.grid(row=0, column=1)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

km_int = tkinter.Label(text=0)
km_int.grid(row=1, column=1)

km = tkinter.Label(text="Km")
km.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
