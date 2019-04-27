from instapy import InstaPy

insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()
session.set_relationship_bounds(enabled=True,
				 potency_ratio=0.80,
				  delimit_by_numbers=False)
accs = ['mohanshakti','raghavjuyal','remodsouza','punitjpathakofficial','jhavartika','muktimohan']

count = 0
while (count < 15):     
    count = count + 1
    session.follow_by_list(accs,times=5000, sleep_delay=15, interact=False)
    session.unfollow_users(amount=6, customList=(True, accs, "all"), style="FIFO", unfollow_after=18, sleep_delay=10)

#session.follow_by_tags(['technology', 'smartphone'], amount=10)
# do the actual liking

# end the bot session
session.end()
