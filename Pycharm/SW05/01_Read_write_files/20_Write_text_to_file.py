# Writing text in a file (and output this file afterwards!)
# Goal: In the text lorem_ipsum.txt, each line should be given a line number
# Explanations of the format (...) method follows later

# read from 'lorem_ipsum.txt', write in 'lorem_ipsum_2.txt,
# read content 'lorem_ipsum_2.txt', print out lorem_ipsum_2.txt

fobj_in = open("lorem_ipsum.txt")
fobj_out = open("lorem_ipsum_2.txt", "w")
counter = 0
for line in fobj_in:
    counter += 1
    out_line = "{0:>5s} {1:s}\n".format(str(counter), line.rstrip())
    # {0:>5s} 0   => first argument
    #         >5s => right aligned 5 strings
    # {1:s}   1   => second argument
    #         s   => string (standard left aligned!)
    # 'rstrip()'? => removes white spaces and newlines
    # from the right margin

    # out_line = "%5d %s" % (counter, line)    # c-style

    fobj_out.write(out_line)


fobj_in.close()        # every open file should be closed
fobj_out.close()       # every open file should be closed

fobj = open("lorem_ipsum_2.txt")
for line in fobj:
    print(line.rstrip())  # try out also without .rstrip() => result?
    # print(line)
    # print(line, end="")
fobj.close()
