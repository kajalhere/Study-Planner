import datetime

# Collect Inputs
num_subjects = int(input("How many subjects do you have? "))
subjects = {}

for _ in range(num_subjects):
    name = input("Enter subject name: ")
    exam_date_str = input(f"Enter exam date for {name} (YYYY-MM-DD): ")
    exam_date = datetime.datetime.strptime(exam_date_str, "%Y-%m-%d").date()
    subjects[name] = exam_date

print("Subjects and exam dates collected:", subjects)  # Debug print

# Ask available study hours per Day
study_hours_per_day = int(input("How many hours can you study each day? "))
today = datetime.date.today()
print("Today's date:", today)  # Debug print

# Calculate days left & priority score
subject_plan = {}
for sub, date in subjects.items():
    days_left = (date - today).days
    print(f"{sub}: {days_left} days left until exam.")  # Debug print
    if days_left <= 0:
        print(f"Exam for {sub} has already passed or is today.")
        continue
    subject_plan[sub] = {"days_left": days_left}

print("Subject plan after filtering past exams:", subject_plan)  # Debug print

# Calculate total weight for proportional time distribution
if subject_plan:
    total_inverse_days = sum(1 / info["days_left"] for info in subject_plan.values())
else:
    total_inverse_days = 0

# Distribute time proportionally
for sub in subject_plan:
    weight = (1 / subject_plan[sub]["days_left"]) / total_inverse_days
    time_allocated = round(weight * study_hours_per_day, 2)
    subject_plan[sub]["time_today"] = time_allocated
    print(f"Allocated {time_allocated} hours to {sub} today.")  # Debug print

# Save plan to a file
with open("study_plan.txt", "w") as file:
    file.write(f"Study plan for {today}:\n\n")
    for sub, info in subject_plan.items():
        file.write(f"{sub}: {info['time_today']} hours (Exam in {info['days_left']} days)\n")

print("\nYour study plan for today has been saved to 'study_plan.txt'")