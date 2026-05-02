import re

def sanitize_input(text):
    """
    AI Developer 3: Security & Sanitization Layer
    Checks for HTML tags and basic prompt injection.
    """
    # 1. Strip HTML tags (Prevents XSS and messy inputs)
    clean_text = re.sub(r'<.*?>', '', text)
    
    # 2. Basic Prompt Injection Detection
    # Look for keywords that try to bypass AI instructions
    forbidden_phrases = ["ignore previous", "system admin", "you are now a", "bypass"]
    
    is_safe = True
    for phrase in forbidden_phrases:
        if phrase in clean_text.lower():
            is_safe = False
            break
            
    return clean_text, is_safe