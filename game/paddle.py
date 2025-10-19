import pygame
import random

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 8

    def move(self, dy, screen_height):
        new_y = self.y + dy
        # Keep paddle within screen bounds
        if new_y >= 0 and new_y + self.height <= screen_height:
            self.y = new_y

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def auto_track(self, ball, screen_height):
        # AI with some imperfection to make it beatable
        target_y = ball.y - self.height // 2 + ball.height // 2
        
        # Add some randomness to AI reaction
        if random.random() > 0.2:  # 80% chance to react
            # Only move if significantly off target
            if abs(self.y - target_y) > 25:
                if self.y > target_y:
                    self.move(-self.speed * 0.8, screen_height)  # Slightly slower than player
                else:
                    self.move(self.speed * 0.8, screen_height)