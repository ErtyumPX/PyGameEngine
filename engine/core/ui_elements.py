# TODO: InputBox should be refactored 
# TODO: For all elements that are rendering more than 1 element, the sub/child elements should be rendered
# on the parent surface but not the root surface, and parent and child surfaces should be updated only when
# a factor that effects the render output changes inside the child or parent element
# TODO: More elements should be added -> CheckBox, ToggleButton, Slider, Image etc
# TODO: All interactables - button, checkbox, toggle button etc - should be inherited from the InteractableElement class
# TODO: InputBox with multiline support 
	# Main issues are: Cursor position, adding new lines and going to the next line when the word is too long
# TODO: Hotkeys could be added and bound to interactable elements

import pygame
from pygame.rect import Rect
from enum import Enum
import re

EMPTY_FUNCTION = lambda: 0
DEFAULT_FONT_PATH = 'data/SpaceMono-Regular.ttf'

"""
class InterfaceElement:
	def __init__(self, status):
		self.image = None
		self.x = 0
		self.y = 0
		self.status = InterfaceStatus.VISIBLE

	def change_status(self, new_status):
		if -1 < new_status < 3:
			self.status = new_status
		else:
			raise Exception("Improper status")
"""	
class InterfaceStatus(Enum):
	VISIBLE = 0
	VISIBLE_UNINTERACTABLE = 1
	INVISIBLE = 2

class Alignment(Enum):
	LEFT_TOP = 0
	TOP = 1
	RIGHT_TOP = 2
	LEFT = 3
	CENTER = 4
	RIGHT = 5
	LEFT_BOTTOM = 6
	BOTTOM = 7
	RIGHT_BOTTOM = 8

class InterfaceElement:
	def __init__(self, root_surface:pygame.Surface, 
			  	status:InterfaceStatus = InterfaceStatus.VISIBLE, 
			  	x:int = 0, y:int = 0, width:int = 0, height:int = 0, 
				alignment:Alignment = Alignment.LEFT_TOP):
		self.root_surface:pygame.Surface = root_surface
		self.rect:Rect = Rect(x, y, width, height)
		self.status:InterfaceStatus = status
		self._alignment:Alignment = alignment
		AlignRect(self)
	
	def change_status(self, new_status):
		assert new_status in InterfaceStatus
		self.status = new_status

	@property
	def alignment(self):
		return self._alignment

	@alignment.setter
	def alignment(self, new_alignment):
		self._alignment = new_alignment
		AlignRect(self)
	
	def move_to(self, x, y):
		self.rect.x = x
		self.rect.y = y
		AlignRect(self)

	def render(self):
		pass

def AlignRect(element:InterfaceElement) -> None:
	"""
	Alignes the Rect of the element according to the alignment with the current x and y of the rect
	"""
	if element.alignment == Alignment.LEFT_TOP:
		element.rect.left = element.rect.x
		element.rect.top = element.rect.y
	elif element.alignment == Alignment.TOP:
		element.rect.centerx = element.rect.x
		element.rect.top = element.rect.y
	elif element.alignment == Alignment.RIGHT_TOP:
		element.rect.right = element.rect.x
		element.rect.top = element.rect.y
	elif element.alignment == Alignment.LEFT:
		element.rect.left = element.rect.x
		element.rect.centery = element.rect.y
	elif element.alignment == Alignment.CENTER:
		element.rect.centerx = element.rect.x
		element.rect.centery = element.rect.y
	elif element.alignment == Alignment.RIGHT:
		element.rect.right = element.rect.x
		element.rect.centery = element.rect.y
	elif element.alignment == Alignment.LEFT_BOTTOM:
		element.rect.left = element.rect.x
		element.rect.bottom = element.rect.y
	elif element.alignment == Alignment.BOTTOM:
		element.rect.centerx = element.rect.x
		element.rect.bottom = element.rect.y
	elif element.alignment == Alignment.RIGHT_BOTTOM:
		element.rect.right = element.rect.x
		element.rect.bottom = element.rect.y

def ElementCollide(element:InterfaceElement, mouse_position) -> bool:
	"""
	Checks if the mouse is colliding with the button
	"""
	return element.rect.collidepoint(mouse_position)

"""
class ImageButton(pygame.sprite.Sprite, InterfaceElement):
	def __init__(self, surface, image, x, y, image_percentage=100, func=empty_function, args=(), kwargs={}, upper_surface=(0,0), selected_change=(0,0), highlight_color = None, highlight_offset = (0, 0), status=0):
		pygame.sprite.Sprite.__init__(self)
		InterfaceElement.__init__(self, status)
		self.surface = surface
		fraction = image_percentage/100
		self.image = pygame.transform.scale(image, (int(image.get_width()*fraction), int(image.get_height()*fraction)))
		self.x = x
		self.y = y
		self.upper_surface = upper_surface
		self.selected_change = selected_change
		self.selected = False
		self.clicked = False

		self.func = func
		self.args = args
		self.kwargs = kwargs

		self.highlight_color = highlight_color
		self.highlight_offset = highlight_offset
		if highlight_color:
			image_size = image.get_size()
			self.effect = pygame.Surface((image_size[0]+highlight_offset[0], image_size[1]+highlight_offset[1]), pygame.SRCALPHA)
			self.effect.fill(highlight_color)

	def update(self):
		if self.status != 2:
			if self.selected:
				self.surface.blit(self.image, (self.x+self.selected_change[0], self.y+self.selected_change[1]))
				if self.highlight_color: self.surface.blit(self.effect, (self.x+self.selected_change[0]-self.highlight_offset[0]/2, self.y+self.selected_change[1]-self.highlight_offset[1]/2))
			else:
				self.surface.blit(self.image, (self.x, self.y))
"""

class Text(InterfaceElement):
	def __init__(self, root_surface, x:int = 0, y:int = 0,  
			  	text:str = "New Text", font_size:int = 11, color:tuple = (0,0,0), 
				alignment:Alignment = Alignment.LEFT_TOP,
				status:int = InterfaceStatus.VISIBLE):
		self.surface = None
		self.text:str = text
		self.color:tuple = color
		self.font_size = font_size
		self.font:pygame.font.Font = pygame.font.Font(DEFAULT_FONT_PATH, font_size)
		self.surface:pygame.Surface = self.font.render(self.text, True, color)
		InterfaceElement.__init__(self, root_surface, status, x, y, 
								self.surface.get_width(), 
								self.surface.get_height(), alignment)

	def change_text_to(self, new_text:str, font_size:int = None):
		if font_size is int and font_size > 0 and self.font_size != font_size:
			self.font_size = font_size
			self.font = pygame.font.Font(DEFAULT_FONT_PATH, font_size)
		self.text = new_text
		self.surface = self.font.render(self.text, True, self.color)

	def change_color_to(self, new_color:tuple):
		assert new_color[0] is int and new_color[1] is int and new_color[2] is int
		self.color = new_color
		self.surface = self.font.render(self.text, True, new_color)

	def render(self):
		if self.status == InterfaceStatus.INVISIBLE: return
		self.root_surface.blit(self.surface, (self.rect.x, self.rect.y))
"""
self, root_surface, x:int = 0, y:int = 0, 
alignment:Alignment = Alignment.LEFT_TOP, 
text:str = "New Text", font_size:int = 11, color:tuple = (0,0,0), 
status:int = InterfaceStatus.VISIBLE
"""

class InteractablePhase(Enum):
	DEFAULT = 0
	HOVER = 1
	PRESSED = 2

#class InteractableElement(InterfaceElement):
#	pass

class Button(InterfaceElement):
	def __init__(self, root_surface, x:int = 0, y:int = 0, width:int = 100, height:int = 25, 
			  	func=EMPTY_FUNCTION, args:tuple=(), kwargs:dict={}, 
				text="Button", font_size=11,
				background:tuple = (190,190,190), foreground:tuple = (0,0,0),
				border_color:tuple = (0,0,0), border_width:int = 4,
				status:InterfaceStatus = InterfaceStatus.VISIBLE,
				alignment:Alignment = Alignment.LEFT_TOP,
				hovering_color:tuple = (0,0,0,50), pressed_color:tuple = (0,0,0,150)):
		self.surface = pygame.Surface((width, height))
		self.surface.fill(background)
		pygame.draw.rect(self.surface, border_color, (0, 0, width, height), border_width)

		self.phase:InteractablePhase = InteractablePhase.DEFAULT
		self.effect_surface:pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
		self.hovering_color = hovering_color
		self.pressed_color = pressed_color

		self.func:function = func
		self.args:tuple = args
		self.kwargs:dict = kwargs

		InterfaceElement.__init__(self, root_surface, status, x, y, 
								width, height, alignment)
		self.text:Text = Text(root_surface, self.rect.centerx, self.rect.centery, text, 
							font_size, foreground, Alignment.CENTER)

	def press(self):
		self.func(*self.args, **self.kwargs)

	def render(self):
		if self.status == InterfaceStatus.INVISIBLE: return

		self.root_surface.blit(self.surface, (self.rect.x, self.rect.y))
		self.text.render()

		if self.phase == InteractablePhase.DEFAULT: return
		if self.phase == InteractablePhase.HOVER:
			self.effect_surface.fill(self.hovering_color)
		elif self.phase == InteractablePhase.PRESSED:
			self.effect_surface.fill(self.pressed_color)
		self.root_surface.blit(self.effect_surface, (self.rect.x, self.rect.y))

"""
valid = r'[^\.A-Za-z0-9 _]'
class InputBox(pygame.sprite.Sprite, InterfaceElement):
	def __init__(self, surface, x:int = 0, y:int = 0, width:int = 50, height:int = 20, font_size = 50, color=(0, 0, 0), default_text='', image=BLANK_WHITE_IMAGE, status:int = 0):
		pygame.sprite.Sprite.__init__(self)
		InterfaceElement.__init__(self, status)
		self.surface = surface
		self.image = pygame.transform.scale(image, (width, height))
		self.x, self.y, self.width, self.height = x, y, width, height
		self.selected = False

		self.text = ''
		self.default_text = default_text
		self.color = color
		self.font_size = min(height-10, font_size)
		self.font = pygame.font.Font(DEFAULT_FONT_PATH, self.font_size)
		self.text_box = self.font.render(self.text, True, color)

	def add(self, char):
		if not re.search(valid, char) and self.image.get_width() - self.text_box.get_width() > 15 + self.font_size/2:
			self.text += char

	def remove(self):
		self.text = self.text[:-1]

	def clear(self):
		self.text = ''

	def render(self):
		self.surface.blit(self.image, (self.x, self.y))
		if self.text == '':
			self.text_box = self.font.render(self.default_text, True, (140,140,140))
		else:
			self.text_box = self.font.render(self.text, True, self.color)
		self.surface.blit(self.text_box, (self.x + 7.5, self.y + 4))
"""

def ProcessElements(events, pressed_keys, mouse_pos, elements:list = [], inputs:list = [], texts:list = []):
	for element_ in elements:
		if ElementCollide(element_, mouse_pos):
			if element_.phase != InteractablePhase.PRESSED:
				element_.phase = InteractablePhase.HOVER
		else:
			element_.phase = InteractablePhase.DEFAULT
	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN:
			for element_ in elements:
				if element_.phase == InteractablePhase.HOVER and element_.status == InterfaceStatus.VISIBLE:
					element_.phase = InteractablePhase.PRESSED

		elif event.type == pygame.MOUSEBUTTONUP:
			for element_ in elements:
				if element_.phase == InteractablePhase.PRESSED and element_.status == InterfaceStatus.VISIBLE:
					print("PRESSED!")
					element_.press()
					element_.phase = InteractablePhase.HOVER
"""
			for input_box in inputs:
				if ElementCollide(input_box, mouse_pos):
					input_box.selected = True
				else: 
					input_box.selected = False

		elif event.type == pygame.KEYDOWN:
			for input_box in inputs:
				if input_box.selected:
					if event.key == pygame.K_BACKSPACE:
						if pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT] or pressed_keys[pygame.K_LCTRL] or pressed_keys[pygame.K_RCTRL]:
							input_box.clear()
						else: 
							input_box.remove()
					else: 
						input_box.add(event.unicode)
"""


def RenderElements(elements:list = [], inputs:list = [], texts:list = []):
	for element_ in elements:
		element_.render()
	for input_ in inputs:
		input_.render()
	for text_ in texts:
		text_.render()
