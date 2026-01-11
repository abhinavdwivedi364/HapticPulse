import os
import time
import pygame

os.environ["SDL_JOYSTICK_HIDAPI_PS4_RUMBLE"] = "1"

class DS4Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.controller = None
        self._initialize_controller()

    def _initialize_controller(self):
        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No controller detected.")
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def pulse(self, strength: float = 0.5, duration_ms: int = 400, count: int = 6, gap_ms: int = 200):
        """
        Triggers a haptic pattern.
        :param strength: Intensity (0.0 to 1.0)
        :param duration_ms: How long each pulse lasts
        :param count: How many pulses to send
        :param gap_ms: Silence between pulses
        """
        if not self.controller:
            return

        for i in range(count):
            # Trigger the rumble motors
            self.controller.rumble(strength, strength, duration_ms)
            
            # Since rumble is non-blocking, we must sleep to allow the pulse to finish
            # plus the gap time before the next iteration
            total_sleep = (duration_ms + gap_ms) / 1000.0
            time.sleep(total_sleep)
            
            # Essential for processing the hardware signal
            pygame.event.pump()