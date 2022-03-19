class Hero:
    names = []
    population = 0
    def __init__(self, name):
        Hero.names.append(name)
        Hero.heroes = " , ".join(Hero.names)

        self.name = name
        print(f'Зашел в игру {self.name}')
    
        Hero.population += 1

        Hero.sayHi(self.name)
        Hero.HowMany()

    def __delattr__(self, item):
        print("--------------")
        print(f'\nПокинул игру {self.name}')
        
        Hero.population -= 1
        
        Hero.names.remove(self.name)
        Hero.heroes = " , ".join(Hero.names)

        if Hero.population == 0:
            print('Это был последний герой.')


        else:
            print(f'Количество героев {Hero.population}')
      
    def sayHi(name):
        print(f'Вас приветствует {name}')
          
    @classmethod
    def HowMany(cls):
        print(f'В игре: {cls.population} \n')
    
        
    
hero1 = Hero('Zeus')
hero2 = Hero('Lion')
hero3 = Hero('Snake')


def kick():
    while Hero.population:        
        print(f"Герои: {Hero.heroes}")
        x = input(f'Исключить из игры - введите название героя из списка:\n')
        if x == hero1.name:
            del hero1.name
            print(f"\n{Hero.heroes} - повезло и они остались в игре.")
            continue

        elif x == hero2.name:
            del hero2.name
            print(f"\n{Hero.heroes} - повезло и они остались в игре.")
            continue
        
        elif x == hero3.name:
            del hero3.name
            print(f"\n{Hero.heroes} - повезло и они остались в игре.")
            continue

        else:
            print('Вы никого не исключили.')
            break


def main():
        kick()

if __name__ == "__main__":
    main()



