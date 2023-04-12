import pytest
from chapter_summary import visualisation

def test_display_topics():
    result = [
        [('god', 0.03),('jesus', 0.02), ('edu', 0.005), ('people', 0.003), ('christ', 0.002)],
        [('key', 0.04),('clipper', 0.02), ('com', 0.006), ('chip', 0.003), ('encryption', 0.002)],
        [('game', 0.02), ('hockey', 0.015), ('team', 0.006), ('ca', 0.004), ('edu', 0.001)]
    ]

    visualisation(result)

