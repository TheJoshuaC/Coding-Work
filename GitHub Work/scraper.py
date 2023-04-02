import requests
import lxml.html
import csv

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = []
for div in tags_divs: tags.append(div.text_content())
tags = [tag.split(', ') for tag in tags]
print(tags)

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []
for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]') 
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

output = []
for info in zip(titles,prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Tags', 'Platforms'])
    for game in output:
        writer.writerow([game['title'], game['price'], ', '.join(game['tags']), ', '.join(game['platforms'])])

print(output)