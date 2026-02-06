from playwright.sync_api import sync_playwright

def inspect():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        print("Navigating to Salcobrand...")
        page.goto("https://www.salcobrand.cl")
        page.wait_for_load_state("networkidle")
        
        # Take a screenshot to verify what we see
        page.screenshot(path="debug_home.png")
        print("Screenshot saved as debug_home.png")
        
        # Print some interesting elements
        print("\n--- Inspecting Selectors ---")
        
        # Current 'keep_location_button' selector: .row .btn-light
        keeps = page.locator(".row .btn-light").all()
        print(f"Found {len(keeps)} elements for '.row .btn-light'")
        for i, el in enumerate(keeps):
            print(f"Keep Button {i} text: {el.text_content().strip()}")
            
        # Current 'change_location_button' selector: .commune .select-commune
        changes = page.locator(".commune .select-commune").all()
        print(f"Found {len(changes)} elements for '.commune .select-commune'")
        for i, el in enumerate(changes):
             print(f"Change Button {i} text: {el.text_content().strip()}")

        # Look for buttons related to location
        buttons = page.locator("button:visible").all()
        print(f"\n--- Visible Buttons ---")
        for b in buttons:
            text = b.text_content().strip()
            if text:
                print(f"Button text: {text}")

        # Look for the commune selection specifically
        communes = page.locator(".commune").all()
        print(f"\n--- .commune elements ---")
        for c in communes:
            print(f"Commune HTML: {c.inner_html()[:200]}...")

        browser.close()

if __name__ == "__main__":
    inspect()
