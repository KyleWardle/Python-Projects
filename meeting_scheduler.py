time_available_in_hours = 12


class Meeting:
    def __init__(self, name: str, hours: float):
        self.name = name
        self.hours = hours

    def __str__(self):
        return "[" + self.name + " ," + str(self.hours) + "]"


def sort_meetings_arr(meetings: list):
    for x in range(0, len(meetings)):
        for i in range(0, len(meetings) - 1):
            if meetings[i].hours > meetings[i + 1].hours:
                temp = meetings[i]
                meetings[i] = meetings[i + 1]
                meetings[i + 1] = temp
    return meetings


def filter_meetings_arr(meetings: list, amount_left: float):
    meetings_copy = []
    for i in range(0, len(meetings)):
        if meetings[i].hours <= amount_left:
            meetings_copy.append(meetings[i])
    return meetings_copy

meetings_arr = [
    Meeting("First", 2.0),
    Meeting('Second', 5.0),
    Meeting('Third', 1.5),
    Meeting('Fourth', 0.5),
    Meeting('Fifth', 4.0),
    Meeting('Sixth', 14.0),
    Meeting('Seventh', 9.0),
]

sorted_meetings = sort_meetings_arr(meetings_arr)

total = 0
arranged_meetings = []

while (total < time_available_in_hours) and (len(sorted_meetings) > 0):
    total_left = time_available_in_hours - total
    sorted_meetings = filter_meetings_arr(sorted_meetings, total_left)
    meeting_index = round((len(sorted_meetings) - 1) / 2)
    meeting_to_add = sorted_meetings[meeting_index]
    sorted_meetings.pop(meeting_index)
    total = total + meeting_to_add.hours
    arranged_meetings.append(meeting_to_add)
print(total)

#
# for i in range(0, len(filtered_meetings)):
#     print(filtered_meetings[i])
