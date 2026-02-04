from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:

    good_station: SpaceStation = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        is_operational=True,
    )

    print("\n== Space Station Data Validation ==\n")
    print("=" * 40)

    print("Valid station created:")
    print(f"ID: {good_station.station_id}")
    print(f"Name: {good_station.name}")
    print(f"Crew: {good_station.crew_size} people")
    print(f"Power: {good_station.power_level}%")
    print(f"Oxygen: {good_station.oxygen_level}%")
    status: str = ("Operational"
                   if good_station.is_operational
                   else "non-operational")
    print(f"Status: {status}")

    print("\n")
    print("Invalid station created:")
    try:
        bad_station: SpaceStation = SpaceStation(
            station_id="ABB002",
            name="Uneverse Space Station",
            crew_size=24,
            power_level=95.5,
            oxygen_level=92.3,
            is_operational=False,
        )
        del bad_station

    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
