from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def contact_validation(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC'"
                )

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified"
            )

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:

    print("\nAlien Contact Log Validation")
    print("="*40)
    print("Valid contact report:")
    zeta_report: AlienContact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received=("Greetings from Zeta Reticuli"),
    )

    print(f"ID: {zeta_report.contact_id}")
    print(f"Type: {zeta_report.contact_type.value}")
    print(f"Location: {zeta_report.location}")
    print(f"Signal: {zeta_report.signal_strength}/10")
    print(f"Duration: {zeta_report.duration_minutes} minutes")
    print(f"Witnesses: {zeta_report.witness_count}")
    print(f"Message: '{zeta_report.message_received}'")

    print()
    print("="*40)
    print("Expected validation error:")

    try:
        finn_report: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 57, Nevada",
            signal_strength=3.12,
            duration_minutes=12,
            witness_count=2,
            message_received=("Greetings from Finn The Human"),
        )

        del finn_report

    except ValidationError as e:
        print(e.errors()[0]["msg"].strip("Value error,"))


if __name__ == "__main__":
    main()
