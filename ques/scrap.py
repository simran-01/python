# insta
# from facebook_scraper import get_posts
# import instaloader
# import pandas as pd
# from prettytable import PrettyTable
# x = PrettyTable()
# bot = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(bot.context, 'amazon')
# x.field_names = ["Attribute", "Details"]
# x.add_rows(
#     [
#         ["Username: ", profile.username],
#         ["User ID: ", profile.userid],
#         ["Number of Posts: ", profile.mediacount],
#         ["Followers Count: ", profile.followers],
#         ["Following Count: ", profile.followees],
#         ["Bio: ", profile.biography],
#         ["External URL: ", profile.external_url],
#     ]
# )
# print(x)

# # twitter
# import json
# from twitter_scraper_selenium import get_profile_details
# twitter_username = "Amazon"
# filename = "twitter_api_data"
# get_profile_details(twitter_username=twitter_username, filename=filename)
# with open('twitter_api_data.json', 'r') as json_file:
#     json_object = json.load(json_file)
# print(json.dumps(json_object, indent=1))

# facebook

from facebook_scraper import get_posts
import pandas as pd
fbPosts = []
for post in get_posts('statebankofindia', pages=12):
    fbPosts.append({x: post[x] for x in ['post_id', 'text', 'likes']})
print(print(f"Latest posts:\n {pd.DataFrame(fbPosts)}"))
