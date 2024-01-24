import instaloader

def download_profile(username):
    loader = instaloader.Instaloader()

    try:
        # Load the profile of the specified username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Print profile information
        print("Username:", profile.username)
        print("Full Name:", profile.full_name)
        print("Followers:", profile.followers)
        print("Following:", profile.followees)
        print("Bio:", profile.biography)

        # Download profile picture
        loader.download_pic(filename=username, profile_pic_only=True)

        # Download the 10 most recent posts
        for post in profile.get_posts()[:10]:
            print("Post:", post.url)
            loader.download_post(post, target=username)

        # Download all saved posts
        for saved_post in profile.get_saved_posts():
            print("Saved Post:", saved_post.url)
            loader.download_post(saved_post, target=username)

        # Download all stories
        for story in profile.get_stories():
            print("Story:", story.url)
            loader.download_story(story, target=username)

        # Download IGTV videos
        for igtv_video in profile.get_igtv_videos():
            print("IGTV Video:", igtv_video.url)
            loader.download_igtv(igtv_video, target=username)

        # Download tagged photos
        for tagged_post in profile.get_tagged_posts():
            print("Tagged Post:", tagged_post.url)
            loader.download_post(tagged_post, target=username)

        # Download profile highlights
        for highlight in profile.get_highlights():
            print("Highlight:", highlight.url)
            loader.download_profilepic(highlight, target=username)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")

if __name__ == "__main__":
    # Replace 'target_username' with the Instagram username you want to download
    target_username = 'target_username'
    download_profile(target_username)
