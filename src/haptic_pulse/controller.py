import os
import pygame

# Enable vibration support for PS4 controllers over Bluetooth on Windows
os.environ["SDL_JOYSTICK_HIDAPI_PS4_RUMBLE"] = "1"

class DS4Controller:
    """Handles the hardware interaction with the DualShock 4 controller."""
    
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.controller = None
        self._initialize_controller()

    def _initialize_controller(self):
        """Detects and initializes the first available controller."""
        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No controller detected. Please connect via USB or Bluetooth.")
        
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def pulse(self, strength: float = 0.6, duration_ms: int = 1000):
        """Triggers a haptic feedback pulse."""
        if self.controller:
            # Rumble parameters: (low_frequency, high_frequency, duration)
            self.controller.rumble(strength, strength, duration_ms)
            # Pump events to ensure the signal is sent to the hardware
            pygame.event.pump()