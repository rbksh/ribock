from typing import Dict, List

def generate_roadmap(user_data: Dict[str, any], goal: str) -> List[str]:
    rating = user_data.get("rating", 0) if isinstance(user_data.get("rating"), int) else 0
    solved = user_data.get("solvedCount", 0)
    accuracy = user_data.get("accuracyPercent", 0)
    tags = user_data.get("tagsCount", {})
    difficulty = user_data.get("difficultyCount", {})

    roadmap = []
    roadmap.append(f"🎯 Goal: {goal}")
    roadmap.append(f"📊 Your Current Stats: Rating {rating}, Accuracy {accuracy}%, Problems Solved {solved}")

    # Base analysis level
    level = "beginner"
    if rating >= 1800:
        level = "advanced"
    elif rating >= 1400:
        level = "intermediate"

    # Roadmap content
    if goal == "high_school":
        roadmap += _roadmap_high_school(level, tags)
    elif goal == "job_interview":
        roadmap += _roadmap_job_interview(level, tags)
    elif goal == "zco_inoi_ioi":
        roadmap += _roadmap_ioi(level, tags)
    elif goal == "acm_icpc":
        roadmap += _roadmap_icpc(level, tags)
    else:
        roadmap.append("Invalid goal provided.")

    return roadmap

def _roadmap_high_school(level: str, tags: Dict[str, int]) -> List[str]:
    plan = ["👶 Focus on basic topics like arrays, strings, and brute force"]
    if level != "beginner":
        plan.append("📚 Start solving implementation and greedy problems rated 800–1200")
    plan.append("🚀 Participate in school-level contests or junior olympiads")
    return plan

def _roadmap_job_interview(level: str, tags: Dict[str, int]) -> List[str]:
    plan = ["💼 Master key patterns: sliding window, two pointers, binary search"]
    plan.append("📘 Solve 150+ Leetcode-style problems across core categories")
    if "dp" not in tags:
        plan.append("🔁 Learn basics of Dynamic Programming")
    plan.append("🧠 Practice system design + behavioral interview questions if >1800")
    return plan

def _roadmap_ioi(level: str, tags: Dict[str, int]) -> List[str]:
    plan = ["🏆 Study CPH and USACO guide for olympiad-level problems"]
    plan.append("🎓 Practice with ZCO/INOI past papers")
    if "graphs" not in tags:
        plan.append("🕸️ Learn Graph Theory (BFS, DFS, Topo Sort, SCC)")
    if "dp" not in tags:
        plan.append("🎯 Master DP problems including knapsack, LIS, digit DP")
    return plan

def _roadmap_icpc(level: str, tags: Dict[str, int]) -> List[str]:
    plan = ["⚙️ Practice team contests (Div2/Div1 Codeforces rounds)"]
    if level == "beginner":
        plan.append("👨‍💻 Solve 100+ problems rated 800–1300 first")
    else:
        plan.append("🧪 Train for ICPC-style problemsets with virtual contests")
    plan.append("🔬 Topics: Segment Trees, DP on Trees, DSU, Centroid Decomp")
    return plan
