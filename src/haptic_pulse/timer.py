import time
from rich.console import Console
from .controller import DS4Controller

console = Console()

class HapticTimer:
    def __init__(self, interval_minutes: int, strength: float, count: int, duration: int):
        self.interval_seconds = interval_minutes * 60
        self.strength = strength
        self.count = count
        self.duration = duration
        self.hardware = DS4Controller()

    def start(self):
        console.print(f"[bold green]▶ HapticPulse Active.[/bold green] Interval: {self.interval_seconds // 60} min.")
        console.print(f"[grey62]Pattern: {self.count}x {self.duration}ms pulses.[/grey62]\n")
        
        try:
            while True:
                time.sleep(self.interval_seconds)
                console.print("[bold cyan]➜ Focus Check-in![/bold cyan]")
                
                # Execute the pattern
                self.hardware.pulse(
                    strength=self.strength, 
                    duration_ms=self.duration, 
                    count=self.count
                )
        except KeyboardInterrupt:
            console.print("\n[bold red]⏹ Timer stopped.[/bold red]")