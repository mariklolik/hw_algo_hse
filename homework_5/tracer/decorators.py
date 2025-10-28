from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast


F = TypeVar("F", bound=Callable[..., Any])


class _TracerState:
    __slots__ = ("depth", "enabled")

    def __init__(self) -> None:
        self.depth = 0
        self.enabled = True


_state = _TracerState()


def _format_args(*args: Any, **kwargs: Any) -> str:
    positional = ", ".join(repr(arg) for arg in args)
    keywords = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
    if positional and keywords:
        return f"{positional}, {keywords}"
    return positional or keywords


def trace_recursion(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not _state.enabled:
            return func(*args, **kwargs)

        indent = "    " * _state.depth
        signature = _format_args(*args, **kwargs)
        print(f"{indent}-> {func.__name__}({signature})")

        _state.depth += 1
        try:
            result = func(*args, **kwargs)
        except Exception as exc:  # pragma: no cover - just for logging
            _state.depth -= 1
            indent = "    " * _state.depth
            print(f"{indent}<- {func.__name__} raised {exc!r}")
            raise
        else:
            _state.depth -= 1
            indent = "    " * _state.depth
            print(f"{indent}<- {func.__name__} -> {result!r}")
            return result

    return cast(F, wrapper)


class disable_tracing:
    """Context manager to temporarily disable tracing within traced calls."""

    __slots__ = ("_previous",)

    def __init__(self) -> None:
        self._previous = None

    def __enter__(self) -> None:
        self._previous = _state.enabled
        _state.enabled = False

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        _state.enabled = bool(self._previous)
        self._previous = None

