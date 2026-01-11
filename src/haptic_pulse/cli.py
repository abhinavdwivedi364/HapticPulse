import typer
import time
from rich.console import Console
from .timer import HapticTimer
from .controller import DS4Controller

# Initialize Typer and Rich Console
app = typer.Typer(help="ADHD-friendly Haptic Timer using PS4 Controllers.")
console = Console()

@app.command()
def start(
    interval: int = typer.Option(25, "--interval", "-i", help="Check-in interval in minutes"),
    strength: float = typer.Option(0.5, "--strength", "-s", help="Vibration intensity (0.0 to 1.0)")
):
    """
    Start the tactile focus timer for deep work.
    """
    try:
        timer = HapticTimer(interval_minutes=interval, strength=strength)
        timer.start()
    except RuntimeError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

@app.command()
def test(
    strength: float = typer.Option(0.6, "--strength", "-s", help="Vibration intensity"),
    duration: int = typer.Option(2000, "--duration", "-d", help="Duration of the pulse in ms")
):
    """
    Test if the controller vibration is working correctly.
    """
    console.print("[bold yellow]Testing hardware connection...[/bold yellow]")
    try:
        hw = DS4Controller()
        console.print(f"Connected to: [bold cyan]{hw.controller.get_name()}[/bold cyan]")
        
        # Perform a double-pulse pattern to confirm it's working
        console.print("Sending haptic feedback pattern...")
        
        # First pulse
        hw.pulse(strength=strength, duration_ms=duration)
        time.sleep(0.2) # Short gap
        # Second pulse
        hw.pulse(strength=strength, duration_ms=duration)
        
        console.print("[bold green]✔ Vibration successful![/bold green]")
        
    except Exception as e:
        console.print(f"[bold red]Test failed:[/bold red] {e}")
        console.print("\n[yellow]Troubleshooting tips:[/yellow]")
        console.print("1. Ensure the controller is connected via USB (most reliable).")
        console.print("2. If using Bluetooth, ensure DS4Windows is running or the controller is paired correctly.")

if __name__ == "__main__":
    app()