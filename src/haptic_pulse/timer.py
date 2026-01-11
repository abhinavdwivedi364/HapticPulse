import time
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from .controller import DS4Controller

console = Console()

class HapticTimer:
    """Logic for the interval timer with a visual progress bar and haptic feedback."""
    
    def __init__(self, interval_minutes: int, strength: float, count: int, duration: int):
        self.interval_seconds = interval_minutes * 60
        self.strength = strength
        self.count = count
        self.duration = duration
        self.hardware = DS4Controller()

    def start(self):
        """Starts the infinite timer loop with a real-time progress bar."""
        console.print(f"[bold green]▶ HapticPulse Active.[/bold green]")
        console.print(f"[grey62]Interval: {self.interval_seconds // 60} min | Pattern: {self.count}x {self.duration}ms[/grey62]\n")
        
        try:
            while True:
                # Set up the visual progress bar
                with Progress(
                    TextColumn("[bold blue]{task.description}"),
                    BarColumn(bar_width=40),
                    "[progress.percentage]{task.percentage:>3.0f}%",
                    TimeRemainingColumn(),
                    console=console,
                    transient=True # Hides the bar after it finishes
                ) as progress:
                    
                    task = progress.add_task(
                        description="Focusing...", 
                        total=self.interval_seconds
                    )

                    # Update the bar every second
                    while not progress.finished:
                        time.sleep(1)
                        progress.update(task, advance=1)

                # Trigger Haptic Feedback after progress reaches 100%
                console.print("[bold cyan]➜ Focus Check-in![/bold cyan] [grey62](Tactile anchor sent)[/grey62]")
                self.hardware.pulse(
                    strength=self.strength, 
                    duration_ms=self.duration, 
                    count=self.count
                )
                
        except KeyboardInterrupt:
            console.print("\n[bold red]⏹ Timer stopped.[/bold red] Great work today!")