import pygame
import numpy as np
from game.game_engine import GameEngine

def generate_beep_sound(frequency=440, duration=0.1, volume=0.5):
    """Generate a simple beep sound using numpy"""
    sample_rate = 44100
    n_samples = int(round(duration * sample_rate))
    
    # Create the time array
    buf = np.zeros((n_samples, 2), dtype=np.int16)
    max_amplitude = np.power(2, 15) - 1
    
    # Generate sine wave
    for i in range(n_samples):
        t = float(i) / sample_rate
        buf[i][0] = int(volume * max_amplitude * np.sin(2 * np.pi * frequency * t))
        buf[i][1] = int(volume * max_amplitude * np.sin(2 * np.pi * frequency * t))
    
    return pygame.sndarray.make_sound(buf)

def main():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    
    # Screen settings
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong - Pygame Version")
    
    # Colors
    BLACK = (0, 0, 0)
    
    # Clock
    clock = pygame.time.Clock()
    FPS = 60
    
    # Generate sound effects programmatically
    try:
        # Different frequencies for different sounds
        paddle_sound = generate_beep_sound(660, 0.1, 0.3)   # High pitch for paddle hit
        wall_sound = generate_beep_sound(440, 0.08, 0.2)    # Medium pitch for wall
        score_sound = generate_beep_sound(880, 0.3, 0.4)    # Long high pitch for score
        
        print("Generated sound effects successfully!")
    except Exception as e:
        print(f"Error generating sounds: {e}")
        # Create silent fallback sounds
        paddle_sound = pygame.mixer.Sound(buffer=bytearray([]))
        wall_sound = pygame.mixer.Sound(buffer=bytearray([]))
        score_sound = pygame.mixer.Sound(buffer=bytearray([]))
    
    # Create game engine
    engine = GameEngine(WIDTH, HEIGHT)
    engine.set_sounds(paddle_sound, wall_sound, score_sound)
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Pass all key events to game engine
                engine.handle_event(event)
        
        # Update game state
        engine.update()
        
        # Render
        screen.fill(BLACK)
        engine.render(screen)
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()