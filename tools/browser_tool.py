import subprocess
from agentscope.service import ServiceResponse

def browser_navigate(url: str) -> ServiceResponse:
    """
    Simulates or uses a headless browser to navigate to a URL and return the visible text/errors.
    In a full production environment, this uses Playwright.
    """
    try:
        # Check if playwright is installed for real execution
        import playwright
        script = f"""
from playwright.sync_api import sync_playwright
import sys
import base64

def run():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Listen for console errors
            errors = []
            page.on("console", lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
            
            response = page.goto("{url}")
            page.wait_for_load_state("networkidle")
            
            title = page.title()
            # Extract main visible text (simplified)
            body_text = page.locator("body").inner_text()[:500] 
            
            # Take a screenshot
            screenshot_bytes = page.screenshot(type="jpeg", quality=50)
            screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            
            print(f"TITLE: {{title}}")
            print(f"STATUS: {{response.status if response else 'Unknown'}}")
            print(f"ERRORS: {{errors}}")
            print(f"PREVIEW: {{body_text}}")
            print(f"SCREENSHOT_B64: {{screenshot_b64}}")
            
            browser.close()
    except Exception as e:
        print(f"BROWSER_ERROR: {{str(e)}}")

run()
"""
        import tempfile
        import sys
        import os
        
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
            f.write(script.encode())
            tmp_path = f.name
            
        result = subprocess.run([sys.executable, tmp_path], capture_output=True, text=True)
        os.remove(tmp_path)
        
        if result.returncode == 0:
            return ServiceResponse(status=ServiceResponse.SUCCESS, content=result.stdout)
        else:
            return ServiceResponse(status=ServiceResponse.ERROR, content=result.stderr)
            
    except ImportError:
        # Fallback simulated response if playwright is missing
        return ServiceResponse(
            status=ServiceResponse.SUCCESS, 
            content=f"[Simulated Browser] Navigated to {url}.\nStatus: 200\nTitle: Simulated Page\nPreview: Page loaded successfully. (Install 'playwright' for real execution)"
        )
