# coding: utf-8
from instapy import InstaPy
insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()


session.set_relationship_bounds(enabled=True,
                                 potency_ratio=None,
                                  delimit_by_numbers=False,
                                     max_followers=1000,
				    max_following=1000000,
				     min_followers=10,
				      min_following=200)




session.set_delimit_liking(enabled=True, max=1000, min=0)
session.like_by_tags(['indiangirl','indiangirls','desigirl','desigirls','gujjugirl','delhigirls','mumbaigirls'], amount=500)
                                
# end the bot session
session.end()
