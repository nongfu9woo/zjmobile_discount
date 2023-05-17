# zjmobile_discount
浙江移动小程序看视频领红包活动，自动刷视频  
使用`pyautogui`模块，实现电脑端自动刷视频，点赞，浏览购物车操作。  
![小程序首页](./小程序首页.png)

## 思路
1. 桌面微信打开浙江移动小程序；  
2. `pyautogui`模块自动操作；  
  * 因为有些图标比较小，识别老是出问题，除了用于起始坐标定位用的标题栏使用`pyautogui.locateOnScreen()`方法，其余全部使用相对坐标实现定位；(识别可能是精度的问题，默认为1.0精度，可以添加`confidence`参数将精度改为`0.9`，需要安装`opencv`模块，否则会报`NotImplementedError`)
  * `pyautogui`用户权限不能操作微信小程序，需要用管理员权限运行：[`/runAsAdmin`](./runAsAdmin.py)
## 使用
* 下载仓库源码  
* 安装python环境  
* 下载依赖  
```pip install requirements.txt```
* 运行[`/wechat_auto.py`](./wechat_auto.py)  
```python wechat_auto.py```
* 输入需要点赞的次数和浏览购物车的次数并确认
