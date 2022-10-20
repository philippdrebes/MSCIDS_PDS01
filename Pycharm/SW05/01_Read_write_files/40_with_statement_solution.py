# solution: How can you divide the output in lorem_ipsum_2.txt
# into different lines

with open("lorem_ipsum.txt") as fobj_in:
    with open("lorem_ipsum_2.txt", "w") as fobj_out:
        counter = 0
        for line in fobj_in:
            counter += 1
            out = "{0:>3s} {1:s}\n".format(str(counter), line.rstrip())
            fobj_out.write(out)

with open("lorem_ipsum_2.txt") as fobj:
    for line in fobj:
        print(line.rstrip())
    fobj.close()
