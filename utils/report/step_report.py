# reporting/step_report.py
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, List
import re


@dataclass
class StepResult:
    name: str
    status: str  # "PASO" o "FALLO"
    timestamp: str
    screenshot_path: Optional[Path] = None
    error: Optional[str] = None

class StepCollector:
    def __init__(self, artifacts_dir: Path, test_name: str):
        self.artifacts_dir = artifacts_dir
        self.test_name = test_name
        self.steps: List[StepResult] = []
        (self.artifacts_dir / "screenshots").mkdir(parents=True, exist_ok=True)

    def add_step(self, name: str, status: str, screenshot_path: Optional[Path] = None, error: Optional[str] = None):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.steps.append(StepResult(name=name, status=status, timestamp=ts, screenshot_path=screenshot_path, error=error))

def _safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", name).strip("_")[:80]

class StepRunner:
    def __init__(self, page, collector: StepCollector, take_screenshot_on_pass: bool = False):
        self.page = page
        self.collector = collector
        self.take_screenshot_on_pass = take_screenshot_on_pass

    def step(self, name: str, fn):
        screenshot_path = None
        try:
            result = fn()

            if self.take_screenshot_on_pass:
                screenshot_path = self._screenshot(name)

            self.collector.add_step(name=name, status="PASÓ", screenshot_path=screenshot_path)
            return result
        except Exception as e:
            screenshot_path = self._screenshot(name + "_FALLO")
            self.collector.add_step(name=name, status="FALLÓ", screenshot_path=screenshot_path, error=str(e))
            raise

    def _screenshot(self, name: str):
        filename = f"{_safe_name(self.collector.test_name)}__{_safe_name(name)}.png"
        path = self.collector.artifacts_dir / "screenshots" / filename
        self.page.screenshot(path=str(path), full_page=True)
        return path