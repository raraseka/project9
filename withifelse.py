hours = input("Enter Hours:")
try:
    hours = float(hours) #mengubah input jam kerja menjadi angka
except ValueError:
    print("Error, please enter numeric input for Rate")
    exit() #menghentikan program jika input tidak valid
    
rate = input("Enter Rate:")
try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit() #menghentikan program jika input tidak valid

if hours < 50:
    pay = round(hours * rate,2)
else:
    overtime = hours - 50
    pay = round(50 * rate + overtime * rate * 1.5,2)
print(f"Pay: {pay: .2f}")
