def bubble_sort(seq):
    while True:
        change = False
        for i, current in enumerate(seq):
            # ignore neighbor if it's the last element
            try:
                neighbor = seq[i + 1]
            except IndexError:
                continue

            if current > neighbor:
                # swap current step with neighbor step if current is a bigger value
                seq[i], seq[i + 1] = neighbor, current
                change = True

        # when there is no change in the forloop, all items have been sorted
        if not change:
            break

    return seq