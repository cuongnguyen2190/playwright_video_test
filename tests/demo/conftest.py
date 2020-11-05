import os
import pytest

@pytest.fixture()
def browser_context_args():
    video_location = f"{os.path.dirname(os.path.abspath(__file__))}"
    return {
        "viewport": {"width": 1680, "height": 1080},
        "videosPath": f"{video_location}"
    }
