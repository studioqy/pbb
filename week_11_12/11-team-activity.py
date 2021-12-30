with open("hr_system.txt") as employees:

    for line in employees:
        word = line.split(" ")
        word_num = 1
        for aword in word:
            singword = aword.strip()
            if word_num == 1:
                emp_name = singword
                word_num += 1
            elif word_num == 2 :
                emp_id = singword
                word_num += 1
            elif word_num == 3:
                emp_title = singword
                word_num += 1
            elif word_num ==4:
                emp_salary = int(singword)
                monthly_sal = emp_salary/24
                if emp_title == "Engineer":
                    monthly_sal += 1000
                word_num += 1
            else:
                pass
        print(f"{emp_name} ID:({emp_id}), {emp_title} - ${monthly_sal:.2f}")