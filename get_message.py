from get_stats import get_counts

counts = get_counts()

world_inf, world_dead, world_rec = counts['world']
ind_inf, ind_dead, ind_rec = counts['india']

short_message = f"WORLD COUNT\n-----------\nTotal = {world_inf}\nDeaths = {world_dead}\nRecovered = {world_rec}\n\n\nINDIA COUNT\n-----------\nTotal = {ind_inf}\nDeaths = {ind_dead}\nRecovered = {ind_rec}"

