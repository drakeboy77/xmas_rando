import random

list = ["Jan", "Bob", "Luke", "Mindye", "Russ", "Sarah"]
forlist = ["Jan", "Bob", "Luke", "Mindye", "Russ", "Sarah"]
fromlist = list
#print (random.choice(list))

#for x in range(0, len(list)):
#    print x
#for x in list:
#    print x
#    print "test"
for x in list:
    #print "we're at %s point in for loop" % list.index(x)
    #print len(list)
    #print("X value is (): ()".format(x, forlist))
    for_value = random.choice(forlist)
    while for_value == x:
        #print for_value
        #print "for_value is the same as x"
        for_value = random.choice(forlist)
        if len(forlist) == 1:
            #print "breaking while loop for same x"
            if x == forlist[0]:
                print "this one is no bueno with someone getting presents for themselves!!!!"
                break
            else:
                break
    while for_value not in forlist:
        #print "stuck on the for_value %s being a part of original list %s" % (for_value, for_list)
        for_value = random.choice(forlist)
    pop_value = forlist.index(for_value)
    #print " pop value is %s" % pop_value
    #del forlist[pop_value]
    print "                        %s is getting presents for %s" % (x, for_value)
    forlist.remove(for_value)
    #print forlist
    #for_value = ""
