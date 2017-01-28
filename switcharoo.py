
input1 = raw_input("First input? ")
input2 = raw_input("Second input? ")

#take two lists, insert values of one into other by index and print after each insertion
def switcharoo(input1, input2):
    list_a = list(input1)
    list_b = list(input2)
    pos = 0
    maxind = len(list_b)
    print "".join(list_b)
    while pos != maxind:
        value = list_a[pos]
        list_b[pos] = value
        updated = "".join(list_b)
        print updated
        pos = pos + 1

switcharoo(input1, input2)
