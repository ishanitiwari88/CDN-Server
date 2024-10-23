# test_cdn.py
import requests
import time
from rich.console import Console
from rich.table import Table

console = Console()

def test_cdn():
    # Create some test content first
    test_files = [
        "test1.txt",
        "image1.jpg",
        "document1.pdf"
    ]
    
    # Create a pretty table for results
    table = Table(title="CDN Test Results")
    table.add_column("Test", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Time", style="green")
    
    for file in test_files:
        try:
            # First request (should be slower - not cached)
            console.print(f"\n[yellow]Testing {file}...[/yellow]")
            
            start_time = time.time()
            response = requests.get(f"http://localhost:8000/{file}")
            first_time = time.time() - start_time
            
            # Wait a bit
            time.sleep(1)
            
            # Second request (should be faster - cached)
            start_time = time.time()
            response = requests.get(f"http://localhost:8000/{file}")
            second_time = time.time() - start_time
            
            # Add results to table
            table.add_row(
                file,
                "✅ Success" if response.status_code == 200 else "❌ Failed",
                f"1st: {first_time:.3f}s\n2nd: {second_time:.3f}s"
            )
            
        except requests.exceptions.ConnectionError:
            table.add_row(file, "❌ Server not reachable", "N/A")
            console.print("[red]Error: Make sure both servers are running![/red]")
            break
    
    # Display results
    console.print(table)

if __name__ == "__main__":
    console.print("[bold green]Starting CDN Tests...[/bold green]")
    test_cdn()