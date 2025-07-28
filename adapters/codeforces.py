# File: adapters/codeforces.py

import requests
from typing import Dict, List, Any, Optional

BASE_URL = "https://codeforces.com/api"

class CodeforcesAPIError(Exception):
    pass

def get_user_info(handle: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/user.info?handles={handle}"
    res = requests.get(url).json()
    if res['status'] != 'OK':
        raise CodeforcesAPIError(f"Error fetching user info: {res.get('comment', '')}")
    return res['result'][0]

def get_user_status(handle: str) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/user.status?handle={handle}&from=1&count=10000"
    res = requests.get(url).json()
    if res['status'] != 'OK':
        raise CodeforcesAPIError(f"Error fetching user status: {res.get('comment', '')}")
    return res['result']

def analyze_user(handle: str) -> Dict[str, Any]:
    info = get_user_info(handle)
    submissions = get_user_status(handle)

    total_subs = len(submissions)
    accepted_subs = [s for s in submissions if s.get('verdict') == 'OK']
    unique_accepted = {f"{s['problem']['contestId']}-{s['problem']['index']}" for s in accepted_subs}

    tags_count = {}
    difficulty_count = {}

    for s in accepted_subs:
        problem = s['problem']
        for tag in problem.get('tags', []):
            tags_count[tag] = tags_count.get(tag, 0) + 1
        if 'rating' in problem:
            r = problem['rating']
            difficulty_count[r] = difficulty_count.get(r, 0) + 1

    accuracy = (len(accepted_subs) / total_subs) * 100 if total_subs else 0

    return {
        'handle': handle,
        'rating': info.get('rating', 'Unrated'),
        'maxRating': info.get('maxRating', 'Unrated'),
        'rank': info.get('rank', 'N/A'),
        'maxRank': info.get('maxRank', 'N/A'),
        'totalSubmissions': total_subs,
        'solvedCount': len(unique_accepted),
        'accuracyPercent': round(accuracy, 2),
        'tagsCount': tags_count,
        'difficultyCount': difficulty_count
    }