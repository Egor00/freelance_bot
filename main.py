import _thread

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot import bot, update_data_loop

# _thread.start_new_thread(crawl, ('python',))
# _thread.start_new_thread(bot.polling, ())
# update_data_loop()
bot.polling()



'''user = User(id=2323)
user1 = User(id=5544, subscribed=False)
session.add(user)
session.add(user1)
session.commit()

users = session.query(User)
for i in users:
    # print(f'id={i.id}   sub = {i.subscribed}  last_post_date = {i.last_post_date}  govno = {i.sub_pars}')
    print(i)
user.subscribed = False
session.commit()
print()
print()
print(session.query(User).get(1))

for i in users:
    session.delete(i)
session.commit()

'''


