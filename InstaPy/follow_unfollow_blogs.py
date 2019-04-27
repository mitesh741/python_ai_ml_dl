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
                  
accs = ['bewakoofofficial','the.realshit.gyan','theindianidiot','tvfqtiyapa','wearyouropinion']
count = 0
while (count < 10):     
    count = count + 1
    session.follow_by_list(accs,times=6000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=15, sleep_delay=15)

print("Sleeping for half an hour")
time.sleep(100)



accs = ['filtercopy','scoopwhoop','officialhumansofbombay','buzzfeedindia','ttt_official']
count = 0
while (count < 10):
    count = count + 1
    session.follow_by_list(accs,times=6000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=20, sleep_delay=15)

'''
time.sleep(1800) 


accs = ['mostlysane','bhuvan.bam22','technicalguruji','harshbeniwal']
count = 0
while (count < 30):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=4, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['deepikapadukone','priyankachopra','aliaabhatt','shraddhakapoor','akshaykumar']
count = 0
while (count < 30):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['jacquelinef143','anushkasharma','beingsalmankhan','parineetichopra']
count = 0
while (count < 30):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=4, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['shahidkapoor','sonamkapoor','sunnyleone','varundvn','iamsrk']
count = 0
while (count < 30):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['ranveersingh','hrithikroshan','dishapatani','katrinakaif','kritisanon','aslisona']
count = 0
while (count < 30):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

print("Sleeping for half an hour")
time.sleep(1800) 

accs = ['narendramodi','malhar028','jankibodiwala','thekinjaldave','aditiraval','dhvanitthaker','iamaarohii','kinjalrajpriya','rjdevaki','geetabenrabariofficial','arvind_vegda','mirchikunal','rjharshil','thecomedyfactoryindia','instafunny_manan','bhaktikubavat','jigneshkavirajbarot','rajalbarotofficial','bhoomitrivediofficial','dharmesh0011','hardikpatel.official','amitshahofficial','ameeshapatel9','actoryash','deekshajoshiofficial','whomayurchauhan']
count = 0
while (count < 30):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=26, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)
'''
# end the bot session
session.end()
