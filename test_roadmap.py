from adapters.codeforces import analyze_user
from roadmap.generator import generate_roadmap

if __name__ == "__main__":
    handle = input("Enter Codeforces handle: ").strip()
    goal = input("Choose goal (high_school / job_interview / zco_inoi_ioi / acm_icpc): ").strip()

    user_data = analyze_user(handle)
    roadmap = generate_roadmap(user_data, goal)

    print("\n🧭 Personalized Roadmap:\n")
    for line in roadmap:
        print(line)
