import typer
from .timer import HapticTimer
from .controller import DS4Controller

app = typer.Typer(help="ADHD-friendly Haptic Timer with Pulse Patterns.")

@app.command()
def start(
    interval: int = typer.Option(25, "--interval", "-i", help="Minutes between check-ins"),
    strength: float = typer.Option(0.5, "--strength", "-s", min=0.0, max=1.0),
    count: int = typer.Option(2, "--count", "-c", help="Number of pulses per check-in"),
    duration: int = typer.Option(400, "--duration", "-d", help="Duration of each pulse in ms")
):
    """Start the timer with a custom pulse pattern."""
    timer = HapticTimer(interval, strength, count, duration)
    timer.start()

@app.command()
def test(
    strength: float = 0.5, 
    count: int = 6, 
    duration: int = 300
):
    hw = DS4Controller()
    hw.pulse(strength=strength, count=count, duration_ms=duration)

if __name__ == "__main__":
    app()