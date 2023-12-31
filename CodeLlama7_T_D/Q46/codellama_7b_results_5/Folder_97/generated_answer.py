
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 944, 814 and 865
    index_944 = my_list[944]
    index_814 = my_list[814]
    index_865 = my_list[865]
    gcf = 1

    for i in range(2, min(index_944, index_814, index_865) + 1)):
        if index_944 % i == 0 and index_814 % i == 0 and index_865 % i == 0:
            gcf = i

    return gcf
