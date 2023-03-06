casino_blacklist = ['Elysia Charles', 'Frances May','Mahnoor Chambers','Clyde Cannon','Franciszek Cardenas','Charlie Logan','Rufus Austin','Nannie Vega',]
poker_blacklist = ['Pearl Thompson', 'Rufus Austin','Naima Garner','Frances May','Franciszek Cardenas','Helena Todd','Mahnoor Chambers','Clyde Cannon',]
alcohol_blacklist = ['Rufus Austin', 'Frances May','Mahnoor Chambers','Frances May','Elysia Charles','Franciszek Cardenas','Elijah Willis','Clyde Cannon',]
common_list = set(casino_blacklist).intersection(poker_blacklist, alcohol_blacklist)
print(common_list)