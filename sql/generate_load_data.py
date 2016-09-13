import hashlib
import os

output = ''

# insert users: sportslover, traveler, spacejunkie
output += 'select * from user;\n'
output += """insert into user values('sportsloyer', 'Paul', 'Walker', 'paulpass93', 'sportslover@hotmail.com');\n"""
output += 'select * from user;\n'
output += """insert into user values('traveler', 'Rebecca', 'Travolta', 'rebeccapass15', 'rebt@explore.org');\n"""
output += 'select * from user;\n'
output += """insert into user values('spacejunkie', 'Bob', 'Spacey', bob1pass', 'bspace@spacejunkies.net');\n"""

# insert albums
albumId = 1
albumDict['I love sports'] = albumId
output+= 'select * from album;\n'
output+= ('insert into album values(' + str(albumId) + """, 'I love sports', , , 'sportslover');\n""")
albumId += 1
albumDict['I love football'] = albumId
output+= 'select * from album;\n'
output+= ('insert into album values(' + str(albumId) + """, 'I love football', , , 'sportslover');\n""")
albumId += 1
albumDict['Around The World'] = albumId
output+= 'select * from album;\n'
output+= ('insert into album values(' + str(albumId) + """, 'Around The World', , , 'traveler');\n""")
albumId += 1
albumDict['Cool Space Shots'] = albumId
output+= 'select * from album;\n'
output+= ('insert into album values(' + str(albumId) + """, 'Cool Space Shots', , , 'spacejunkie');\n""")
albumId += 1

# check files
seqNum = 0
htable = hashlib.md5()
for file in os.listdir("/vagrant/static/images/"):
    if file.startswith('.'):
        continue
        
    dotNum = file.find('.')
    fname = file[0:dot_num-1]
    fformat = file[dot_num+1:len(file)]
    if fname.startswith('sports'):
        album = 'I love sports'
    elif fname.startswith('football'):
        album = 'I love football'
    elif fname.startswith('world'):
        album = 'Around The World'
    elif fname.startswith('space'):
        album = 'Cool Space Shots'i

    albumId = albumDict[album]
    htable.update(str(albumId))
    htable.update(fname)
    picid = htable.hexidigest()
        
    output += 'select * from contain;\n'
    output += ('insert into contain values(' + str(seqNum) + ', ' + str(albumId) + """, '""" + str(picid) + """', '');\n""")

    output += 'select * from photo;\n'
    output += ("""insert into photo values('""" + fformat + """', '""" + str(picid) + """');\n""")

    seqNum += 1
