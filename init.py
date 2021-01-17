# Quick-and-dirty pygame demo of a camera that scrolls to follow
# a player. Please excuse the horrible graphics. WASD to move.

import pygame

# Actual size of the game map
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Dimensions of the part you can see
VIEW_WIDTH = 500
VIEW_HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode([VIEW_WIDTH,VIEW_HEIGHT])
clock = pygame.time.Clock()

keymap = {
'up': pygame.K_w,
'down': pygame.K_s,
'left': pygame.K_a,
'right': pygame.K_d
}

# Scale the map image to the desired dimensions; this distorts it a bit.
# Would be better to have an image of the desired size already

bg = pygame.transform.scale(
  pygame.image.load('images/bg.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Player sprite
class Sprite(pygame.sprite.Sprite):

  def __init__(self,x,y,speed):
    super().__init__()
    self.x = x
    self.y = y
    self.speed = speed

  def update(self, keys):
    '''Basic movement.'''

    if keys[keymap['up']]:
        self.y -= self.speed

    if keys[keymap['down']]:
      self.y += self.speed

    if keys[keymap['right']]:
      self.x += self.speed

    if keys[keymap['left']]:
      self.x -= self.speed

  def render(self, surf):
    ''' Sprite is represented as a circle for simplicity.'''
    pygame.draw.circle(surf, (255,0,0), (self.x, self.y), 5)

player = Sprite(500, 500, 10)

# A rectangle to represent the part of the map you can see
camera = pygame.Rect(0,0, VIEW_WIDTH,VIEW_HEIGHT)
camera.center = (player.x, player.y)

# Main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          quit()

  camera.center = (player.x, player.y)
  surf = bg.copy()

  keys = pygame.key.get_pressed()
  player.render(surf)
  player.update(keys)

  # Draw the part of the map that you can see (as defined by the camera rect)
  # onto the screen
  screen.blit(surf, (0,0), camera)

  pygame.display.flip()
  clock.tick(60)
