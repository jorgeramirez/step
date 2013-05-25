#!/usr/bin/env python

import pygame
from board import Board
from multiprocessing import Queue

class GuiBoard(Board):
    def __init__(self, size=10):
        Board.__init__(self, size)
        
    def draw(self, q):
        """ Draw a chess board with queens, as determined by the the_board. """
        pygame.init()
        colors = [(255,250,250), (0,0,0), (255,255,0)]    # set up colors [white, black,yellow]

        surfaceSz = 640          # Proposed physical surface size.
        sq_sz = surfaceSz // self._size    # sq_sz is length of a square.
        surfaceSz = self._size * sq_sz     # Adjust to exact multiple of sq_sz

        # Create the surface of (width, height), and its window.
        pygame.display.set_caption("Simulador")    
        surface = pygame.display.set_mode((surfaceSz, surfaceSz))


        ball = pygame.image.load("tux.bmp")
        if ball.get_width() > sq_sz:
	    	ball = pygame.transform.scale(ball, (sq_sz - 10, sq_sz - 10)) 

        # Use an extra offset to centre the ball in its square.
        # If the square is too small, offset becomes negative,
        # but it will still be centered :-)
        ball_offset = (sq_sz-ball.get_rect()[2]) // 2
        
        while True:

            # look for an event from keyboard, mouse, etc.
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break;
                
            
            if not q.empty():
                e = q.get()
                self.move(e["command"])
          
            # Draw a fresh background (a blank chess board)
            for row in range(self._size):         # Draw each row of the board.
                c_indx = row % 2           # Alternate starting color
                for col in range(self._size):       # Run through cols drawing squares
                    the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                    surface.fill(colors[c_indx], the_square)
                    # now flip the color index for the next square
                    c_indx = (c_indx + 1) % 2
            
            pygame.time.delay(50)
        
            # Now that squares are drawn, draw the queens.
            surface.blit(ball,
                (self._posc*sq_sz+ball_offset,self._posr*sq_sz+ball_offset))

            pygame.display.flip()
  
            pygame.time.delay(50)
            
    pygame.quit()

