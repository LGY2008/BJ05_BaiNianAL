import yaml,os

class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+"Data"+os.sep+filename

    def read_yaml(self):
        with open(self.filepath,"r",encoding="utf-8")as f:
            return yaml.load(f)
    def read_yaml02(self):
        with open("../Data/address.yaml","r",encoding="utf-8")as f:
            return yaml.load(f)
if __name__ == '__main__':

    """     最终要的格式：
            return [("18610453007","123456"),(),()]
    """
    # datas=ReadYaml("login.yaml").read_yaml02()
    # print(datas)
    # arrs=[]
    # for data in datas.values():
    #     arrs.append((data.get("username"),data.get("password"),data.get("expect"),data.get("toast_expect")))
    # print(arrs)
    def get_data(text_type):
        datas=ReadYaml("address.yaml").read_yaml02()
        arrs=[]
        if text_type=="add":
            for data in datas.get("add_address").values():
                arrs.append((data.get("receipt_name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("address"),data.get("postcode")))
            return arrs
        elif text_type=="update":
            for data in datas.get("update_address").values():
                arrs.append((data.get("receipt_name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("address"),data.get("postcode"),data.get("toast_expect")))
            return arrs



    print(get_data("update"))
    print(get_data("add"))