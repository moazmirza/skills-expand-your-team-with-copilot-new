import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.database import initial_activities


def test_manga_maniacs_activity_is_seeded():
    activity = initial_activities["Manga Maniacs"]

    assert activity["description"] == (
        "Explore the fantastic stories of the most interesting characters from "
        "Japanese Manga (graphic novels)."
    )
    assert activity["schedule"] == "Tuesdays, 7:00 PM - 8:00 PM"
    assert activity["schedule_details"]["days"] == ["Tuesday"]
    assert activity["schedule_details"]["start_time"] == "19:00"
    assert activity["schedule_details"]["end_time"] == "20:00"
    assert activity["max_participants"] == 15
    assert activity["participants"] == []
