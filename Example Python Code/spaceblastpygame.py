#basic python game


from random import random
from math import cos, sin, radians

#Define your global constants (that you don't want to change) here
WIDTH=500
HEIGHT=500
DARK_BLUE = (50, 50, 100) #Colors can be defined as (R, G, B) tuples
ALIEN_SPEED = 4

#Define global variables that maintain the state of the game here
score = 0
ship = Actor('ship', (WIDTH/2, HEIGHT/2))
alien = Actor('alien', (0,HEIGHT))

ship.speed = 8
ship.bullets = []

alien_bounce = False 
alien_heading = random() * 360 - 180

#TOP LEVEL PROCEDURES:
#  draw and update should contain primarily function and procedure 
#    calls that you create.
#  REMEMBER:  Pygame Zero handles the main game loop for you.  Every 
#             time a new frame is drawn, update will be called and then 
#             draw will be called.  

#Run space_blast.py by typing the following in Konsole
#     pgrzun space_blast.py

#Procedure: draw
#Pygame zero objects are used to represent items to be displayed 
#  to the screen 
#None->None
def draw():
    """Draws items on the screen.
    """
    screen.fill(DARK_BLUE)
    ship.draw()
    alien.draw()
    for bullet in ship.bullets:
    	screen.draw.circle((bullet[0],10,(200, 100, 0)))


    
#Procedure: update
#Pygame zero objects and Python objects represent the state of the 
#   game
#None->None
def update():
	move_alien()
	move_ship()
	move_bullets()
	"""Updates various objects to maintain the current state of the game. """
    
    
def move_bullets():
	updated_bullets = []
	for bullet in ship.bullets:
		new_pos = calculate_move(bullet[0], bullet[1], ship.speed)
		updated_bullets.append((new_pos, bullet[1]))
	ship.bullets = updated_bullets
    
    

def move_ship(key):
	if keyboard.up or keyboard.w:
		ship.y -= ship.speed
	elif keyboard.down or keyboard.s:
		ship.y += ship.speed
	
	if keyboard.left or keyboard.a:
		ship.x -= ship.speed
	elif keyboard.right or keyboard.d:
		ship.x += ship.speed
		
	ship.pos = bounds_check(ship.pos)

    
def bounds_check(pos):
	x = max(0, min(pos[0], WIDTH))
	y = max(0, min(pos[1], HEIGHT))	
	return (x,y)
	
	
	
def on_mouse_move(pos):
	ship.angle = ship.angle_to(pos)
	
	
	
def on_mouse_down(pos,button):
	if button == mouse.LEFT:
		ship.bullets.append(ship.pos, ship.angle)



def move_alien():
    global alien_heading
    
    alien_heading += random() * 40 - 20
    
    alien.pos = calculate_move(alien.pos, alien_heading, ALIEN_SPEED)
    
    alien.pos = bounds_check(alien.pos)
    
    	
    #spin and move	
    alien.angle += random() * 2 - 1

def calculate_move(pos, angle, speed):
	x = pos[0] + cos(radians(angle)) * speed
	y = pos[1] + sin(radians(-angle)) * speed
	
	return (x, y)
