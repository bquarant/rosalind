def oddlines(filename):
    inp = open(filename, 'r')
    
    #parse input data into a string
    s = inp.readlines()

    #create array for even line selection loop
    halflines = []

    #select only even lines
    for line in range(len(s)):
        if line % 2 != 0:
            halflines.append(s[line])

    #create output string
    output = ""

    #loop to add each item in array to output string
    for item in halflines:
        output += item

    #test print output
    print output

    #create, write and close output file
    out = open('output.txt', 'w')
    out.write(output)
    out.close()

oddlines("rosalind_ini5.txt")
