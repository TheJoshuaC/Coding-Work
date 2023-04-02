# import pyperclip, re

# def find_australian_numbers(text):
#     # The regex pattern below matches Australian mobile numbers in the following formats:
#     # 0412 345 678, 0412-345-678, 0412.345.678, 0412345678, +61 412 345 678
#     pattern = re.compile(r'''
#     (?:\(\d\d\)\s\d{4}\s\d{4}| # (02) 1234 5678
#     \d{2}\s\d{4}\s\d{4}| # 02 1234 5678
#     \+\d{2}\s\d\s\d{4}\s\d{4}| # +61 2 1234 5678
#     \+\d{2}\s\d{4}\s\d{4}| # +61 1234 5678
#     \+\d{2}\s\d{4}\s\d{3}\s\d{3}| # +61 433 557 130
#     \+\d{2}\s0\d{3}\s\d{3}\s\d{3}| # +61 0433 557 130
#     \d{8}| # 12345678
#     \d{4}\s\d{4}| # 1234 5678
#     \d{4}-\d{4}| # 1234-5678
#     \d{4}\.\d{4}| # 1234.5678
#     \d{2}.?\d{4}.?\d{4}| # 02-1234-5678, 02.1234.5678
#     (?:0|\+61\s?)?\d{3}?[\s.-]?\d{3}?[\s.-]?\d{3}?) # 0412 345 678, 0412-345-678, 0412.345.678, 0412345678, +61 412 345 678
#      ''', re.VERBOSE)
    
#     # aus_nums = re.compile(r'''
#     # (?:(?:0|\+61\s?)?\d{3}?[\s.-]?\d{3}?[\s.-]?\d{3}?|\d) # 0412 345 678, 0412-345-678, 0412.345.678, 0412345678, +61 412 345 678
#     # ''', re.VERBOSE)
    

#     # Find all matches in the given text
#     matched_numbers = re.findall(pattern, text)
#     for number in matched_numbers:
#         print(number)

#     return matched_numbers




# text = """
# Once upon a time in the sunburnt land of Australia, people communicated using a variety of phone numbers, 
# including both landlines and mobile phones. The phone number formats were as diverse as the landscape itself, 
# reflecting the vast expanse of the country and the unique regions that made it so special.

# In the bustling city of Sydney, a young accountant named Sarah had a landline phone number with the format (02) 1234 5678. 
# The area code "02" represented New South Wales and the Australian Capital Territory. Sarah often chatted with her cousin, 
# Jack, who lived in Melbourne. Jack's landline phone number followed the format (03) 9876 5432, 
# with the "03" area code representing Victoria and Tasmania.

# Meanwhile, in the beautiful coastal city of Brisbane, a retired couple, George and Mary, enjoyed their golden years. 
# Their landline phone number had the format (07) 3456 7890, representing the Queensland area code "07." 
# They frequently called their friends in Adelaide, where the landline phone number format was (08) 4567 8901, 
# and the "08" area code covered South Australia and Western Australia.

# In the remote Northern Territory, a wildlife researcher named Alice had a satellite phone with the number 0417 123 456. 
# She often communicated with her colleagues in different parts of Australia, using their landline and 
# mobile numbers to share her findings.

# Now, let's not forget the ever-popular mobile phone numbers that connected Australians from coast to coast. 
# The mobile phone numbers typically began with "04," followed by eight additional digits. 
# For example, Sarah's mobile phone number was +61 412 345 678, while Jack's mobile phone number was +61 0487 654 321. 
# Mobile phones were essential tools for staying in touch with friends, family, and business associates.

# In Australia, there were also various other phone number formats, such as:

# Freecall numbers: 1800 123 456
# Local rate numbers: 13 12 34
# Premium rate numbers: 1900 123 456

# Regardless of the format or location, 
# Australian phone numbers served as a crucial means of communication across the vast continent. 
# Each number represented a person, a story, and a connection, 
# reminding us of the power of technology in bringing people together, no matter the distance.
# """

# phone_numbers = find_australian_numbers(text)
# print(phone_numbers)

"-----------------------------------------------------------"
# Test Example : Here are some Australian mobile numbers: 0412 345 678, 0412-345-678, 0412.345.678, 0412345678, +61 412 345 678, 0433 557 130, 0433-557-130, 0433.557.130, 0433557130, +61 433 557 130, 0450 233 897"
"-----------------------------------------------------------"

    # [a-zA-Z0-9._%+'-]+[\w._%+'-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

import re

def find_emails(text):
    pattern = re.compile(r'''
    [\w.%+'-]+[\w._%+'-]*@[\w.-]+\.[a-zA-Z]{2,} # email address
     ''', re.VERBOSE)
    
    # Find all matches in the given text
    matched_emails = re.findall(pattern, emailtextexample)
    for email in matched_emails:
        print(email)

    return matched_emails


emailtextexample = """

Once upon a time in the technologically advanced world of email communication, 
there were countless ways to format email addresses, each with its own unique flavor. 
People from all walks of life created email addresses that reflected their personalities, hobbies, and professions.

For instance, there was John, a passionate soccer fan. His email address was john_soccerfan@football.com. 
He had a friend named Alice, a talented artist. Her email address was alice.art@creative-works.net. 
They frequently exchanged emails about their shared interests and even collaborated on projects together.

In the bustling city, a young entrepreneur named Mark decided to open a bakery. 
He chose the email address mark@bakedgoods.co to represent his business. 
He also created a secondary email address for his catering service, mark_catering@bakedgoods.co. 
Mark often corresponded with his suppliers, such as the local farmer Jane, who used the email address jane-farm@farmland.org.

On the other side of the world, a scientist named Dr. Li Xiaoping studied the effects of climate change on the environment. 
Her professional email address was xiaoping.li@climate-research.edu. 
In her spare time, she loved hiking and exploring the great outdoors. 
She used a personal email address, li-hiker@naturelover.io, to share her adventures with friends and family.

In a small, tight-knit community, the local librarian, Mrs. Patel, had a unique email address that 
incorporated her favorite book character. Her email address was mrs_patel_hobbit@bookloverslibrary.info. 
She often exchanged book recommendations and reviews with a fellow librarian in a neighboring town, 
whose email address was daniel_thebookworm@literaryoasis.org.

And who could forget the famous rock band, The Electric Zebras? Each band member had an email address 
featuring their stage name. The lead singer's email was zebraqueen@electriczebras.biz, while the guitarist 
used axeman_zebra@electriczebras.biz. They kept in touch with their manager through the email address, 
manager@electriczebras.biz.

As the world continued to evolve, so did the complexity and creativity of email addresses. 
People experimented with different characters and formatting options, such as:

Numeric combinations: robert1978@techpros.com
Punctuation: jenny_o'brien@emailnetwork.ie
Underscores and dashes: evan-j_smith@venturecapital.io
Multiple domain levels: olivia@sales.region1.companyx.co.uk
Domain extensions: melissa@melissaphotography.photography
International characters: åsa.löfgren@swedishmail.se

Despite the many variations and formats, one thing remained constant: 
email addresses served as a unique identifier and a means of communication for 
individuals all around the globe. The possibilities for email address formatting were seemingly endless, 
yet each address represented a person, a story, and a connection.
"""

emails = find_emails(emailtextexample)
print(emails)


# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.

"""
#TESTER
Once upon a time in the technologically advanced world of email communication, 
there were countless ways to format email addresses, each with its own unique flavour.

john_soccerfan@football.com
alice.art@creative-works.net
mark@bakedgoods.co
mark_catering@bakedgoods.co
xiaoping.li@climate-research.edu
xiaoping.li@climate-research.edu.au
li-hiker@naturelover.io
mrs_patel_hobbit@bookloverslibrary.info
daniel_thebookworm@literaryoasis.org
zebraqueen@electriczebras.biz
axeman_zebra@electriczebras.biz
manager@electriczebras.biz
robert1978@techpros.com
jenny_o'brien@emailnetwork.ie
evan-j_smith@venturecapital.io
olivia@sales.region1.companyx.co.uk
melissa@melissaphotography.photography
åsa.löfgren@swedishmail.se
"""