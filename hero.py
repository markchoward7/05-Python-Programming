class SuperHero:

    def __init__(self, hero_name, real_name, powers):
        self.hero_name = hero_name
        self.real_name = real_name
        self.powers = powers

    def __repr__(self):
        return f'SuperHero({self.hero_name}, {self.real_name}, {self.powers})'
        
class Powers:

    def __init__(self, power_name, power_desc):
        self.power_name = power_name
        self.power_desc = power_desc
    
    def __repr__(self):
        return f'Powers({self.power_name}, {self.power_desc})'

def main():
    power = Powers("Flight I", "Can fly at speeds up to 50mph.")
    powers = {power.power_name : power}
    power = Powers("Flight II", "Can fly at speeds up to 200mph.")
    powers[power.power_name] = power
    power = Powers("Flight III", "Can fly at speeds up to 800mph.")
    powers[power.power_name] = power
    power = Powers("Indestructible", "Can't be hurt.")
    powers[power.power_name] = power
    power = Powers("Super Strength I", "Can punch through a brick wall.")
    powers[power.power_name] = power
    power = Powers("Super Strength II", "Can pick up a jumbo jet.")
    powers[power.power_name] = power
    power = Powers("Laser Eyes", "Shoots friggen laser beams out of their friggen eyes")
    powers[power.power_name] = power
    power = Powers("Rich", "Has a lot of money")
    powers[power.power_name] = power
    power = Powers("Regeneration", "Heals injuries rapidly")
    powers[power.power_name] = power

    superman = SuperHero("Superman", "Kal-El", [powers["Flight III"], powers["Indestructible"], powers["Super Strength II"], powers["Laser Eyes"]])
    batman = SuperHero("Batman", "Bruce Wayne", [powers["Rich"]])
    wolverine = SuperHero("Wolverine", "Logan", [powers["Super Strength I"], powers["Regeneration"]])

    print(superman)
    print(batman)
    print(wolverine)

main()
