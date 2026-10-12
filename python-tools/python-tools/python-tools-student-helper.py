# Humaira AI Toolkit - Student Helper
# By Humaira Mukhtar | BSSE 5th Sem | RYK
# Bano Qabil AI Essentials Project

def ai_helper(topic):
    print(f"--- Help for: {topic} ---")
    if topic.lower() == "ai":
        return "AI ka matlab hai Machine ko Insan jaisa sochna sikhana."
    elif topic.lower() == "github":
        return "GitHub ek website hai jahan programmers apna code save karte hain."
    elif topic.lower() == "python":
        return "Python ek simple language hai, AI banane ke liye use hoti hai."
    else:
        return f"{topic} Software Engineering ka important topic hai."

# Testing the tool
print(ai_helper("AI"))
print(ai_helper("GitHub"))
print(ai_helper("Python"))
print("\nTool created by Humaira Mukhtar - RYK")
