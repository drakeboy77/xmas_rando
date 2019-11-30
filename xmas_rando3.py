import random

name_list = []
while bool:
    name_list.append(input("What is the name of one of the gifters?"))
    bool = input("Are there any other names, y/n?")
    if bool == "y":
        bool = 1
    else:
        bool = 0
#print name_list
forlist = name_list[:]
#print forlist
#name_list = ["Jan", "Bob", "Luke", "Mindye", "Russ", "Sarah"]
#forlist = ["Jan", "Bob", "Luke", "Mindye", "Russ", "Sarah"]
#fromlist = list
#print (random.choice(list))

#for x in range(0, len(list)):
#    print x
#for x in list:
#    print x
#    print "test"
#for x in list:
for x in name_list:  
    #  This iterates over our main list of names and is essentially the "from" list
    #print "we're at %s point in for loop" % list.index(x)
    #print len(list)
    #print("X value is (): ()".format(x, forlist))
    for_value = random.choice(forlist)    #the "for" list is essentially the list of people who are getting presents
    while for_value == x:
        # we can't have people getting their own gifts?!?!
        #print for_value
        #print "for_value is the same as x"
        for_value = random.choice(forlist)  # so we choose again
        if len(forlist) == 1:
            # this is a function to test if we're at the very last person to choose a for 
            # and to see if from and for person are the same, if so, this is a bad list and must be redone
            # need to come up with a better way to deal with this problem
            #print "breaking while loop for same x"
            if x == forlist[0]:
                print("this one is no bueno with someone getting presents for themselves!!!!")
                break
            else:
                break
    while for_value not in forlist:
        #print "stuck on the for_value %s being a part of original list %s" % (for_value, for_list)
        for_value = random.choice(forlist)
        # not sure in the end if this function is needed, can't remember why I added it
    pop_value = forlist.index(for_value)
    # once we've selected a good pair, we need to purge the for person's name from the for_list as they have been taken care of
    # this tells us where in the forlist that the for person is so we can remove it later in the code
    #print " pop value is %s" % pop_value
    #del forlist[pop_value]
    print("                        "+x+" is getting presents for "+for_value)
    forlist.remove(for_value)  # this is where we remove the for person from the forlist
    #print forlist
    #for_value = ""
