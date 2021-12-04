#!/usr/bin/python3

from typing import List

def convert_str_to_list(measures : str) -> List[int]:
    depth_str_list = measures.split("\n")
    depth_list = [ int(depth) for depth in depth_str_list if depth != "" ]
    return depth_list

# Window increases when n+xth > nth
def get_increase_count(depth_list : List[int], window_size : int = 1) -> int:
    increase_count = 0
    for i in range(window_size, len(depth_list)):
        if depth_list[i] > depth_list[i-window_size]:
            increase_count += 1

    print(increase_count)
    return increase_count

with open("Day01.txt", "r") as f:
    measures = f.read()

depth_list = convert_str_to_list(measures)
get_increase_count(depth_list)
get_increase_count(depth_list, window_size=3)