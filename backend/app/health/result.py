from dataclasses import dataclass


@dataclass
class HealthResult:
    service_name: str
    status: str
    response_time_ms: float