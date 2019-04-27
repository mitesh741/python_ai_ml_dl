from instapy import InstaPy
import time 

insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()

print(time.ctime()) 

session.set_relationship_bounds(enabled=True,
				 potency_ratio=0.80,
				  delimit_by_numbers=False)

accs = ['virat.kohli','sachintendulkar','nehwalsaina','mahi7781','mirzasaniar','pvsindhu1','yuvisofficial','hardikpandya93']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=8, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['nehakakkar','shreyaghoshal','arijitsingh','arrahman','atifaslam','sunidhichauhan5','armaanmalik22','kanik4kapoor','shirleysetia','shadyblush']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=10, customList=(True, accs, "all"), style="FIFO", unfollow_after=15, sleep_delay=15)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['ipoonampandey','manushi_chhillar','urvashirautela','malaikaaroraofficial','coachsapna','yasminkarachiwala']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=15, sleep_delay=15)




# end the bot session
session.end()
