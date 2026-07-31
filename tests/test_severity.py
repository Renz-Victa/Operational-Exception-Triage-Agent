import pytest
from severity import classify_severity, Severity, determine_severity

def test_low():
  assert classify_severity(3) == Severity.LOW

def test_medium():
  assert classify_severity(8) == Severity.MEDIUM

def test_high():
  assert classify_severity(15) == Severity.HIGH

def test_critical():
  assert classify_severity(20) == Severity.CRITICAL

def test_password_leak():
  result = determine_severity(
    "Database credentials were leaked publicly."
  )
  assert result == "critical"

def test_wifi():
  result = determine_severity(
    "Internet connection is slow"
  )
  assert result == "high"

def test_quality():
  result = determine_severity(
    "Low quality material"
  )
  assert result == "high"

def test_delay_of_shipment():
  result = determine_severity(
    "Shipment is delayed"
  )
  assert result == "high"

def test_slow_response():
  result = determine_severity(
    "API latency increased to 4 seconds."
  )
  assert result == "medium"

def test_negative_score():
  with pytest.raises(ValueError):
    classify_severity(-1)

def main():
  test_low()
  test_medium()
  test_high()
  test_critical()
  test_password_leak()
  test_wifi()
  test_quality()
  test_delay_of_shipment()
  test_slow_response()
  test_negative_score()

if __name__ == "__main__":
  main()