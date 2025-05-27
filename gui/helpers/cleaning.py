
def format_days(day_bools): #Takes a list of seven bools
    #basically if all the days are there say every day, otherwise convert to M-F / M-W, F-Sa / Tu - Su / etc
    day_abbr = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    selected_indices = [i for i, selected in enumerate(day_bools) if selected]

    if len(selected_indices) == 7:
        return "Every Day"
    if not selected_indices:
        return "None"
    
    ranges = []
    start = prev = selected_indices[0]

    for i in selected_indices[1:]: 
        if i == prev + 1:
            prev = i
        else:
            ranges.append((start, prev))
            start = prev = i
    ranges.append((start, prev))
    ##
    #if selected_indices[-1] != 6:
    #    ranges.append((start, prev))

    #TODO: Make this work when change happens over the bookends
    parts = []
    for start, end in ranges:
        if start == end:
            parts.append(day_abbr[start])
        else:
            parts.append(f'{day_abbr[start]}-{day_abbr[end]}')
        
    return ", ".join(parts)

