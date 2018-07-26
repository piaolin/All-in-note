#coding = 'utf-8'
class Person(object):
	def __init__(self, name):
		self.name = name
		self.gun = None
		self.blood = 100
	def shot(self, clip, ak47_bullet, number):
		clip.zb(ak47_bullet, number)
	def loading(self, gun, clip):
		gun.zdj(clip)
	def hold(self, gun):
		self.gun = gun
	def shoot(self, target):
		self.gun.fire(target)
	def __str__(self):
		if self.gun != None:
			return '%s的生命值为%d, 武器为%s'%(self.name, self.blood, self.gun)
		else:
			return '%s的生命值为%d, 没有武器'%(self.name, self.blood)
        
class Gun(object):
	def __init__(self, type):
		self.type = type
		self.clip = None
	def zdj(self, new_clip):
		self.clip = new_clip
	def fire(self, target):
		self.clip.come(target)
	def __str__(self):
		if self.clip != None:
			return "%s 已上膛:%s"%(self.type, self.clip)
		else:
			return "%s 未上膛"%self.type

class Clip(object):
	def __init__(self, type, max_number):
		self.type = type
		self.max_number = max_number
	def zb(self, bullet, number):
		self.bullet = bullet
		if number >= 30:
			self.number = 30
		else:
			self.number = number
	def come(self, target):
		if self.number > 0:
			self.number -= 1
			self.bullet.hit(target)
		else:
			print("没有子弹")
	def __str__(self):
		return "%d/%d"%(self.number, self.max_number)
		
class Bullet(object):
	def __init__(self, caliber):
		self.caliber = caliber
	def hit(self, target):
		if self.caliber == 7.62:
			print("成功命中")
			target.blood -= 50
		else:
			target.blood -= 10

class Enemy(object):
	def __init__(self, name):
		self.name = name
		self.blood = 100
	def __str__(self):
		if self.blood >= 0:
			return '%s的血量为%d'%(self.name, self.blood)
		else:
			return '%s已被你击败'%self.name
	
def main():
	piaolin = Person("piaolin")
	ak47 = Gun("ak47")
	ak47_clip = Clip("ak47", 30)
	ak47_bullet = Bullet(7.62)
	piaolin.shot(ak47_clip, ak47_bullet, 3)
	piaolin.loading(ak47, ak47_clip)
	piaolin.hold(ak47)
	print(piaolin)
	boss = Enemy('boss')
	print(boss)
	piaolin.shoot(boss)
	print(boss)
	piaolin.shoot(boss)
	print(boss)
	piaolin.shoot(boss)
	print(boss)
	print(piaolin)

if __name__ == '__main__':
	main()