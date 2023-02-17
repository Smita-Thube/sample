class Tata:
    def first_car(self):
        print('launched in 1991,First Indian Passenger.')
class Indica(Tata):
    def second_car(self):
        print('launched in 1998,secong Indian Passenger Car.')
class Punch(Indica):
    def third_car(self):
        print('launched version car,eco-friendly.')
class Safari(Punch):
    def fourth_car(self):
        print("launched new fourth version car,runs in Desert.")
class Nexon(Safari):
    def fifth_car(self):
        print('launched fifth-version car, Eco-friendly.')
t1=Nexon()
t1.fifth_car()
t1.fourth_car()
t1.third_car()
t1.second_car()
t1.first_car()
t2=Punch()
#t2.fourth_car()
t2.third_car()
t2.first_car()