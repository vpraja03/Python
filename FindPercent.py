class FindPercent:
    def percentage():
        marks = []
        for i in range(1, 6):
            mark = int(input(f"Subject{i}= "))
            marks.append(mark)
        total = sum(marks)
        percentage = (total / 500) * 100
        print("Total : ", total)
        print("Percentage : ", percentage)