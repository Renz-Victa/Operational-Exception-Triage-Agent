from fallback_templates import FALLBACK_TEMPLATES

response = FALLBACK_TEMPLATES["tool_failure"]["message"]

FALLBACK_TEMPLATES = {
  "unknown_intent": {
    "message": "I'm not sure what you're asking. Can you rephrase? ",
    "severity": "low",
    "retry": False,
    "action": "retry_intent"
  },
  "tool_failure": {
    "message": "The external service failed. ",
    "severity": "medium",
    "retry": True,
    "action": "retry_tool"
  },
  "missing_context": {
    "message": "I don't have enough information to answer confidently. Can you provide more details? ",
    "severity": "low",
    "retry": False,
    "action": "ask_clarification"
  },
  "tool_timeout": {
    "message": "The service took too long to respond. Please try again. ",
    "severity": "medium",
    "retry": True,
    "action": "retry"
  },
  "invalid_input": {
    "message": "I couldn't process that request. Please check the format and try again. ",
    "severity": "medium",
    "retry": True,
    "action": "request_fix"
  },
  "internal_error": {
    "text": "Something went wrong while processing your request. ",
    "severity": "medium",
    "retry": True,
    "action": "log_error"
  },
  "unsafe_request": {
    "message": "I can't help with that request, but I can help with a safe alternative. ",
    "severity": "low",
    "retry": True,
    "action": "provide_alternative"
  },
  "retry_policy": {
    "enabled": True,
    "max_attempts": 3,
    "backoff_seconds": 5
  }
}