import pip._vendor.requests
# from bs4 import BeautifulSoup


url = "https://sitechris7.netlify.app/"

reponse = pip._vendor.requests.get(url)

page = str(reponse.content)
# page = page.replace("\t","")
# page = page.replace("\n","")
page_without_undesirable_characters = " ".join(word for word in page.split() if not word.startswith("\\"))

print(type(page_without_undesirable_characters))
# print(page_without_undesirable_characters)

file_copy_index3 = open("file_copy_index3.txt", "w")

file_copy_index3.write(page_without_undesirable_characters)

file_copy_index3.close

# partie fonctionnelle :

mon_string = "Salut \tChristophe, tout \nse passe pour le mieux"

# j'échappe les \n et les \t de mon_string
mon_string2 = " ".join(word for word in mon_string.split() if not word.startswith("\\"))

# mon_string2 = mon_string.replace("\t","")
# mon_string2 = mon_string.replace("\n","")


print("mon_string2")
print(mon_string2)

"""
for s in mon_string:
    # print(s, end="")
    # print(i,mon_string[i])
    if "\n" in mon_string or "\t" in mon_string  or "  " in mon_string  :
        mon_string2 = "".join(mon_string)
        # mon_string2 = mon_string.replace("\n","")
        # mon_string2 += mon_string[i]
    mon_string2 += s


print("mon_string")
print(mon_string)

print("mon_string2")
print(mon_string2)
"""
