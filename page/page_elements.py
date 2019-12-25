from selenium.webdriver.common.by import By


class PageElements:
    """通讯录主页面"""

    # 联系人1
    address = (By.ID, "com.android.contacts:id/cliv_name_textview")

    """联系人详情页"""

    # 编辑按钮

    edit = (By.ID, "com.android.contacts:id/menu_edit")
    # 获取联系人信息
    linkman_name_result = (By.ID, "com.android.contacts:id/title")

    """修改联系人页面"""

    # 修改name
    input_name = (By.CLASS_NAME, "android.widget.EditText")
    # 点击返回
    back_linkman = (By.CLASS_NAME, "android.widget.ImageButton")
