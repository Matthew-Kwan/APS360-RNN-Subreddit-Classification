import praw

reddit = praw.Reddit(client_id='O2CGE0BaM0D2Cg',
                    client_secret='Px4x2nz-tLGCzAy_ieNr4sVcEnQ',
                    user_agent='O2CGE0BaM0D2Cg')

for submission in reddit.subreddit('surrealmemes').top(limit=10):
    print(submission.title)


