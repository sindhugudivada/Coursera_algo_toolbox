import sys

def merge_and_count_inversions(a,b):
    count_of_inversions = 0
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            count_of_inversions = count_of_inversions + len(a) - i
            c.append(b[j])
            j = j + 1
        elif a[i] < b[j]:
            c.append(a[i])
            i = i + 1
    c = c + a[i:] + b[j:]
    return count_of_inversions,c


#print(merge_and_count_inversions([45,90,95,100],[9,46,120]))

def sort_and_count_inversions(data):
    if len(data) <= 1:
        return 0, data
    mid = len(data)/2
    first_count, first_leg = sort_and_count_inversions(data[0:mid])
    second_count, second_leg = sort_and_count_inversions(data[mid:])
    inversions, total_sorted = merge_and_count_inversions(first_leg, second_leg)
    return first_count + second_count + inversions, total_sorted

print(sort_and_count_inversions([45,90,95,9,46,120])[0])
