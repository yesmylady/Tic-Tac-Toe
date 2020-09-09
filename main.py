import sys
import pygame
import pygame.font
from pygame.time import Clock
from pygame.sprite import Sprite 
from pygame.sprite import Group

# 游戏中矩形类
class Board(Sprite):
	def __init__(self, screen, screen_width, screen_height, position_x, position_y):
		super().__init__()
		self.w = screen_width/3
		self.h = screen_height/3
		self.position_x = position_x
		self.position_y = position_y
		self.screen = screen 
		self.rect = pygame.Rect(self.position_x, self.position_y, self.w-10, self.h-10)

		self.draw_circle = False
		self.draw_x = False
		self.touch = False  # 判断是否被点过

		# 每一个方块都有独特的编号， 用于判断输赢 
		self.id = 0

	# 绘制函数
	def draw_board(self):
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		if self.draw_circle == True:	
			pygame.draw.circle(self.screen, (255, 0, 0), 
				(int(self.position_x+60), int(self.position_y+70)), 40, 5)
		elif self.draw_x == True:
			pygame.draw.line(self.screen, (255, 0, 0), (int(self.position_x+25), int(self.position_y+25)), 
				(int(self.position_x+self.w-25), int(self.position_y+self.h-25)), 5)
			pygame.draw.line(self.screen, (255, 0, 0), (int(self.position_x+25), int(self.position_y+self.h-25)), 
				(int(self.position_x+self.w-25), int(self.position_y+25)), 5)
	
	# 下面两个函数用于判断当前状态是叉输入还是圈输入
	def one(self):
		self.draw_circle = True
	def two(self):
		self.draw_x = True

# 主页矩形类
class Main_interface_board(Sprite):
	def __init__(self, screen, message, position_y):
		super().__init__()
		self.screen = screen
		self.message = message # 文字信息
		self.position_x, self.position_y = 50, position_y
		self.width, self.height = 300, 80
		self.text_color = (230, 230, 230)
		self.button_color = (0, 0, 255)
		self.id = 0

		self.rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
		self.font = pygame.font.SysFont("arial", 32)

		# 将文字渲染程图片，并设定其位置
		self.message_image = self.font.render(message, True, self.text_color, self.button_color)
		self.message_image_rect = self.message_image.get_rect()
		self.message_image_rect.center = self.rect.center

		# 游戏结束后显示哪边赢了
		self.xwin = False
		self.owin = False
		self.nowin = False

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.message_image, self.message_image_rect)

def son1(circle_list, cross_list, owin, xwin):
	print("O win!")
	print(circle_list)
	owin.owin = True
	owin.draw_button()
def son2(circle_list, cross_list, owin, xwin):
	print("X win!")
	print(cross_list)
	xwin.xwin = True
	xwin.draw_button()

# 判断输赢函数
def judging(circle_list, cross_list, owin, xwin):
	if len(circle_list) >= 3:
		if 1 in circle_list and 2 in circle_list and 3 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 1 in circle_list and 4 in circle_list and 7 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 1 in circle_list and 5 in circle_list and 9 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 2 in circle_list and 5 in circle_list and 8 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 4 in circle_list and 5 in circle_list and 6 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 7 in circle_list and 8 in circle_list and 9 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 3 in circle_list and 6 in circle_list and 9 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'

		elif 3 in circle_list and 5 in circle_list and 7 in circle_list:
			son1(circle_list, cross_list, owin, xwin)
			return 'o'


	if len(cross_list) >= 3:
		if 1 in cross_list and 2 in cross_list and 3 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'
			
		elif 1 in cross_list and 4 in cross_list and 7 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

		elif 1 in cross_list and 5 in cross_list and 9 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

		elif 2 in cross_list and 5 in cross_list and 8 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

		elif 4 in cross_list and 5 in cross_list and 6 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

		elif 7 in cross_list and 8 in cross_list and 9 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

		elif 3 in cross_list and 6 in cross_list and 9 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

		elif 3 in cross_list and 5 in cross_list and 7 in cross_list:
			son2(circle_list, cross_list, owin, xwin)
			return 'x'

# 初始化游戏配置
def initialize():
	pygame.init()
	screen_width = 400
	screen_height = 450
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Go")

	boards = Group()

	# 创建9个配置好属性的方块对象，
	i = 1
	for y in range(0, 3):
		for x in range(0, 3):
			board = Board(screen, screen_width, screen_height, x * (screen_width/3)+4, y*(screen_height/3)+4)
			board.id = i
			i += 1
			boards.add(board)

	# 配置主页
	bs = Group()
	p_y = 20
	name = ['Man vs. Man', 'Man vs. Computer', 'Computer vs. Man', 'EXIT', 'O win!', 'X win!', 'DRAW']
	for i in range(1, 5):
		main_interface_board = Main_interface_board(screen, name[i-1], p_y)
		main_interface_board.id = i
		bs.add(main_interface_board)
		p_y += 100

	owin = Main_interface_board(screen, name[4], 0)
	xwin = Main_interface_board(screen, name[5], 0)
	nowin = Main_interface_board(screen, name[6], 0)
	# 返回主函数有需要的变量
	return screen, boards, bs, owin, xwin, nowin


# 人机自走，返回一个最佳位置
def artificial_intelligence(circle_list, cross_list, boards):
	total_list = [i for i in range(1, 10)]
	all_routes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
	valuation = 0
	valuations = {1:0, 2:0, 3:0, 
				  4:0, 5:0, 6:0, 
				  7:0, 8:0, 9:0, }

	checkboard = {1:0, 2:0, 3:0, 
				  4:0, 5:0, 6:0, 
			 	  7:0, 8:0, 9:0, }

	# 用字典描述此棋盘，1代表圈，-1代表叉，0代表还未赋值
	for board in boards:
		if board.draw_circle:
			checkboard[board.id] = 1
		elif board.draw_x:
			checkboard[board.id] = -1
		else:
			pass

	# 将已经有棋子的棋盘的估价设为-10
	for board in boards:
		if board.draw_circle or board.draw_x:
			valuations[board.id] = -1000
	
	# 未赋值的位置id
	remained_boards = []
	for k, v in checkboard.items():
		if v == 0:
			remained_boards.append(k)
	print(remained_boards)

	temp = []

	for para in remained_boards:
		for route in all_routes:
			if para in route:
				for r in route:
					if r != para:
						temp.append(checkboard[r])
				# 对应ai.txt估价函数的5种情况
				if temp[0] == 0 and temp[1] == 0:
					valuations[para] += 1
				elif 0 in temp and 1 in temp:
					valuations[para] += 10
				elif temp[0] == 1 and temp[1] == 1:
					valuations[para] += 800
				elif temp[0] == -1 and temp[1] == -1:
					valuations[para] += 1000
				elif 0 in temp and -1 in temp:
					valuations[para] += 30
				elif 1 in temp and -1 in temp:
					valuations[para] += -10
				else:
					assert("Wrong! no 5 situation matched")
				temp = []
	print(valuations)
	for k, v in valuations.items():
		temp.append(v)
	for k in valuations.keys():
		if valuations[k] == max(temp):
			return k


def run_game():
	
	screen, boards, bs, owin, xwin, nowin = initialize()
	# 用于判断当前输入是叉或是圈的参数
	temp = 0
	# 两个列表分别存储圆圈和叉的位置
	circle_list = []
	cross_list = []

	# 用于判断游戏应该进行哪个模式
	game_begin = False
	mode_one = False
	mode_two = False
	mouse_access = True
	ai_first_step = True 
	# 开始游戏循环
	while True:
		# 控制帧率
		clock = Clock()
		time_passed = clock.tick(10)

		# 主页
		if not game_begin:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_x, mouse_y = pygame.mouse.get_pos()
					for b in bs:
						if b.rect.collidepoint(mouse_x, mouse_y) and b.id == 1:
							game_begin = True
						elif b.rect.collidepoint(mouse_x, mouse_y) and b.id == 2:
							mode_one = True
							game_begin = True
						elif b.rect.collidepoint(mouse_x, mouse_y) and b.id == 3:
							mode_two = True
							game_begin = True
						elif b.rect.collidepoint(mouse_x, mouse_y) and b.id == 4:
							sys.exit()
			for b in bs:
				b.draw_button()
				pygame.display.flip()
			continue


		# 机人对战模式电脑先走的那一步
		if mode_two:
			if ai_first_step:
				ar = artificial_intelligence(circle_list, cross_list, boards)
				for b2 in boards:
					if b2.id == ar:
						b2.two()
						cross_list.append(b2.id)
						b2.touch = True
						ai_first_step = False
						break
		# 获取用户操作
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# esc返回主页
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					game_begin = False
					circle_list = []
					cross_list = []
					mouse_access = True
					temp = 0
					mode_one = False
					mode_two = False
					ai_first_step = True

					for b in boards:
						b.draw_circle = False
						b.draw_x = False
						b.touch = False
					owin.owin = False
					xwin.xwin = False
					nowin.nowin = False

			# 监听鼠标事件
			elif event.type == pygame.MOUSEBUTTONDOWN and mouse_access == True:
				mouse_x, mouse_y = pygame.mouse.get_pos() # 获取点击位置坐标
				
				# 玩家对战模式
				if not mode_one and not mode_two:
					for b in boards:
						if b.rect.collidepoint(mouse_x, mouse_y) and not b.touch:
							if not temp:
								b.one() # 在指定方块上画圆圈
								b.touch = True
								circle_list.append(b.id)
								temp = 1
							else:
								b.two() # 在指定方块上画叉
								b.touch = True
								cross_list.append(b.id)
								temp = 0

					# 判断输赢
						if_win = judging(circle_list, cross_list, owin, xwin)
						if if_win == 'x' or if_win == 'o':
							mouse_access = False
						else:
							mouse_access = True

						if len(circle_list) + len(cross_list) == 9 and not owin.owin and not xwin.xwin:
							print("平局")
							nowin.nowin = True
							mouse_access = False
				
				# 人机对战模式
				elif mode_one or mode_two:
					for b in boards:
						if b.rect.collidepoint(mouse_x, mouse_y) and not b.touch:
							b.one()
							circle_list.append(b.id)
							b.touch = True

							# 电脑自走
							ar = artificial_intelligence(circle_list, cross_list, boards)
							for b1 in boards:
								if b1.id == ar and not b1.touch:
									print(b1.id)
									b1.two()
									cross_list.append(b1.id)
									b1.touch = True
									break
					# 判断输赢
						if_win = judging(circle_list, cross_list, owin, xwin)
						if if_win == 'x' or if_win == 'o':
							mouse_access = False
						else:
							mouse_access = True
						if len(circle_list) + len(cross_list) == 9 and not owin.owin and not xwin.xwin:
							print("平局")
							nowin.nowin = True
							mouse_access = False

							
						# 判断输赢
						if_win = judging(circle_list, cross_list, owin, xwin)
						if if_win == 'x' or if_win == 'o':
							mouse_access = False
						else:
							mouse_access = True
						if len(circle_list) + len(cross_list) == 9 and not owin.owin and not xwin.xwin:
							print("平局")
							nowin.nowin = True
							mouse_access = False

		screen.fill((230, 230, 230)) # 填充屏幕底层颜色

		if game_begin:
			for b in boards.sprites(): # 绘制更新后的方块
				b.draw_board()

		if owin.owin:
			owin.draw_button()
		elif xwin.xwin:
			xwin.draw_button()
		elif nowin.nowin:
			nowin.draw_button()

		pygame.display.flip() # 刷新

run_game()
