from typing import List, Dict

def create_profile(user_id: int, name: str, skills: List[str]) -> Dict[str, str]:

    formatted_name = name.strip().title()

    profile = {
        "ID": str(user_id),
        "Name": formatted_name,
        "Top Skills": skills[0] if skills else "No Skills"
    }

    return profile

my_profile = create_profile(101, "rAhUl", ["python", "AI", "Git"])
print("Generated Profile:", my_profile)