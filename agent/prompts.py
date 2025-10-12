def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT = f""" 
        you are the planner agent. Convert the user prompt into a complete engineering project plan
        User request: {user_prompt}
        """
    return PLANNER_PROMPT


