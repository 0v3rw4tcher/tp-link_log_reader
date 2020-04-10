import sys

while True:

    try:

        log=open(input("log file path >>> "),"r").read().split("\n")

    except:

        print("we can not open the file")

    else:

        break

i=0

while i <= len(log):

    if i == len(log):

        break


    if "repeat" in log[i]:

        log.remove(log[i])

    i+=1
try:

    while True:

        found = []
        intime= []

        keys = input(">>> ").strip(" ").split(",")

        if keys == ["exit()"]:

            sys.exit(0)

        elif keys==["help()"]:

            print("""
exit() : to exit
help() : to help
special : for special searching

or you can just type values to search , an example for format:

1/1/2000 0:24:18>
""")

        elif keys==["special"]:

            time=input("time : ")

            day=input("day format : ")

            errorkind=input("what error ? ")

            for i in log:

                if i.split(" ")[0] == day:

                    if i.split(" ")[1] == time:

                        if i.split(" ")[2] == errorkind:

                            found.append(log)

                        else:

                            intime.append(log)

            if found == [] : found = ["not found"]

            if intime== [] : intime= ["not found"]

            print("=============found=============")

            for i in found :

                print(i)

            print("=============in that time============")

            for i in intime :

                print(i)
        else:
            for i in log:

                error=False

                for n in keys:

                    if n in i :

                        pass

                    else:

                        error=True

                if error == False:

                    found.append(i)

                else:

                    pass

            if found == []:

                found = ["could not find any"]

            for i in found:

                print (i)

except:

    sys.exit(0)