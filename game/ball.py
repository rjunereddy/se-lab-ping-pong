import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])
        self.sounds_loaded = False
        self.last_wall_hit = 0  # Prevent multiple sound triggers

    def set_sounds(self, paddle_sound, wall_sound, score_sound):
        self.paddle_sound = paddle_sound
        self.wall_sound = wall_sound  
        self.score_sound = score_sound
        self.sounds_loaded = True
        print("Sounds loaded into ball object")

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wall collision with bounds checking and sound
        if self.y <= 0:
            self.y = 1
            self.velocity_y = abs(self.velocity_y)  # Ensure positive velocity
            self.play_wall_sound()
        elif self.y + self.height >= self.screen_height:
            self.y = self.screen_height - self.height - 1
            self.velocity_y = -abs(self.velocity_y)  # Ensure negative velocity
            self.play_wall_sound()

    def play_wall_sound(self):
        if self.sounds_loaded:
            try:
                self.wall_sound.play()
                print("Wall sound played")
            except Exception as e:
                print(f"Error playing wall sound: {e}")

    def check_collision(self, player, ai):
        ball_rect = self.rect()
        player_rect = player.rect()
        ai_rect = ai.rect()
        
        # Check collision with player paddle
        if ball_rect.colliderect(player_rect) and self.velocity_x < 0:
            # Calculate hit position for angle variation
            relative_intersect_y = (player_rect.centery - ball_rect.centery) / (player_rect.height / 2)
            self.velocity_x = abs(self.velocity_x)  # Reverse X direction
            self.velocity_y = -relative_intersect_y * 8  # Adjust Y based on hit position
            
            # Ensure minimum speed
            self.velocity_x = max(4, min(8, abs(self.velocity_x))) * (1 if self.velocity_x > 0 else -1)
            
            # Move ball to avoid multiple collisions
            self.x = player_rect.right + 1
            
            self.play_paddle_sound()
        
        # Check collision with AI paddle
        elif ball_rect.colliderect(ai_rect) and self.velocity_x > 0:
            # Calculate hit position for angle variation
            relative_intersect_y = (ai_rect.centery - ball_rect.centery) / (ai_rect.height / 2)
            self.velocity_x = -abs(self.velocity_x)  # Reverse X direction
            self.velocity_y = -relative_intersect_y * 8  # Adjust Y based on hit position
            
            # Ensure minimum speed
            self.velocity_x = max(4, min(8, abs(self.velocity_x))) * (1 if self.velocity_x > 0 else -1)
            
            # Move ball to avoid multiple collisions
            self.x = ai_rect.left - self.width - 1
            
            self.play_paddle_sound()

    def play_paddle_sound(self):
        if self.sounds_loaded:
            try:
                self.paddle_sound.play()
                print("Paddle sound played")
            except Exception as e:
                print(f"Error playing paddle sound: {e}")

    def reset(self, scored=False):
        if scored and self.sounds_loaded:
            try:
                self.score_sound.play()
                print("Score sound played")
            except Exception as e:
                print(f"Error playing score sound: {e}")
            
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)