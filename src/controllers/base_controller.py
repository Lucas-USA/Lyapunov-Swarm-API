"""Base interfaces for Lyapunov swarm controllers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseController(ABC):
    """Minimal interface for controller implementations."""

    def __init__(self, name: str = "base-controller") -> None:
        self.name = name

    @abstractmethod
    def reset(self) -> None:
        """Reset any controller state before a new rollout."""

    @abstractmethod
    def compute_control(self, state: Any, **kwargs: Any) -> Any:
        """Return the control action for the current system state."""
