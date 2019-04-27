# coding: utf-8
from instapy import InstaPy
insta_username = 'thenewsocean'
insta_password = 'popatbhaigrandi10'

session = InstaPy(username=insta_username, password=insta_password)
session.login()


session.set_relationship_bounds(enabled=False,
                                 potency_ratio=None,
                                  delimit_by_numbers=False,
                                    max_followers=1000,
				    max_following=10000,
				     min_followers=1,
				      min_following=1)

session.set_do_comment(True, percentage=100)
session.set_comments(['VISIT OUR PAGE OR REGRET '])
session.comment_by_locations(['234281926/ahmedabad-india/','913811836/ahmedabad-city/','939600974/ahmedabad-gujarat-india/'], amount=10, skip_top_posts=False)



# end the bot session
session.end()
