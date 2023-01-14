maxy={'owner':'pius','kind':'dog'}
trixie={'owner':'aubrey','kind':'dog'}
erica={'owner':'brigid','kind':'cat'}
jimmy={'owner':'jessy','kind':'monkey'}
pets=[maxy,trixie,erica,jimmy]
for pet in pets:
    for info,detail in pet.items():
        print(info.title())
        print(detail.title())
