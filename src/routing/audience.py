from enum import Enum

class Audience(str, Enum):
  BEGINNER = "beginner"
  BUSINESS = "business"
  DEVELOPER = "developer"
  EXECUTIVE = "executive"
  EXPERT = "expert"

def detect_audience(user_profile, message):
  if user_profile.role == "Developer":
    return Audience.DEVELOPER

  if user_profile.role == "CEO":
    return Audience.EXECUTIVE

  if "code" in message.lower():
    return Audience.DEVELOPER

  return Audience.BEGINNER

AUDIENCE_CONFIG = {
  Audience.BEGINNER: {
    "detail": "simple",
    "examples": True,
    "technical": False,
  },
  Audience.DEVELOPER: {
    "detail": "deep",
    "examples": True,
    "technical": True,
  },
  Audience.EXECUTIVE: {
    "detail": "summary",
    "technical": False,
    "focus": "business value",
  },
}

def main():
  detect_audience()
  Audience()

if __name__ == "__main__":
  main()