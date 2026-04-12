scores = [88, 92, 79, 95, 60, 85]
scores.sort(reverse=True)

print("Top scores:")
for score in scores[:3]:
    if score >= 90:
        print(f"{score} - Excellent")
    else:
        print(f"{score} - Good")