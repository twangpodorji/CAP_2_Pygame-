import unittest
import pygame
from Objects_ofgam import Player, Bar, Dot, Particle, Button, ScoreCard, Message

class TestPlayer(unittest.TestCase):
  def setUp(self):    # this function will check the environment and creates a window for game and the object for the use 
      self.win = pygame.display.set_mode((288, 512))
      self.player = Player(self.win)

  def test_move_up(self):   # this function tells the player to move up and then checks the player position 
      self.player.update(True, True)
      self.assertGreater(self.player.rect.y, -1)

class Player:
   def __init__(self, win): # is for the rectangle and for its shape
      self.win = win
      self.rect = pygame.Rect(0, 0, 50, 50) # player's rectangle in my game 

   def handle_event(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN:
          self.rect.y -= 10

   def update(self, move_up, move_down):
      if move_up:
          self.rect.y -= 10 # Moving up of the rectangle(ball)
      if move_down:
          self.rect.y += 10 # Moving down the rectangle(ball)


class TestBar(unittest.TestCase):
  def setUp(self):
      self.win = pygame.display.set_mode((800, 600))
      self.bar = Bar(100, 100, 50, (255, 255, 255), self.win)

  def test_move(self):
      initial_x = self.bar.rect.x
      self.bar.update(10)
      final_x = self.bar.rect.x
      self.assertEqual(initial_x - 10, final_x)

  def test_kill(self):
      self.bar.update(-100)
      self.assertFalse(self.bar.alive())



class TestDot(unittest.TestCase):
  def setUp(self):
      self.win = pygame.display.set_mode((800, 600))
      self.dot = Dot(100, 100, self.win)

  def test_move(self):
      initial_x = self.dot.x
      self.dot.update(10)
      final_x = self.dot.x
      self.assertEqual(initial_x - 10, final_x)

  def test_kill(self):
      self.dot.update(-100)
      self.assertFalse(self.dot.alive())



class TestParticle(unittest.TestCase):
  def setUp(self):
      self.win = pygame.display.set_mode((800, 600))
      self.particle = Particle(100, 100, (255, 255, 255), self.win)

  def test_update(self):
      initial_size = self.particle.size
      self.particle.update()
      final_size = self.particle.size
      self.assertEqual(initial_size - 0.1, final_size)

  def test_kill(self):
      self.particle.lifetime = 50
      self.particle.update()
      self.assertFalse(self.particle.alive())


class TestButton(unittest.TestCase):
  def setUp(self):
      self.win = pygame.display.set_mode((800, 600))
      self.button = Button(pygame.Surface((100, 100)), (100, 100), 100, 100)

  def test_draw(self):
      action = self.button.draw(self.win)
      self.assertFalse(action)

  def test_update_image(self):
      self.button.update_image(pygame.Surface((100, 100)))
      self.assertEqual(self.button.image.get_size(), (100, 100))

if __name__ == '__main__':
  unittest.main()
