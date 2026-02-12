import os
import re

def test_profile_exists():
    assert os.path.exists("PROFILE.md"), "PROFILE.md does not exist"

def test_profile_not_empty():
    assert os.path.getsize("PROFILE.md") > 0, "PROFILE.md is empty"

def test_profile_content():
    with open("PROFILE.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Use normalized whitespace for comparison
    normalized_content = " ".join(content.split())

    expected_intro_parts = [
        "嗨，我是 lostlight 👋",
        "学生开发者 & 开源爱好者",
        "安静带笑地折腾 Python + AI",
        "喜欢把想法打磨成可复用、可测试、可维护的小工具与流程"
    ]

    for part in expected_intro_parts:
        assert part in content, f"PROFILE.md is missing expected part: {part}"

    # The 'Welcome to my GitHub profile!' message is required by the GitHub Skills exercise steps
    expected_welcome = "Welcome to my GitHub profile!"
    assert expected_welcome in content, f"PROFILE.md is missing the mandatory exercise message: '{expected_welcome}'"
