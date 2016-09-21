import hashlib
import os

output = ''

# insert users: sportslover, traveler, spacejunkie
output += """insert into user values('sportslover', 'Paul', 'Walker', 'paulpass93', 'sportslover@hotmail.com');\n"""
output += """insert into user values('traveler', 'Rebecca', 'Travolta', 'rebeccapass15', 'rebt@explore.org');\n"""
output += """insert into user values('spacejunkie', 'Bob', 'Spacey', 'bob1pass', 'bspace@spacejunkies.net');\n"""

# insert albums
albumDict = {}
albumId = 1
albumDict['I love sports'] = albumId
output+= ('insert into album values(NULL'+ """, 'I love sports', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'sportslover');\n""")
albumId += 1
albumDict['I love football'] = albumId
output+= ('insert into album values(NULL' + """, 'I love football', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'sportslover');\n""")
albumId += 1
albumDict['Around The World'] = albumId
output+= ('insert into album values(NULL' + """, 'Around The World', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'traveler');\n""")
albumId += 1
albumDict['Cool Space Shots'] = albumId
output+= ('insert into album values(NULL' + """, 'Cool Space Shots', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'spacejunkie');\n""")
albumId += 1

# check files
seqNum = 0
htable = hashlib.md5()
directory = "./../static/images"
for file in os.listdir(directory):
    if file.startswith('.'):
        continue
        
    dotNum = file.find('.')
    fname = file[0:dotNum-1]
    fformat = file[dotNum+1:len(file)]
    if fname.startswith('sports'):
        album = 'I love sports'
    elif fname.startswith('football'):
        album = 'I love football'
    elif fname.startswith('world'):
        album = 'Around The World'
    elif fname.startswith('space'):
        album = 'Cool Space Shots'

    albumId = albumDict[album]
    htable.update(str(albumId))
    htable.update(fname)
    picid = htable.hexdigest()
    oName = os.path.join(directory, file)
    nName = os.path.join(directory, picid+'.'+fformat)
    os.rename(oName, nName)
        
    output += ("""insert into photo values('""" + fformat + """', '""" + str(picid) + """', CURRENT_TIMESTAMP);\n""")
    output += ('insert into contain values(' + str(seqNum) + ', ' + str(albumId) + """, '""" + str(picid) + """', '');\n""")

    seqNum += 1

oFile = open("load_data.sql", "w")
oFile.write(output)
oFile.close()
