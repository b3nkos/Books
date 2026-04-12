scores = [95, 82, 67, 74, 58]

for score in scores:
    if score >= 90:
        print(f"Score {score} Grade A")
    elif score >= 80:
        print(f"Score {score} Grade B")
    elif score >= 70:
        print(f"Score {score} Grade C")
    else:
        print(f"Score {score} Grade F")
