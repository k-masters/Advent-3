import re

with open("Files/test_input_day3-1.txt") as data:
    cloth_start_x = 0
    cloth_start_y = 0
    cloth_size_x = 0
    cloth_size_y = 0
    cloth_list = []
    used_inch_coords = []

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
        #print(cloth)
        # get x,y pairs of each used inch starting with the given coords
        temp_list =[]

        #todo: this takes care of the first group of x coords now need to start over for the second group of y
        for i in range(int(cloth.get("cloth_start_x")), int(cloth.get("cloth_start_x")) +
                                                            int(cloth.get("cloth_size_x"))):

            temp_list.append("{}, {}".format(str(i), cloth.get("cloth_start_y")))

        print(temp_list)