from easygui import *

def calculator():
    # Sisesta kaks täisarvu lõigus 1-10
    num1 = integerbox("Sisesta esimene täisarv (1-10):", "Kalkulaator", lowerbound=1, upperbound=10)
    num2 = integerbox("Sisesta teine täisarv (1-10):", "Kalkulaator", lowerbound=1, upperbound=10)

    if num1 is None or num2 is None:
        easygui.msgbox("Kalkulatsioon katkestati.", "Kalkulaator")
        return

    # Valik liitmise, lahutamise või korrutamise vahel
    operation = buttonbox("Vali tehe:", "Kalkulaator", choices=["Liitmine", "Lahutamine", "Korrutamine"])

    if operation == "Liitmine":
        result = num1 + num2
        message = f"{num1} + {num2} = {result}"
    elif operation == "Lahutamine":
        result = num1 - num2
        message = f"{num1} - {num2} = {result}"
    elif operation == "Korrutamine":
        result = num1 * num2
        message = f"{num1} * {num2} = {result}"
    else:
        message = "Tehe katkestati."

    # Kuvab arvutuse tulemuse
    msgbox(message, "Kalkulaator")

if __name__ == "__main__":
    calculator()
