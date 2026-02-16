> *This project has been created as part of the 42 curriculum by rhssayn.*

# 🌌 Cosmic Data
### *Discover Pydantic Models & Validation*
---

## 📌 Description
**Cosmic Data** is a Python project focused on mastering **Pydantic data validation**:
model creation, field constraints, custom validation, and nested data structures.

Set in the *Cosmic Data Observatory*, you'll create robust validation models, implement business rules,
and manage complex data structures using production-grade Pydantic patterns.

---

## 🎯 Project Objectives
- 🏗️ Create BaseModel classes with field validation
- 🔍 Use Field constraints for advanced validation
- ✨ Implement custom validation with @model_validator
- 🎯 Work with Enums for categorical data
- 🔗 Design nested Pydantic models and relationships

---

## 🧪 Exercises Overview

### 🌍 Exercise 0 — Space Station Data
Create a SpaceStation model with constraints on crew size, power levels, and operational status.
Learn basic Pydantic validation and type conversion.

**Key Concepts:** BaseModel, Field validation, type hints, datetime handling

---

### 👽 Exercise 1 — Alien Contact Logs
Build an AlienContact model with custom validation rules using @model_validator.
Implement business logic for different contact types.

**Key Concepts:** @model_validator, Enums, custom validation, conditional rules

---

### 👨‍🚀 Exercise 2 — Space Crew Management
Master nested models by building a SpaceMission with a crew list.
Validate complex mission safety requirements.

**Key Concepts:** Nested models, List validation, complex business rules

---

## ⚙️ Rules & Constraints
- Python **3.10+**
- flake8 compliance required
- **Type hints required** for all functions
- Pydantic **2.x**
- Use `@model_validator(mode='after')` (not deprecated @validator)

---

## 📁 Project Structure
```
your-repo/
├── ex0/space_station.py
├── ex1/alien_contact.py
└── ex2/space_crew.py
```

---

## 🚀 Execution
```bash
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

---

## 🔑 Key Pydantic Concepts

**BaseModel** - Foundation for all Pydantic models
```python
from pydantic import BaseModel

class SpaceStation(BaseModel):
    station_id: str
    crew_size: int
```

**Field** - Add constraints and validation
```python
from pydantic import Field

crew_size: int = Field(..., ge=1, le=20)
power_level: float = Field(ge=0.0, le=100.0)
```

**@model_validator** - Custom validation logic
```python
@model_validator(mode='after')
def validate_rules(self):
    # Your validation logic
    return self
```

**Enum** - Type-safe categorical data
```python
from enum import Enum

class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
```

**Nested Models** - Complex relationships
```python
crew: List[CrewMember]
```

---

## 📦 Authorized Imports
- pydantic (BaseModel, Field, model_validator)
- enum
- datetime
- json, csv
- Standard library

---

## 🎓 Learning Outcomes

✅ Create BaseModel classes with validation  
✅ Use Field constraints  
✅ Implement custom validation  
✅ Work with Enums  
✅ Design nested models  
✅ Validate lists and relationships  
✅ Build robust data pipelines  

---

## 👤 Author

*Created as part of the 42 curriculum — Professional Data Validation*

If this project helps you master Pydantic, feel free to ⭐ the repository!

**Pydantic is the foundation of robust data validation in Python. You've learned to create systems that ensure data integrity and prevent invalid data.** 🌌✨