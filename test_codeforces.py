
from adapters.codeforces import analyze_user

if __name__ == "__main__":
    handle = input("Enter Codeforces handle: ").strip()
    result = analyze_user(handle)
    for k, v in result.items():
        print(f"{k}: {v}")
