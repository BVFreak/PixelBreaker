import pygame
# speed to pulse
# 632ms

class PulsatingScreen:
    def __init__(self, pulse_duration, base_brightness, brightness_range):
        self.pulse_duration = pulse_duration
        self.base_brightness = base_brightness
        self.brightness_range = brightness_range
        self.last_pulse_time = pygame.time.get_ticks()
        
    def calculate_pulse_brightness(self, time_since_pulse):
        pulse_progress = min(time_since_pulse / self.pulse_duration, 1.0)
        return self.base_brightness + int(self.brightness_range * pulse_progress)
    
    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        time_since_pulse = current_time - self.last_pulse_time

        # Clear the screen with pulsating brightness
        brightness = self.calculate_pulse_brightness(time_since_pulse)
        screen.fill((brightness, brightness, brightness))

        # Check if a new pulse should start
        if time_since_pulse >= self.pulse_duration:
            self.last_pulse_time = current_time