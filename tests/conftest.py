import pytest
from pages.home.home_page import HomePage
from pathlib import Path
from utils.report.step_report import StepCollector, StepRunner
from utils.report.pdf_writer import generate_pdf

@pytest.fixture
def home_page(page):
    home_page = HomePage(page)
    home_page.open()
    return home_page

@pytest.fixture
def step_report(request, page):  # usa fixture "page" de pytest-playwright
    test_name = request.node.name
    artifacts_dir = Path("artifacts") / test_name
    collector = StepCollector(artifacts_dir=artifacts_dir, test_name=test_name)
    runner = StepRunner(page=page, collector=collector, take_screenshot_on_pass=False)
    yield runner

    # al terminar el test, generar PDF
    pdf_path = artifacts_dir / f"{test_name}.pdf"
    generate_pdf(pdf_path, test_name, collector.steps)