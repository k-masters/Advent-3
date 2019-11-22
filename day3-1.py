import re
import timeit
import pprint as pp

start = timeit.default_timer()

with open("Files/input.txt") as data:
    cloth_list = []
    used_inch_coords = []
    dup_inch_coords = []

    for line in data:

        #Regex search: Look for 5 groups '()' of digits '\d+' with anything in between '.*?'
        match_on = re.search(r"(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)", line)
        temp_dict = {
            "index" : match_on.group(1),
            "cloth_start_x" : match_on.group(2),
            "cloth_start_y" : match_on.group(3),
            "cloth_size_x" : match_on.group(4),
            "cloth_size_y" : match_on.group(5)
        }
        cloth_list.append(temp_dict)

    for cloth in cloth_list:

        overlap_found = False

        print(cloth.get("index"))

        temp_list =[]

        for i in range(int(cloth.get("cloth_start_x")), int(cloth.get("cloth_start_x")) +
                                                            int(cloth.get("cloth_size_x"))):

            temp_list.append("{}, {}".format(str(i), cloth.get("cloth_start_y")))
            #print(temp_list)

            for z in range(int(cloth.get("cloth_start_y")) + 1, int(cloth.get("cloth_start_y")) +
                                                                int(cloth.get("cloth_size_y"))):

                temp_list.append("{}, {}".format(i, z))
                #print(temp_list)

        # print(temp_list)
        for coord in temp_list:
            if coord in used_inch_coords and coord not in dup_inch_coords: # basically is the coord a new dupe
                dup_inch_coords.append(coord)
            else:
                used_inch_coords.append(coord)

print("Duplicate inch coordinates!: ", len(dup_inch_coords))
print("Ok inch coordinates!: ", len(used_inch_coords))

stop = timeit.default_timer()
print("Time: {}".format(start - stop))