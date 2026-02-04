from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "'Mission ID must start with 'M'"
                )

        if not [member
                for member in self.crew
                if member.rank == Rank.COMMANDER
                or member.rank == Rank.CAPTAIN]:
            raise ValueError(
                "Mission Must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced_crew = len(
                [m for m in self.crew if m.years_experience > 5]
            )

            if experienced_crew < total_crew / 2:
                raise ValueError(
                    "Long missions (>365 days) require at least 50% "
                    "experienced crew (5+ years)"
                )

        if [member for member in self.crew if not member.is_active]:
            raise ValueError(
                "All crew members must be active"
                )

        return self


def main() -> None:
    print("\nSpace Mission Crew Validation")
    print("="*40)

    sarah_connor: CrewMember = CrewMember(
        member_id="M001_M",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=55,
        specialization="Mission Command",
        years_experience=30,
    )

    john_smith: CrewMember = CrewMember(
        member_id="J002_M",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=40,
        specialization="Navigation",
        years_experience=12,
    )

    alice_johnson: CrewMember = CrewMember(
        member_id="A003_M",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=31,
        specialization="Engineering",
        years_experience=8,
    )

    colony: SpaceMission = SpaceMission(
        mission_name="Mars Colony Establishment",
        mission_id="M2024_MARS",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[sarah_connor, john_smith, alice_johnson],
    )

    print("Valid mission created:")
    print(f"Mission: {colony.mission_name}")
    print(f"ID: {colony.mission_id}")
    print(f"Destination: {colony.destination}")
    print(f"Duration: {colony.duration_days} days")
    print(f"Budget: {colony.budget_millions} M")
    print(f"Crew size: {len(colony.crew)}")
    print("Crew members: ")
    for m in colony.crew:
        print(f"- {m.name} ({m.rank.value}) - {m.specialization}")
    print()
    print("="*40)

    print("Expected validation error:")

    finn: CrewMember = CrewMember(
        member_id="X000_Z",
        name="Finn the human",
        rank=Rank.OFFICER,
        age=20,
        specialization="Navigation",
        years_experience=5,
    )

    try:
        colony2: SpaceMission = SpaceMission(
            mission_name="Meta Exploration",
            mission_id="M2027_JAN",
            destination="Meta",
            duration_days=999,
            budget_millions=5500.0,
            crew=[finn],
        )
        del colony2

    except ValidationError as e:
        print(e.errors()[0]["msg"].strip("Value error,"))


if __name__ == "__main__":
    main()
