class Hero:
    population = 0
    
    def __init__(self, name):
        self.name = name
        print(f'Зашел в игру {self.name}')
    
        Hero.population += 1
        
    def delete(self, ):
        print(f'Покинул игру {self.name}')
        
        Hero.population -= 1
        
        if Hero.population == 0:
            print('Это был последний герой.')
            
        else:
            print(f'Количество героев {Hero.population}')
        
    def sayHi(self, ):
        print(f'Вас приветствует {self.name}')
        
    def HowMany():
        print(f'В игре: {Hero.population} \n')
        
    HowMany = staticmethod(HowMany)
    
hero1 = Hero('Zeus')
hero1name = 'Zeus'
hero1.sayHi()
Hero.HowMany()

hero2 = Hero('Lion')
hero2name = 'Lion'
hero2.sayHi()
Hero.HowMany()


def kill(x = input('Исключить из игры - введите "Zeus" или "Lion":')):
    if x == 'Zeus':
            hero1.delete()
            print(f'\n{hero2name} повезло и он остался в игре.')

    elif x == 'Lion':
            hero2.delete()
            print(f"\n{hero1name} повезло и он остался в игре.")

    else:
            print('Вы никого не исключили.')



kill()
Hero.HowMany()


