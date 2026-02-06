from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("Navigating to Salcobrand...")
        try:
            page.goto("https://www.salcobrand.cl", timeout=60000)
            print("Page loaded.")
            
            # Wait a bit for dynamic content
            page.wait_for_timeout(5000)
            
            print("\n--- Accessibility Tree (Snapshot) ---")
            snapshot = page.accessibility.snapshot()
            if snapshot:
                # Helper to print recursively
                def print_node(node, indent=0):
                    name = node.get("name", "")
                    role = node.get("role", "")
                    print(f"{'  ' * indent}{role}: {name}")
                    for child in node.get("children", []):
                        print_node(child, indent + 1)
                
                print_node(snapshot)
            else:
                print("No accessibility snapshot available.")
            
            print("\n--- Button Elements ---")
            buttons = page.locator("button").all()
            for i, btn in enumerate(buttons):
                if btn.is_visible():
                    print(f"Button {i}: '{btn.text_content().strip()}'")

            print("\n--- Header Commune ---")
            commune = page.locator(".commune").first
            if commune.is_visible():
                print(f"Commune text: {commune.text_content()}")
            else:
                print(".commune element not visible or not found")
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run()
