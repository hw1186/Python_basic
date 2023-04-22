for i in range(1, 51):
    with open(str(i) + "주차.txt", "w") as report_file:
        report_file.write(i, "주차 보고")
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")