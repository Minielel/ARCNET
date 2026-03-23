# main.py

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from filter import is_spam

# ARCNET Info
print("ARCNET")
print("Automated Recognition and Cleansing Network for Engagement Threats")
print("---------------------------------------------------------------\n")

# YouTube API Scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

def fetch_comments(youtube, video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    while request:
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "id": item["snippet"]["topLevelComment"]["id"],
                "author": comment["authorDisplayName"],
                "text": comment["textDisplay"]
            })
        request = youtube.commentThreads().list_next(request, response)
    return comments

def delete_comment(youtube, comment_id):
    try:
        youtube.comments().delete(id=comment_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting comment {comment_id}: {e}")
        return False

def main():
    youtube = get_authenticated_service()
    video_id = input("Enter Video ID to clean: ").strip()
    print("Fetching comments...")
    comments = fetch_comments(youtube, video_id)
    print(f"Total comments fetched: {len(comments)}")
    
    spam_comments = [c for c in comments if is_spam(c["text"], c["author"])]
    print(f"Spam comments detected: {len(spam_comments)}")
    
    if spam_comments:
        confirm = input("Delete all detected spam comments? (yes/no): ").strip().lower()
        if confirm == "yes":
            for c in spam_comments:
                delete_comment(youtube, c["id"])
            print("All spam comments deleted.")
        else:
            print("No comments deleted.")
    else:
        print("No spam detected.")

if __name__ == "__main__":
    main()