from instapy import InstaPy
import time
insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()
session.set_relationship_bounds(enabled=True,
				 potency_ratio=0.80,
				  delimit_by_numbers=False)

accs = ['narendramodi','malhar028','jankibodiwala','thekinjaldave','aditiraval','dhvanitthaker']
count = 0
while (count < 10):     
    count = count + 1
    session.follow_by_list(accs,times=1000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

time.sleep(600)

accs = ['iamaarohii','kinjalrajpriya','rjdevaki','geetabenrabariofficial','arvind_vegda','mirchikunal']
count = 0
while (count < 10):     
    count = count + 1
    session.follow_by_list(accs,times=1000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

time.sleep(600)

accs = ['rjharshil','thecomedyfactoryindia','instafunny_manan','bhaktikubavat','jigneshkavirajbarot','rajalbarotofficial']
count = 0
while (count < 10):     
    count = count + 1
    session.follow_by_list(accs,times=1000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

time.sleep(600)

accs = ['bhoomitrivediofficial','dharmesh0011','hardikpatel.official']
count = 0
while (count < 10):     
    count = count + 1
    session.follow_by_list(accs,times=1000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=3, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)

time.sleep(600)

accs = ['amitshahofficial','ameeshapatel9','actoryash','deekshajoshiofficial','whomayurchauhan']
count = 0
while (count < 10):     
    count = count + 1
    session.follow_by_list(accs,times=1000, sleep_delay=10, interact=False)
    session.unfollow_users(amount=5, customList=(True, accs, "all"), style="FIFO", unfollow_after=10, sleep_delay=10)


#session.follow_by_tags(['technology', 'smartphone'], amount=10)
# do the actual liking

# end the bot session
session.end()
