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
        break
    title = input("Please enter the title of this album: ")
    if title == 'q':
        break
    nums = input("Please enter the number of songs in this album: ")
    album = make_album(artist, title, nums)
    print(f'Album made: {album}.')