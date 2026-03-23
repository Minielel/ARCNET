# filter.py

# BLACKLIST: bekannte Spam-Kommentare / Schlagwörter
BLACKLIST = [
    "free porn", "visit my site", "click here", "subscribe now", 
    "check my profile", "DM for info"
]

# Optional: bekannte Nutzer, die Spam posten
BLACKLIST_USERS = [
    "spammer123", "botaccount", "clickbait_user"
]

def is_spam(comment_text: str, author_name: str) -> bool:
    """
    Prüft, ob ein Kommentar Spam ist
    """
    text_lower = comment_text.lower()
    author_lower = author_name.lower()
    
    # Prüfe gegen Blacklist
    for word in BLACKLIST:
        if word.lower() in text_lower:
            return True
    if author_lower in BLACKLIST_USERS:
        return True
    return False