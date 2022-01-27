# 8-7. Album
def make_album(artist, title, nums = None):
    if nums:
        album = {'artist':artist.title(), 'title':title.title(), 'nums':nums}
    else:
        album = {'artist':artist.title(), 'title':title.title()}
    return album

print(make_album("Coldplay", "american idot"))
print(make_album("lana del rey", "born to die", 9))
print(make_album("Linkin Park", "Numb"))