# Encapsulation - Wrapping data and functions into single unit
# Data hiding

class BankAccount:

    def __init__(self, Name, Balance):
        self.Name = Name          # Public
        self._Balance = Balance   # Protected
        self.__SecretBalance = Balance  # Private

    # Getter
    def get_balance(self):
        return self._Balance

    # Setter
    def set_balance(self, newBalance):
        self._Balance = newBalance
        self.__SecretBalance = newBalance


acc1 = BankAccount("Ronak", 10_000)
acc1.set_balance(20000)

# Public
print(acc1.Name)

# Protected (by convention)
print(acc1._Balance)

# Private (Name Mangling)
print(acc1._BankAccount__SecretBalance)
