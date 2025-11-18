#!/usr/bin/env python3
"""
Instagram Profile Checker
Checks if Instagram profiles exist for a given name.
"""

import instaloader
import sys
from typing import List, Dict


def search_instagram_profiles(search_name: str) -> List[Dict[str, str]]:
    """
    Search for Instagram profiles matching the given name.
    
    Args:
        search_name: The name to search for
        
    Returns:
        List of dictionaries containing profile information
    """
    loader = instaloader.Instaloader()
    results = []
    
    # Generate potential username variations
    # Remove spaces and convert to lowercase for potential usernames
    username_variants = [
        search_name.replace(" ", "").lower(),
        search_name.replace(" ", "_").lower(),
        search_name.replace(" ", ".").lower(),
        search_name.replace(" ", ""),
    ]
    
    # Remove duplicates
    username_variants = list(set(username_variants))
    
    print(f"Searching for Instagram profiles for: {search_name}")
    print(f"Checking username variations: {username_variants}\n")
    
    for username in username_variants:
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
            results.append({
                "username": profile.username,
                "full_name": profile.full_name,
                "bio": profile.biography,
                "followers": profile.followers,
                "following": profile.followees,
                "posts": profile.mediacount,
                "is_private": profile.is_private,
                "profile_url": f"https://www.instagram.com/{profile.username}/"
            })
            print(f"✓ Found profile: @{profile.username}")
            print(f"  Full Name: {profile.full_name}")
            print(f"  Bio: {profile.biography[:100] if profile.biography else 'N/A'}")
            print(f"  Followers: {profile.followers}")
            print(f"  Following: {profile.followees}")
            print(f"  Posts: {profile.mediacount}")
            print(f"  Private: {profile.is_private}")
            print(f"  URL: https://www.instagram.com/{profile.username}/")
            print()
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"✗ Profile not found: @{username}")
        except instaloader.exceptions.ConnectionException as e:
            print(f"⚠ Connection error for @{username}: {e}")
        except Exception as e:
            print(f"⚠ Error checking @{username}: {e}")
    
    return results


def main():
    """Main function to search for Instagram profiles."""
    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print("Usage: python find_insta_profile.py [name]")
        print()
        print("Search for Instagram profiles matching the given name.")
        print()
        print("Arguments:")
        print("  name    Name to search for (default: 'subrahmanyam kommireddy')")
        print()
        print("Examples:")
        print("  python find_insta_profile.py")
        print("  python find_insta_profile.py \"john doe\"")
        print("  python find_insta_profile.py \"subrahmanyam kommireddy\"")
        return 0
    
    # Default search name
    search_name = "subrahmanyam kommireddy"
    
    # Allow command line argument to override
    if len(sys.argv) > 1:
        search_name = " ".join(sys.argv[1:])
    
    print("=" * 60)
    print("Instagram Profile Checker")
    print("=" * 60)
    print()
    
    results = search_instagram_profiles(search_name)
    
    print("\n" + "=" * 60)
    if results:
        print(f"Summary: Found {len(results)} profile(s)")
        for result in results:
            print(f"  - @{result['username']} ({result['full_name']})")
    else:
        print("Summary: No profiles found")
    print("=" * 60)
    
    return 0 if results else 1


if __name__ == "__main__":
    sys.exit(main())
