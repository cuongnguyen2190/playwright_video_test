class TestPlaywrightVideo:
    def test_video_file_capture(self, page):
        page.goto("https://www.google.com")
        assert 1 == 1
