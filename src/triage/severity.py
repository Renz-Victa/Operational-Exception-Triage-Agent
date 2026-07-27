from enum import IntEnum
from dataclasses import dataclass

class Severity(IntEnum):
  INFO = 0
  LOW = 1
  MEDIUM = 2
  HIGH = 3
  CRITICAL = 4

@dataclass(frozen=True)
class SeverityConfig:
  name: str
  requires_confirmation: bool
  stop_execution: bool
  notify_user: bool
  log_level: str

SEVERITY = {
  Severity.INFO: SeverityConfig(
    name="Info",
    requires_confirmation=False,
    stop_execution=False,
    notify_user=False,
    log_level="INFO",
  ),
  Severity.LOW: SeverityConfig(
    name="Low",
    requires_confirmation=False,
    stop_execution=False,
    notify_user=True,
    log_level="WARNING",
  ),
  Severity.HIGH: SeverityConfig(
    name="High",
    requires_confirmation=True,
    stop_execution=False,
    notify_user=True,
    log_level="WARNING",
  ),
  Severity.HIGH: SeverityConfig(
    name="High",
    requires_confirmation=True,
    stop_execution=False,
    notify_user=True,
    log_level="ERROR",
  ),
  Severity.Critical: SeverityConfig(
    name="Critical",
    requires_confirmation=True,
    stop_execution=True,
    notify_user=True,
    log_level="CRITICAL",
  ),
}

def should_stop(level: Severity) -> bool:
  return SEVERITY[level].stop_execution

def requires_confirmation(level: Severity) -> bool:
  return SEVERITY[level].requires_confirmation

def should_notify(level: Severity) -> bool:
  return SEVERITY[level].notify_user 

Incident(
  severity=Severity.CRITICAL,
  category=Severity.SECURITY,
  message="API key detected in output."
)

score = (
  security_risk * 5 +
  data_loss * 4 +
  financial_risk * 4 +
  privacy_risk * 5 + 
  user_impact * 3 +
)

if score >= 20:
  severity = Severity.CRITICAL
elif score >= 15:
  severity = Severity.HIGH
elif score >= 8:
  severity = Severity.MEDIUM
elif score >= 3:
  severity = Severity.LOW
else: 
  severity = Severity.INFO

def main():
  Severity()
  SeverityConfig()

if __name__ == "__main__":
  main()