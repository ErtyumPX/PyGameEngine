from pygame import Surface

class RenderManager:
	def __init__(self, surface: Surface = None, background_color: tuple = None):
		self.surface = surface
		self.background_color = background_color
		self.objects = {}

	def register(self, object_to_register, layer = 0):
		if layer in self.objects.keys():
			self.objects[layer].append(object_to_register)
		else:
			self.objects[layer] = [object_to_register,]
			self.objects = dict(sorted(self.objects.items()))

	def register_all(self, list_to_register: list, layer = 0):
		if layer in self.objects.keys():
			self.objects[layer].extend(list_to_register)
		else:
			self.objects[layer] = list_to_register
			self.objects = dict(sorted(self.objects.items()))

	def remove(self, object_to_remove):
		for layer in self.objects.values():
			for obj_ in layer:
				if object_to_remove == obj_:
					layer.remove(object_to_remove)
					if len(layer) == 0:
						self.objects.pop(layer)

	def remove_all(self, list_to_remove: list):		
		for obj in list_to_remove:
			for layer in self.objects.values():
				for obj_ in layer:
					if obj == obj_:
						layer.remove(obj)
						if len(layer) == 0:
							self.objects.pop(layer)

	def clear(self):
		self.objects = []

	def render(self):
		if self.surface is not None and self.background_color is not None:
			self.surface.fill(self.background_color)
		for layer in self.objects.values():
			for obj in layer:
				obj.render()
