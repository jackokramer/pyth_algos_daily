class Weapon():
    def __init__(self, name, power, durabilty, weight):
        self.name = name
        self.power = power # 0 to 100
        self.durabilty = durabilty # durability between 0 and 1
        self.weight = weight # between 0 and 100

    def damage(self):
        return (self.power * self.durabilty)




class Player():
    def __init__(self, player, player_move, weapon): ## method used to create an instance
        self.name = player
        self.move = player_move
        self.weapons = weapon
        self.health = 100
## self refered to your instance)
    def attack(self, other_player):
        other_player.health -=10
        self.weapons.durabilty -= .1
        print(f"{self.name} attacked {other_player.name} with {self.weapons}.")
        return self
# #return self at the end of a function enables chaining.
    def heal(self):
        self.health +=10
        print(f"{self.name} used a healing potion to regenreate +10 health")
    def defeat(self):
        if self.health <= 0:
            return print(f'{self.name} has been eliminated.')
    def stats(self):
        print(f'name: {self.name}, HP:{self.health}')


upper_cut = Weapon('uppercut', 20, 3, 4)
smack_talk = Weapon('smack_talk', 5, 2, 1)
criss_cross = Weapon('criss_cross', 2, 1, 1)
ball = Weapon('ball', 10, 2, 2)

##instance below
jack = Player('Jack', upper_cut, 'stick')
krista = Player('Krysta', smack_talk, 'knife')
susan = Player('Suzzie', criss_cross, 'cross')

kylian = Player('Kylian', ball, 'cleats')

# print(jack.name)
# print(krista.weapons.power)
# print(susan.weapons. weight)
# print(kylian.weapons.durability)

# jack.weapons = 'fins'

# print(jack.weapons)

# jack.attack(kylian)
# print(kylian.health)
# kylian.heal()
# print(kylian.heal)

print("welcome to our Fighter Game")
name = input(name)

jack.attack(kylian).attack(kylian)
kylian.attack(susan).attack(krista)
jack.stats
krista.stats