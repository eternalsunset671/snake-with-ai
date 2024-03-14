import pygame
import random

class Game:
    pygame.init()
    __white = (255, 255, 255)
    __yellow = (255, 255, 102)
    __black = (0, 0, 0)
    __red = (213, 50, 80)

    __green = (40, 255, 40)
    __dark_green = (34,139,34)
    __blue = (50, 153, 213)
    __width = 800
    __height = 600
    __FPS = 30

    __dis = pygame.display.set_mode((__width, __height))
    pygame.display.set_caption('Snake')
    __clock = pygame.time.Clock()
    __snake_size = 30
    __snake_speed = 8
    __apple_size = 20

    font_style = pygame.font.SysFont("arial", 25)
    
    def __init__(self):
       game_over = False
       game_close = False
       x1 = self.__width // 2
       y1 = self.__height // 2
       x1_delta = 0
       y1_delta = 0
       snake_List = []
       Length_of_snake = 1
       applex = round(random.randrange(0, self.__width - self.__snake_size) // 10.0) * 10.0
       appley = round(random.randrange(0, self.__height - self.__snake_size) // 10.0) * 10.0
       vertical_block = True
       horizontal_block = True
       mode = None
       while not game_over:
           while game_close == True:
               self.__dis.fill(self.__black)
               self.__show_message("You lose! Press SPACE for new game.", self.__white)
               self.__show_score(Length_of_snake - 1)
               pygame.display.update()
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_SPACE:
                           pass
                           Game()#fix for ai

       
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   game_over = True
               if event.type == pygame.KEYUP:
                   if horizontal_block and event.key == pygame.K_LEFT:
                       horizontal_block = False
                       vertical_block = True
                       x1_delta = -self.__snake_speed
                       y1_delta = 0
                       mode = True
                   elif horizontal_block and event.key == pygame.K_RIGHT:
                       horizontal_block = False
                       vertical_block = True
                       x1_delta = self.__snake_speed
                       y1_delta = 0
                       mode = True
                   elif vertical_block and event.key == pygame.K_UP:
                       horizontal_block = True
                       vertical_block = False
                       y1_delta = -self.__snake_speed
                       x1_delta = 0
                       mode = False
                   elif vertical_block and event.key == pygame.K_DOWN:
                       horizontal_block = True
                       vertical_block = False
                       y1_delta = self.__snake_speed
                       x1_delta = 0
                       mode = False
               elif event.type == pygame.KEYDOWN:
                    if horizontal_block and event.key == pygame.K_LEFT:
                        horizontal_block = False
                        vertical_block = True
                        x1_delta = -self.__snake_speed * 2
                        y1_delta = 0
                    elif horizontal_block and event.key == pygame.K_RIGHT:
                        horizontal_block = False
                        vertical_block = True
                        x1_delta = self.__snake_speed * 2
                        y1_delta = 0
                    elif vertical_block and event.key == pygame.K_UP:
                        horizontal_block = True
                        vertical_block = False
                        y1_delta = -self.__snake_speed * 2
                        x1_delta = 0
                    elif vertical_block and event.key == pygame.K_DOWN:
                        horizontal_block = True
                        vertical_block = False
                        y1_delta = self.__snake_speed * 2
                        x1_delta = 0


           if x1 >= self.__width or x1 < 0 or y1 >= self.__height or y1 < 0:
               game_close = True

           x1 += x1_delta
           y1 += y1_delta
           self.__dis.fill(self.__black)
           pygame.draw.rect(self.__dis, self.__red, [applex, appley, self.__apple_size, self.__apple_size])
           snake_Head = []
           snake_Head.append(x1 + 4)
           snake_Head.append(y1 + 4)
           snake_List.append(snake_Head)
           if len(snake_List) > Length_of_snake:
               del snake_List[0]
           for x in snake_List[:-1]:
               if x == snake_Head:
                   game_close = True
           self.__show_snake(snake_List, mode)
           self.__show_score(Length_of_snake - 1)
           pygame.display.update()
           if applex + self.__apple_size > x1 and \
               applex < x1 + self.__snake_size and \
               appley + self.__apple_size >  y1 and \
               appley < y1 + self.__snake_size:

               applex = round(random.randrange(0, self.__width - self.__snake_size) / 10.0) * 10.0
               appley = round(random.randrange(0, self.__height - self.__snake_size) / 10.0) * 10.0
               Length_of_snake += 1
           self.__clock.tick(self.__FPS)

       pygame.quit()
       quit()


    def __show_score(self, score):
       score_font = pygame.font.SysFont('arial', 35)
       value = score_font.render(f'score: {score}', True, self.__yellow)
       self.__dis.blit(value, [0, 0])
 
    def __show_snake(self, snake_list, mode):
       if mode:
           for i in range(0, len(snake_list)-1):
               pygame.draw.rect(self.__dis, self.__dark_green, [snake_list[i][0], snake_list[i][1], self.__snake_size, self.__snake_size])
           pygame.draw.rect(self.__dis, self.__green, [snake_list[-1][0], snake_list[-1][1], self.__snake_size, self.__snake_size])
       else:
           for i in range(len(snake_list)-2, -1, -1):
               pygame.draw.rect(self.__dis, self.__dark_green, [snake_list[i][0], snake_list[i][1], self.__snake_size, self.__snake_size])
           pygame.draw.rect(self.__dis, self.__green, [snake_list[-1][0], snake_list[-1][1], self.__snake_size, self.__snake_size])

    def __show_message(self, msg, color):
       mesg = self.font_style.render(msg, True, color)
       self.__dis.blit(mesg, [self.__width / 2, self.__height / 2])

if __name__ == '__main__':
    Game()
