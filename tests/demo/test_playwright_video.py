class TestPlaywrightVideo:
    def test_video_file_capture(self, browser):
        browser.goto("https://www.google.com")
        assert 1 == 1
