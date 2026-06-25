from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1. Launch the native Chrome browser
    browser = p.chromium.launch(
        channel="chrome",
        headless=False
    )

    page = browser.new_page()
    
    # 2. Navigate to YouTube
    print("Navigating to YouTube...")
    page.goto("https://www.youtube.com")

    # 3. Locate the search bar, type the song name, and submit
    print("Searching for 'pavamalli song'...")
    search_bar = page.get_by_placeholder("Search")
    search_bar.fill("pavamalli song")
    search_bar.press("Enter")

    # 4. Wait for the search results page to load content
    page.wait_for_selector("ytd-video-renderer")

    # 5. Click the first video container in the results to play it
    print("Playing the song...")
    first_video = page.locator("ytd-video-renderer").first
    first_video.click()

    # Keeps the browser open so you can listen to the music
    input("\nPress Enter to close the automation script...")
    browser.close()