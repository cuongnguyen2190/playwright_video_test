import pytest
import os
from playwright import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        try:
            video_location = f"{os.path.dirname(os.path.abspath(__file__))}"
            new_browser = p.chromium.launch(headless=False)
            page = new_browser.newPage(
                viewport={"width": 1680, "height": 1080},
                videosPath=f"{video_location}"
            )
            yield page
            new_browser.close()
            p.stop()
        except Exception as e:
            print(e)
            pytest.skip("Exception")
