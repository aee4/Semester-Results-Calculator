from model import calculate_grade_point
from model import calculate_grade
from model import calculate_weighted_gpa
from model import semester_class

program = input("Are there more students? Type yes to see results page")
while program.lower() == "yes":

  student_id = input("Enter your Student ID: ")
  marks_programming = float(input("Enter your marks for Programming: "))
  marks_hardware = float(input("Enter your marks for Hardware: "))
  marks_aca_writing = float(input("Enter your marks for Academic Writing: "))
  marks_french = float(input("Enter your marks for French: "))

  credit_hours = 3

  grade_programming = calculate_grade(marks_programming)
  grade_hardware = calculate_grade(marks_hardware)
  grade_aca_writing = calculate_grade(marks_aca_writing)
  grade_french = calculate_grade(marks_french)

  gp_programming = calculate_grade_point(marks_programming)
  gp_hardware = calculate_grade_point(marks_hardware)
  gp_aca_writing = calculate_grade_point(marks_aca_writing)
  gp_french = calculate_grade_point(marks_aca_writing)

  wgp_programming = calculate_weighted_gpa(marks_programming)
  wgp_hardware = calculate_weighted_gpa(marks_hardware)
  wgp_aca_writing = calculate_weighted_gpa(marks_aca_writing)
  wgp_french = calculate_weighted_gpa(marks_french)

  total_credit_hours = credit_hours * 4
  total_wgp = (wgp_programming + wgp_hardware + wgp_aca_writing + wgp_french)
  sgpa = total_wgp / total_credit_hours
  sem_class =semester_class(sgpa) 

  print(f"""
FIRST SEMESTER RESULTS *************************
Student ID: {student_id}

{"Course Title":<20} {"Marks":>6} {"Grade":>6} {"CHrs":>4} {"GP":>3} {"WGP":>4}
{"*"*60}

{"Programming":<20} {marks_programming:>6} {grade_programming:>6} {credit_hours:>4} {gp_programming:>3} {wgp_programming:>4}
{"Hardware":<20} {marks_hardware:>6} {grade_hardware:>6} {credit_hours:>4} {gp_hardware:>3} {wgp_hardware:>4}
{"Academic Writing":<20} {marks_aca_writing:>6} {grade_aca_writing:>6} {credit_hours:>4} {gp_aca_writing:>3} {wgp_aca_writing:>4}
{"French":<20} {marks_french:>6} {grade_french:>6} {credit_hours:>4} {gp_french:>3} {wgp_french:>4}

{"*"*60}
                            ΣChrs= {total_credit_hours} ΣWGP = {total_wgp}

SGPA :    {sgpa}
Semester Class: {sem_class}

----------------------------------------END OF RESULTS --------------------------------------------
""")

