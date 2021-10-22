from main import Bot, NoMoreUsers
from random import randint
import csv

users_to_retrieve = ['applephoneofc', 'inspiracaonosestudos', 'engfuncional']
f = open('links')
link_comentario = list(csv.reader(f))

bot = Bot(username='roboinsta0@gmail.com', password='rabanete123!', links=link_comentario, file_name='followers_0.csv')

try:
    bot.run()

except NoMoreUsers:
    bot.get_followers(usuario=users_to_retrieve[randint(0, len(users_to_retrieve))], quantidade=1000)
