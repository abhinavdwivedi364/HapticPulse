import time
from rich.console import Console
from .controller import DS4Controller

console = Console()

class HapticTimer:
    """Logic for the interval timer and ADHD-friendly notification."""
    
    def __init__(self, interval_minutes: int, strength: float):
        self.interval_seconds = interval_minutes * 60
        self.strength = strength
        self.hardware = DS4Controller()

    def start(self):
        """Starts the infinite timer loop."""
        console.print(f"[bold green]▶ HapticPulse Active.[/bold green] Interval: {self.interval_seconds // 60} min.")
        console.print("[grey62]Keep the controller in your pocket or lap for tactile anchoring.[/grey62]\n")
        
        try:
            while True:
                time.sleep(self.interval_seconds)
                
                console.print("[bold cyan]➜ Focus Check-in![/bold cyan] Sending pulse...")
                self.hardware.pulse(strength=self.strength)
                
        except KeyboardInterrupt:
            console.print("\n[bold red]⏹ Timer stopped.[/bold red] Take a break!")