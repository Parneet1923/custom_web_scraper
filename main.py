import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/stats'


response = requests.get(url)
nba_webpage = response.text
soup = BeautifulSoup(nba_webpage, 'html.parser')
all_data = soup.find_all("table", class_="LeaderBoardPlayerCard_lbpcTable__q3iZD")
points_anchor = all_data[0].find_all("a", class_="Anchor_anchor__cSc3P")
rebounds_anchor = all_data[1].find_all("a", class_="Anchor_anchor__cSc3P")
assists_anchor = all_data[2].find_all("a", class_="Anchor_anchor__cSc3P")
blocks_anchor = all_data[3].find_all("a", class_="Anchor_anchor__cSc3P")
steals_anchor = all_data[4].find_all("a", class_="Anchor_anchor__cSc3P")
turnovers_anchor = all_data[5].find_all("a", class_="Anchor_anchor__cSc3P")
three_pointers_anchor = all_data[6].find_all("a", class_="Anchor_anchor__cSc3P")
free_throws_anchor = all_data[7].find_all("a", class_="Anchor_anchor__cSc3P")
fantasy_points_anchor = all_data[8].find_all("a", class_="Anchor_anchor__cSc3P")
points_player = {}
rebounds_player = {}
assists_player = {}
blocks_player = {}
steals_player = {}
turnovers_player = {}
three_pointer_player = {}
free_throws_player = {}
fantasy_points_player = {}
for i in range(0, len(points_anchor) - 1, 2):
    points_player[points_anchor[i].getText()] = points_anchor[i + 1].getText()
    rebounds_player[rebounds_anchor[i].getText()] = rebounds_anchor[i + 1].getText()
    assists_player[assists_anchor[i].getText()] = assists_anchor[i + 1].getText()
    blocks_player[blocks_anchor[i].getText()] = blocks_anchor[i + 1].getText()
    steals_player[steals_anchor[i].getText()] = steals_anchor[i + 1].getText()
    turnovers_player[turnovers_anchor[i].getText()] = turnovers_anchor[i + 1].getText()
    three_pointer_player[three_pointers_anchor[i].getText()] = three_pointers_anchor[i + 1].getText()
    free_throws_player[free_throws_anchor[i].getText()] = free_throws_anchor[i + 1].getText()
    fantasy_points_player[fantasy_points_anchor[i].getText()] = fantasy_points_anchor[i + 1].getText()
print(points_player)
print(rebounds_player)
print(assists_player)
print(blocks_player)
print(steals_player)
print(turnovers_player)
print(three_pointer_player)
print(free_throws_player)
print(fantasy_points_player)
