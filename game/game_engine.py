import pygame
from .paddle import Paddle
from .ball import Ball

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 15
        self.paddle_height = 100

        # Create game objects
        self.player = Paddle(20, height // 2 - self.paddle_height // 2, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20 - self.paddle_width, height // 2 - self.paddle_height // 2, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 15, 15, width, height)

        # Game state
        self.player_score = 0
        self.ai_score = 0
        self.game_over = False
        self.winning_score = 3  # Best of 5 (first to 3 wins)
        self.show_replay_options = False
        self.replay_timer = 0
        
        # Fonts
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 24)
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.GRAY = (128, 128, 128)

    def set_sounds(self, paddle_sound, wall_sound, score_sound):
        print("Setting sounds in game engine...")
        self.ball.set_sounds(paddle_sound, wall_sound, score_sound)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.game_over and self.show_replay_options:
                if event.key == pygame.K_3:
                    self.winning_score = 2  # Best of 3
                    self.reset_game()
                elif event.key == pygame.K_5:
                    self.winning_score = 3  # Best of 5
                    self.reset_game()
                elif event.key == pygame.K_7:
                    self.winning_score = 4  # Best of 7
                    self.reset_game()

    def update(self):
        if self.game_over:
            # Handle replay menu delay
            if not self.show_replay_options:
                self.replay_timer += 1
                if self.replay_timer >= 120:  # Show after 2 seconds
                    self.show_replay_options = True
            return
        
        # Handle continuous key presses for player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-8, self.height)
        if keys[pygame.K_s]:
            self.player.move(8, self.height)
        
        # Update ball position and check collisions
        self.ball.move()
        self.ball.check_collision(self.player, self.ai)
        
        # AI movement
        self.ai.auto_track(self.ball, self.height)
        
        # Scoring
        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset(scored=True)
            self.check_game_over()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.ball.reset(scored=True)
            self.check_game_over()

    def check_game_over(self):
        if self.player_score >= self.winning_score or self.ai_score >= self.winning_score:
            self.game_over = True
            self.replay_timer = 0

    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.game_over = False
        self.show_replay_options = False
        self.ball.reset()
        self.player.y = self.height // 2 - self.paddle_height // 2
        self.ai.y = self.height // 2 - self.paddle_height // 2

    def render(self, screen):
        if self.game_over:
            self.render_game_over(screen)
        else:
            self.render_game(screen)

    def render_game(self, screen):
        # Draw center line
        for y in range(0, self.height, 20):
            pygame.draw.rect(screen, self.GRAY, (self.width // 2 - 1, y, 2, 10))
        
        # Draw paddles
        pygame.draw.rect(screen, self.WHITE, self.player.rect())
        pygame.draw.rect(screen, self.WHITE, self.ai.rect())
        
        # Draw ball
        pygame.draw.ellipse(screen, self.WHITE, self.ball.rect())
        
        # Draw scores
        player_score_text = self.font.render(str(self.player_score), True, self.WHITE)
        ai_score_text = self.font.render(str(self.ai_score), True, self.WHITE)
        screen.blit(player_score_text, (self.width // 4, 20))
        screen.blit(ai_score_text, (3 * self.width // 4, 20))
        
        # Draw game info
        info_text = self.small_font.render(f"First to {self.winning_score} wins - W/S to move - ESC to quit", True, self.GRAY)
        screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2, self.height - 30))

    def render_game_over(self, screen):
        # Determine winner
        if self.player_score >= self.winning_score:
            winner_text = "PLAYER WINS!"
            winner_color = (0, 255, 0)  # Green for player
        else:
            winner_text = "AI WINS!"
            winner_color = (255, 0, 0)  # Red for AI
        
        # Draw winner text
        winner_surface = self.large_font.render(winner_text, True, winner_color)
        winner_rect = winner_surface.get_rect(center=(self.width // 2, self.height // 2 - 80))
        screen.blit(winner_surface, winner_rect)
        
        # Draw final score
        score_text = self.font.render(f"Final Score: {self.player_score} - {self.ai_score}", True, self.WHITE)
        score_rect = score_text.get_rect(center=(self.width // 2, self.height // 2 - 20))
        screen.blit(score_text, score_rect)
        
        if self.show_replay_options:
            # Draw replay options
            options = [
                "Press 3 for Best of 3",
                "Press 5 for Best of 5", 
                "Press 7 for Best of 7",
                "Press ESC to Quit"
            ]
            
            for i, option in enumerate(options):
                option_surface = self.small_font.render(option, True, self.WHITE)
                option_rect = option_surface.get_rect(center=(self.width // 2, self.height // 2 + 30 + i * 35))
                screen.blit(option_surface, option_rect)
        else:
            # Draw loading message
            loading_text = self.small_font.render("Game Over...", True, self.GRAY)
            loading_rect = loading_text.get_rect(center=(self.width // 2, self.height // 2 + 30))
            screen.blit(loading_text, loading_rect)