'''Create a class Battle where two Player objects fight. Each player has name and power.
 The method fight() compares power and declares the winner.'''
class Player:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def fight(self):
        if self.player1.power > self.player2.power:
            print(f"{self.player1.name} wins the battle!")
        elif self.player2.power > self.player1.power:
            print(f"{self.player2.name} wins the battle!")
        else:
            print("It's a tie!")

# Create player objects
p1 = Player("Ali", 80)
p2 = Player("Zara", 90)

# Start the battle
match = Battle(p1, p2)
match.fight()