from engine import Engine

'''
About this problem: given an array of books with arr[i] representing the number of pages of that
book, allocate the books to the given number of students in such a manner that the max number of 
pages allocated to a student is the minimum possible.Every student must get one book
allocation of books must be contiguous.
each book can only be allocated to one student.
'''

test_cases = [
    ([[12, 34, 67, 90], 2], {'ret': 113}), 
    ([[25, 46, 28, 1, 24], 4], {'ret': 46}),
    ([[10, 20], 3], {'ret': -1}),
    ([[5, 10, 20, 30], 1], {'ret': 65}),
    ([[15, 10, 45, 22, 9], 5], {'ret': 45}),
    ([[20, 20, 20, 20, 20], 3], {'ret': 40}),
    ([[1, 1, 1, 100, 1, 1], 3], {'ret': 100}),
    ([[7, 13, 12, 4, 9, 8], 3], {'ret': 20})
]
run = Engine(test_cases)

#---Solution-----------------------------------------------------------------------------

'''
return -1 if len(pages) is smaller than number of students.

the range should be from max of pages so that we can allocate all the books, all the way to sum(pages)
low to max(pages), high to sum(pages)

run a while loop with condition low <= high
    calc the mid of low and high
    make std_done = 1
    make alc_pages = 0

    run a for loop and iterate over the pages array
        if alc_pages + pages[i] > mid: this means the student cannot hold more pages
            std_done += 1
            alc_pages = pages[i]
        else: we will simply add the pages to the students allocation
            alc_pages += pages[i]

        if std_done > std: notice how this is not equality but greater than.
            break
    else: if we didn't break out of the for loop, this mean, we either weren't able to allocate 
    all stds or we have a possible candidate, in both cases decrease the allocation
        this means, we are allocating a lot of pages to a single student, decrease it
        high = mid - 1
        continue
        
    if we broke out of the for loop becaue too many students were given books which is not good. 
    try increasing the pages allocated
    low = mid + 1

return low
            
'''

def solution(pages: list, std: int) -> int:
    if len(pages) < std:
        return -1
    
    low, high = max(pages), sum(pages)

    while low <= high:
        mid = (low + high) // 2
        std_done = 1
        alc_pages = 0

        for page in pages:
            if page + alc_pages > mid:
                std_done += 1
                alc_pages = page

            else:
                alc_pages += page

            if std_done > std:
                break

        else:
            high = mid - 1
            continue

        low = mid + 1

    return low
    
    
run.v8(solution)