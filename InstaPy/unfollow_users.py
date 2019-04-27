from instapy import InstaPy

insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()


session.unfollow_users(amount=500, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=5, sleep_delay=5)


# end the bot session
session.end()
