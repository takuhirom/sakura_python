import streamlit as st
import pygame
import threading
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invader Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
clock = pygame.time.Clock()
running = False
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5
bullet_speed = -10
bullets = []
enemy_x, enemy_y = WIDTH // 2, 50
enemy_speed = 3
score = 0

def draw_player():
    pygame.draw.rect(screen, GREEN, (player_x, player_y, 50, 10))

def draw_enemy():
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 50, 10))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], 5, 10))

def game_logic():
    global player_x, enemy_x, enemy_speed, bullets, score

    # Move enemy
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= WIDTH - 50:
        enemy_speed = -enemy_speed

    # Move bullets
    bullets = [[x, y + bullet_speed] for x, y in bullets if y > 0]

    # Check for collisions
    for bullet in bullets:
        if enemy_x < bullet[0] < enemy_x + 50 and enemy_y < bullet[1] < enemy_y + 10:
            bullets.remove(bullet)
            score += 1
            break

def render_game():
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        global player_x
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append([player_x + 22, player_y])

        game_logic()

        # Render everything
        screen.fill(BLACK)
        draw_player()
        draw_enemy()
        draw_bullets()

        # Show score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Streamlit interface
def main():
    st.title("Play Invader Game")

    if st.button("Start Game"):
        if not threading.active_count() > 1:
            threading.Thread(target=render_game, daemon=True).start()
            st.write("Game is running! Close the pygame window to stop.")
        else:
            st.warning("Game is already running.")

    st.write("Use the arrow keys to move and spacebar to shoot.")

if __name__ == "__main__":
    main()
    
