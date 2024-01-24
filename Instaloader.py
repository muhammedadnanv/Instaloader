import sys
import instaloader

def download_profile_picture(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Load the profile of the specified username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download the profile picture
        loader.download_profilepic(profile.username, profile.profile_pic_url)
        print(f"Profile picture for {profile.username} downloaded successfully.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python insta_downloader.py <username>")
    else:
        username = sys.argv[1]
        download_profile_picture(username)
