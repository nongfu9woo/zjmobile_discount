# _*_ coding:utf-8 _*_ 
# @Time : 14:01 2023/5/16
# Author : Abner
# @File : test.py
# @Software : PyCharm

import pyautogui
from base64 import b64decode
from io import BytesIO
from PIL import Image
from gui_head import IMAGE_GUI
from runAsAdmin import RunAsAdmin


class Automouse:
    def __init__(self):

        self.MAX_CARTS = None
        self.MAX_LIKES = None
        pyautogui.PAUSE = 1
        self.run()

    # 点赞视频：点赞次数，未点赞(白色)，已点赞(红色)
    def check_video(self, anchor_x, anchor_y):
        # 用颜色判断是否进入视频界面(减少图片占用空间)
        if pyautogui.screenshot().getpixel((anchor_x + 367, anchor_y + 580))[1] < 230:
            print('继续等待>>>')
            return False
        else:
            return True

    def like_video(self, anchor_x, anchor_y):
        # 判断”点赞“颜色，如白则点，如红则双击
        rgb = pyautogui.screenshot().getpixel((anchor_x + 377, anchor_y + 625))
        pyautogui.moveTo(anchor_x + 377, anchor_y + 625)
        if rgb[0] <= 240:
            print('未点赞')
            pyautogui.click(button='left')
        else:
            print('已经点赞')
            pyautogui.click(button='left')
            pyautogui.click(button='left')

    # 浏览购物车：浏览次数，进入/未进入购物车，退出购物车
    def view_cart(self, anchor_x, anchor_y):
        # 点击“购物车”图标
        pyautogui.click(anchor_x + 25, anchor_y + 735, button='left')
        # 点击“去看看”图标
        pyautogui.click(anchor_x + 230, anchor_y + 680, button='left')
        # 判断是否进入“购物车”
        # pyautogui.sleep(2)
        if self.check_cart(anchor_x, anchor_y):
            print('进入购物车失败')
            # 进入失败的话，大概率是需要打开小程序界面，直接esc退出并返回到主界面
            pyautogui.click(anchor_x + 230, anchor_y + 680, button='left')
            pyautogui.press('esc')
            return False  # 返回值用于判断是否有浏览购物车并计数
        else:
            # 通过颜色判断是否有“红包”，若有则表示已退出购物车,若没有则继续点击
            while True:
                # pyautogui.sleep(2)
                pyautogui.click(anchor_x + 25, anchor_y + 20, button='left')
                # 颜色判断退出成功与否
                if pyautogui.screenshot().getpixel((anchor_x + 355, anchor_y + 175))[0] >= 230:
                    break
            return True

    # 判断是否有购物车按钮
    def check_cart(self, anchor_x, anchor_y):
        rgb_1 = pyautogui.screenshot().getpixel((anchor_x + 35, anchor_y + 735))
        rgb_2 = pyautogui.screenshot().getpixel((anchor_x + 50, anchor_y + 735))
        if rgb_1[0] > 250 and rgb_1[1] > 250 and rgb_2[0] > 250 and rgb_2[1] < 80:
            return True
        else:
            return False

    def run(self, ):
        # 检查管理员权限
        RunAsAdmin()
        while True:
            try:
                self.MAX_LIKES = int(input('输入点赞次数：'))
                self.MAX_CARTS = int(input('输入购物车浏览次数：'))
                break
            except ValueError:
                pyautogui.alert(text='仅接受数字输入！', title='错误！')

        pyautogui.alert(text='程序运行中将鼠标快速移动至屏幕左上角即可退出运行！', title='告知！')
        likes = 0
        carts = 0
        # 检测是否有看视频的标题图像，起始xy坐标和宽高
        base64_image = IMAGE_GUI
        image_data = b64decode(base64_image)
        image = Image.open(BytesIO(image_data))
        # image.show()
        try:
            l, r, w, h = pyautogui.locateOnScreen(image, confidence=0.9)  # 添加confidence防止nonetypeeerror，需要安装opencv库
            pyautogui.moveTo(l, r)
            print(f'标题栏坐标信息：x:{l}, y:{r}, w:{w}, h:{h}')
            while True:
                # 移至“去观看”按钮并点击
                pyautogui.click(l + 340, r + 400, button='left')
                if likes < self.MAX_LIKES:
                    if self.check_video(l, r):
                        self.like_video(l, r)
                    else:
                        pyautogui.sleep(2)
                        self.like_video(l, r)
                    likes += 1
                    print(f'点赞视频成功,第{likes}次点赞')

                if self.check_cart(l, r) and carts < self.MAX_CARTS:
                    if self.view_cart(l, r):
                        carts += 1
                        print(f'浏览购物车成功,第{carts}次浏览')
                    else:
                        print('浏览购物车失败')
                elif carts == self.MAX_CARTS:
                    break

                pyautogui.click(l + 20, r + 115, button='left')

        except TypeError:
            pyautogui.alert(text='无法找到视频界面，请确保界面无遮挡，显示完整。', title='警告！')
        except pyautogui.FailSafeException:
            pyautogui.alert(text='用户强制退出！', title='警告！')
        except Exception as e:
            # 处理其他异常的代码块
            pyautogui.alert(text=f'发生了未知异常：{type(e).__name__}', title='警告！')
        print('退出程序！')


if __name__ == '__main__':
    Automouse()
