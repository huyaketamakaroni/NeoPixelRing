#! /usr/bin/env python3

import board
from NPRController import NPRController
import time

controller = NPRController(board.D18, 0.03)
controller.stop()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#上
controller.clear()
controller.set(NPRController.LT, red)
controller.set(NPRController.RT, red)
controller.show()
time.sleep(1.0)
#左
controller.clear()
controller.set(NPRController.LL, red)
controller.set(NPRController.RL, red)
controller.show()
time.sleep(1.0)
#下
controller.clear()
controller.set(NPRController.LB, red)
controller.set(NPRController.RB, red)
controller.show()
time.sleep(1.0)
#右
controller.clear()
controller.set(NPRController.LR, red)
controller.set(NPRController.RR, red)
controller.show()
time.sleep(1.0)
#右上
controller.clear()
controller.set(NPRController.RTL, red)
controller.set(NPRController.LTL, red)
controller.show()
time.sleep(1.0)
#右下
controller.clear()
controller.set(NPRController.RBL, red)
controller.set(NPRController.LBL, red)
controller.show()
time.sleep(1.0)
#左下
controller.clear()
controller.set(NPRController.RBR, red)
controller.set(NPRController.LBR, red)
controller.show()
time.sleep(1.0)
#左上
controller.clear()
controller.set(NPRController.RTR, red)
controller.set(NPRController.LTR, red)
controller.show()
time.sleep(1.0)
#後方に位置する対象物への視線誘導（右方向）
controller.clear()
controller.set(NPRController.TURR,green)
controller.set(NPRController.TURL,green)
controller.show()
time.sleep(1.0)
#後方に位置する対象物への視線誘導（左方向）
controller.clear()
controller.set(NPRController.TULR,green)
controller.set(NPRController.TULL,green)
controller.show()
time.sleep(1.0)


controller.stop()

