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

accs = ['ileana_official','kartikaaryan','janhvikapoor','saraalikhan95','aishwaryaraibachchan_arb','bipashabasu','egupta']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=7, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1500) 

#####################################################################################################################

accs = ['sachintendulkar','virat.kohli','mahi7781']
count = 0
while (count < 20):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=3, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1000) 


#####################################################################################################################
accs = ['sidmalhotra','twinklerkhanna','nargisfakhri','diamirzaofficial','madhuridixitnene','badboyshah']
count = 0
while (count < 20):
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(2000)


######################################################################################################
accs = ['norafatehi','mohanshakti','raghavjuyal','remodsouza','dharmesh0011','malaikaaroraofficial','manushi_chhillar']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=7, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1700)
#####################################################################################################################

accs = ['amitabhbachchan','bachchan','manishmalhotra05','karanjohar','kapilsharma','theshilpashetty']
count = 0
while (count < 18):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1900) 
###############################################################################################################
accs = ['priya.p.varrier','anushkashettyofficial','tamannaahspeaks','kajalaggarwalofficial','shrutzhaasan']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=6000, sleep_delay=17, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping ")

time.sleep(1800) 

#####################################################################################################################

accs = ['deepikapadukone','priyankachopra','aliaabhatt','shraddhakapoor','akshaykumar']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

#####################################################################################################################

accs = ['jacquelinef143','anushkasharma','beingsalmankhan','parineetichopra']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=4, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

#####################################################################################################################

accs = ['shahidkapoor','sonamkapoor','sunnyleone','varundvn','iamsrk']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=13, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=11, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

#####################################################################################################################

accs = ['ranveersingh','hrithikroshan','dishapatani','katrinakaif','kritisanon','aslisona']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

#####################################################################################################################

accs = ['narendramodi','kanik4kapoor','shreyaghoshal','urvashirautela','nehakakkar']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=14, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

time.sleep(1800) 

#####################################################################################################################

accs = ['diljitdosanjh','sushmitasen47','realhinakhan','rannvijaysingha','darshanravaldz']
count = 0
while (count < 15):
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=14, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

time.sleep(1800) 
#####################################################################################################################

accs = ['mostlysane','bhuvan.bam22','technicalguruji','harshbeniwal']
count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=4, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

#####################################################################################################################
os.system("shutdown /s /t 1")

# end the bot session
session.end()
