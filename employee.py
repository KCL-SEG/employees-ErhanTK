"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=None, hourly_rate=None, hours_worked=None, bonus_commission=None, contract_commission=None, contracts_landed=None):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission
        self.contracts_landed = contracts_landed

    def get_pay(self):
        pay = 0
        if self.contract_type == 'salary':
            pay = self.salary
        elif self.contract_type == 'hourly':
            pay = self.hourly_rate * self.hours_worked
        
        if self.bonus_commission:
            pay += self.bonus_commission
        if self.contract_commission and self.contracts_landed:
            pay += self.contract_commission * self.contracts_landed

        return pay

    def __str__(self):
        description = f"{self.name} works on a "
        if self.contract_type == 'salary':
            description += f"monthly salary of {self.salary}"
        elif self.contract_type == 'hourly':
            description += f"contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

        if self.bonus_commission:
            description += f" and receives a bonus commission of {self.bonus_commission}"
        if self.contract_commission and self.contracts_landed:
            description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.contract_commission}/contract"

        description += f". Their total pay is {self.get_pay()}."
        return description

# Employee objects creation
billie = Employee('Billie', 'salary', salary=4000)
charlie = Employee('Charlie', 'hourly', hourly_rate=25, hours_worked=100)
renee = Employee('Renee', 'salary', salary=3000, contract_commission=200, contracts_landed=4)
jan = Employee('Jan', 'hourly', hourly_rate=25, hours_worked=150, contract_commission=220, contracts_landed=3)
robbie = Employee('Robbie', 'salary', salary=2000, bonus_commission=1500)
ariel = Employee('Ariel', 'hourly', hourly_rate=30, hours_worked=120, bonus_commission=600)

