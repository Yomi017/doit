from menu.menu_base import MenuBase
from menu.menu import GetMenu
from menu.control.control_menu import ControlMenu

class MainMenu(MenuBase):
    """主菜单实现"""
    
    def __init__(self, controllers_manager):
        self.controllers = controllers_manager  # 存储控制器管理器
        
        self.get_menu = None
        self.control_menu = None
        
        commands = {
            'get': (self.handle_get, "获取设备信息"),
            'control': (self.handle_control, "控制设备")
        }
        
        super().__init__("主菜单", "输入命令 (get/control/quit): ", commands)
        
        # 延迟初始化子菜单，避免循环引用
        self.get_menu = GetMenu(controllers_manager, self)
        self.control_menu = ControlMenu(controllers_manager, self)
        
    def handle_get(self):
        """处理获取信息命令"""
        return self.get_menu.handle_input()
        
    def handle_control(self):
        """处理控制设备命令"""
        return self.control_menu.handle_input()