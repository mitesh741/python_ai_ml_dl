from instapy import InstaPy
import time 
import os
insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()

print(time.ctime()) 

session.set_relationship_bounds(enabled=True,potency_ratio=0.80, delimit_by_numbers=False)

#####################################################################################################################
accs = ['kyliejenner','selenagomez','cristiano','therock','arianagrande','kimkardashian']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=6000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping ")

time.sleep(1000) 

###############################################################################################################

accs = ['beyonce','taylorswift','neymarjr','leomessi','justinbieber','kendalljenner']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1000) 

#####################################################################################################################

accs = ['natgeo','nickiminaj','khloekardashian','jlo','nike']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1000) 

#####################################################################################################################
accs = ['mileycyrus','katyperry','kourtneykardash','ddlovato','kevinhart4real']
count = 0
while (count < 20):
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=12, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1200)


######################################################################################################
accs = ['realmadrid','badgalriri','theellenshow','fcbarcelona','victoriassecret']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=13, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1000)
#####################################################################################################################
'''
accs = ['','','','','']
count = 0
while (count < 18):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=20, interact=False)
    session.unfollow_users(amount=2, customList=(True, accs, "all"), style="FIFO", unfollow_after=20, sleep_delay=20)

print("Sleeping for half an hour")
time.sleep(1100) 


#####################################################################################################################

accs = ['shahidkapoor','sonamkapoor','sunnyleone','varundvn','iamsrk']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=13, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=11, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1000) 

#####################################################################################################################

accs = ['ranveersingh','hrithikroshan','dishapatani','katrinakaif','kritisanon','aslisona']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1100) 

#####################################################################################################################

accs = ['narendramodi','shreyaghoshal','urvashirautela','nehakakkar']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=14, interact=False)
    session.unfollow_users(amount=4, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

#####################################################################################################################
'''
os.system("shutdown /s /t 1")

# end the bot session
session.end()
