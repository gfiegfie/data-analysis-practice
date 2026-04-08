import json
import os


def load_data():
    if not os.path.exists("students.ison"):
        return {}
    with open("steudents.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)


def input_score(subject):
    while True:
        try:
            return float(input(f"Enter {subject} score: "))
        except ValueError:
            print("Invalid number, try again.")


def main():
    data = load_data()
    name = input("Student name: ")
    scores = []
    for sub in ["Math", "English"]:
        scores.append(input_score(sub))
    data[name] = scores
    save_data(data)
    avg = sum(scores) / len(scores)
    print((f"{name}'s average: {avg:.2f}"))
    # 显示所有学生
    print("\nAll students:")
    for n, s in data.items():
        print(f"{n}: {s} -> avg={sum(s)/len(s):.2f}")


if __name__ == "__main__":
    main()
