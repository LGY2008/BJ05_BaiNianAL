import Page
from Base.base import Base
class PageAddress(Base):
    # 点击 地址管理
    def page_click_address_manage(self):
        self.base_click(Page.address_manage)
    # 点击 新增地址
    def page_click_new_address(self):
        self.base_click(Page.address_new_address)
    # 输入 收件人
    def page_input_receipt_name(self,receipt_name):
        self.base_input(Page.address_receipt_name,receipt_name)
    # 输入 手机号
    def page_input_phone(self,phone):
        self.base_input(Page.address_add_phone,phone)
    # 选择 所在地区
    def page_click_area(self,sheng,shi,qu):
        # 点击 所在地区
        self.base_click(Page.address_area)
        # 选择 省
        self.base_xpath_click(sheng)
        # 选择 市
        self.base_xpath_click(shi)
        # 选择 区
        self.base_xpath_click(qu)
    # 选择 所在地区02
    def page_click_area_zhixia(self,sheng,qu):
        # 点击 所在地区
        self.base_click(Page.address_area)
        # 选择 省
        self.base_xpath_click(sheng)
        # 点击市 大框
        self.base_click(Page.zhixiashikuang)
        # 选择 市
        self.base_click(Page.zhixiashi)
        # 选择 区
        self.base_xpath_click(qu)
    # 输入 详细地址
    def page_input_detail_address(self,address):
        self.base_input(Page.address_detail_addr,address)
    # 输入 邮编
    def page_input_post_code(self,postcode):
        self.base_input(Page.address_post_code,postcode)
    # 点击设为默认地址
    def page_click_default_address(self):
        self.base_click(Page.address_default)
    # 点击保存
    def page_click_save(self):
        self.base_click(Page.address_save)
    # 获取收件人和电话
    def page_get_recipit_and_phone(self):
        # 返回收件人 和电话
        return self.base_get_text(Page.address_receipt_and_phone)
    # 获取一组元素的文本
    def page_get_elements_text(self):
        # 获取地址列表（收件人+电话）所有元素
        elemets=self.base_find_elements(Page.address_receipt_and_phone)
        # 返回每个元素的文本
        return [i.text for i in elemets]
    # 点击编辑
    def page_click_edit_btn(self):
        # self.base_click(Page.address_edit_btn)
        # 第二种方式  测试
        self.base_xpath_click("编辑")
    # 点击修改
    def page_click_update(self,text="修改"):
        # 获取所有修改元素
        elements=self.base_xpaths(text)
        # 点击列表元素中第一个元素
        self.base_click_elements(elements)
    # 点击保存
    def page_click_save_btn(self):
        self.base_xpath_click(Page.address_save_btn)

    # 删除地址
    def page_delete_address(self,text="删除"):
        # 获取当前所有地址列表
        elements=self.base_find_elements(Page.address_receipt_and_phone)
        for i in range(len(elements)):
            # 点击 编辑
            self.page_click_edit_btn()
            # 获取所有修改元素
            elements=self.base_xpaths(text)
            # 点击列表元素中第一个元素
            self.base_click_elements(elements)
            # 点击确认删除
            self.base_click(Page.address_delete_ok)
    def page_is_delete(self):
        try:
            self.base_find_elements(Page.address_receipt_and_phone,timeout=3)
            return False
        except:
            return True
