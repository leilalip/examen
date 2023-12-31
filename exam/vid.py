import pygame, random

from starwars import en_partida, num_nivel

#ventana
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def colision(x1, y1, a1, b1, x2, y2, a2, b2, ex=0):
    if x1 + a1 > x2 + ex and \
            x1 + ex < x2 + a2 and \
            y1 + b1 > y2 + ex and \
            y1 + ex < y2 + b2:
        return True
    else:
        return False

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("asteroide1c.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1

		if self.rect.y > SCREEN_HEIGHT:
			self.rect.y = -10
			self.rect.x = random.randrange(SCREEN_WIDTH)


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("asteroide1g.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		self.rect.x = mouse_pos[0]
		self.rect.y = mouse_pos[1]


while en_partida:
    en_final = False

    num_aste_grandes = num_nivel * 5
    num_aste_pequenios = num_nivel * 10



class Game(object):
	def __init__(self):
		self.game_over = False

		self.score = 0

		self.meteor_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()


		for i in range(30):
			meteor = Meteor()
			meteor.rect.x = random.randrange(SCREEN_WIDTH)
			meteor.rect.y = random.randrange(SCREEN_HEIGHT)

			self.meteor_list.add(meteor)
			self.all_sprites_list.add(meteor)

		self.player = Player()
		self.all_sprites_list.add(self.player)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()

		return False

	def run_logic(self):

		if not self.game_over:
			self.all_sprites_list.update()

			meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

			for meteor in meteor_hit_list:
				self.score += 1
				print(self.score)

			if len(self.meteor_list) == 0:
				self.game_over = True

	def display_frame(self, screen):
		screen.fill(WHITE)

		if self.game_over:
			font = pygame.font.SysFont("Serif", 25) # Fuente
			text = font.render("Has pasado al segundo nivel. Da click para continuar", True, BLACK) # Texto
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) # posicion text
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.blit(text, [center_x, center_y]) # ponerlo en pantalla

		if not self.game_over:
			self.all_sprites_list.draw(screen)
























		pygame.display.flip()

def main():
	pygame.init()

	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

	done = False
	clock = pygame.time.Clock()

	game = Game()

	while not done:
		done = game.process_events()
		game.run_logic()
		game.display_frame(screen)
		clock.tick(60)
	pygame.quit()


if __name__ == "__main__":
	main()