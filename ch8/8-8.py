# 8-8. User Albums
def make_album(artist, title, nums = None):
    if nums:
        album = {'artist':artist.title(), 'title':title.title(), 'nums':nums}
    else:
        album = {'artist':artist.title(), 'title':title.title()}
    return album

while True:
    print("You can quit anytime by entering 'q'")
    artist = input("Please enter the artist of this album: ")
    if artist == 'q':
        beark
    title = input("Please enter the title of this album: ")
    if title == 'q':
        break
    num = input("Please enter the number of songs in this album: ")
    make_album(artist, title, nums)