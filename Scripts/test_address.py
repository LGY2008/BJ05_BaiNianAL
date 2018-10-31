import os, sys
sys.path.append(os.getcwd())

import allure
import pytest
from Base.read_yaml import ReadYaml
from Page.page_in import PageIn
from Base.get_driver import get_driver


def get_data(text_type):
    datas = ReadYaml("address.yaml").read_yaml()
    arrs = []
    if text_type == "add":
        for data in datas.get("add_address").values():
            arrs.append((
                data.get("receipt_name"), data.get("phone"), data.get("sheng"), data.get("shi"), data.get("qu"),
                data.get("address"), data.get("postcode")))
        return arrs
    elif text_type == "update":
        for data in datas.get("update_address").values():
            arrs.append((
                data.get("receipt_name"), data.get("phone"), data.get("sheng"), data.get("shi"), data.get("qu"),
                data.get("address"), data.get("postcode"), data.get("toast_expect")))
        return arrs


class TestAddress():
    def setup_class(self):
        # 登录成功
        self.page = PageIn(get_driver())
        self.page.page_get_login().page_login("18610453007", "123456")
        # 点击设置
        self.page.page_get_login().page_click_setting()
        # 实例化 PageAddress
        self.address = self.page.page_get_address()
        # 点击地址管理
        self.address.page_click_address_manage()

    def teardown_class(self):
        # 关闭 驱动对象
        self.page.driver.quit()

    # 新增地址
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("receipt_name,phone,sheng,shi,qu,address,postcode", get_data("add"))
    def test_add_address(self, receipt_name, phone, sheng, shi, qu, address, postcode):
        addr = self.address
        # 点击 新增地址
        addr.page_click_new_address()
        # 输入 收件人
        addr.page_input_receipt_name(receipt_name)
        # 输入 手机号
        addr.page_input_phone(phone)
        # 选择 所在区域
        addr.page_click_area(sheng, shi, qu)

        # 选择 所在区域2
        # addr.page_click_area_zhixia("北京","海淀")

        # 输入 详细地址
        addr.page_input_detail_address(address)
        # 输入 邮编
        addr.page_input_post_code(postcode)
        # 点击 设为默认地址
        addr.page_click_default_address()
        # 点击 保存
        addr.page_click_save()
        try:
            # 断言 是否新增成功
            # print("获取新增地址联系人和电话为：",addr.page_get_recipit_and_phone())
            # assert receipt_name in addr.page_get_recipit_and_phone()

            """第二种实现断言方法：通过后去地址列表所有的收件和电话"""
            # 组装字符串，模拟获取文本后的格式：  "张三  18600000000"
            name_phont = receipt_name + "  " + phone
            assert name_phont in addr.page_get_elements_text()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise

    # 更新地址
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("receipt_name,phone,sheng,shi,qu,address,postcode,toast_expect", get_data("update"))
    def test_update_address(self, receipt_name, phone, sheng, shi, qu, address, postcode, toast_expect):
        addr = self.address
        # 点击 编辑
        self.address.page_click_edit_btn()
        # 点击 修改
        self.address.page_click_update()
        """输入 修改信息"""
        # 输入 收件人
        addr.page_input_receipt_name(receipt_name)
        # 输入 手机号
        addr.page_input_phone(phone)
        # 选择 所在区域
        addr.page_click_area(sheng, shi, qu)
        # 输入 详细地址
        addr.page_input_detail_address(address)
        # 输入 邮编
        addr.page_input_post_code(postcode)
        # 点击 保存
        addr.page_click_save_btn()
        try:
            """第一种断言更新是否成功：断言更新后的用户名+电话，是否在地址列表中"""
            name_phont = receipt_name + "  " + phone
            assert name_phont in addr.page_get_elements_text()

            """第二种断言更新是否成功：根据toast消息  保存成功"""
            assert toast_expect in self.address.base_get_toast(toast_expect)
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise

    # 删除地址
    @pytest.mark.run(order=3)
    def test_delete_address(self):
        # 删除地址操作  默认删除第一个地址
        self.address.page_delete_address()
        try:
            # 断言
            assert self.address.page_is_delete()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise
