import sys
import paramiko

arg_list=sys.argv

class Parser():
    def __init__(self):
        self.config_set={
                        "--config":[False,["static","dynamic"]],
                        "--connect":[False,[]]
                        # "--wifi":[False,["setup","change-pass","change-ssid"]]
                        }
    
    def confirm_operation(self):
        for keys_config in self.config_set.keys():
            if keys_config in arg_list[1:2]:
                #print(self.validate_syntax(keys_config))
                if self.validate_syntax(keys_config):
                    self.config_set[keys_config][0]=True
                    return
            
    def validate_syntax(self,check_it):
        for validators in self.config_set[check_it][1:]:
            if len(validators)==0:
                return True
            else:
                for items in validators:
                    if items in arg_list[2:]:
                        return True
            return False

    def redirector(self):
        for keys_config in self.config_set.keys():
            if self.config_set[keys_config][0]:
                return keys_config
    
    def checker(self):
        for keys_config in self.config_set.keys():
            print(self.config_set[keys_config][0])

class Configure():
    def execute_dynamic(self):
        print("dynamic")
    
    def execute_static(self,details):
        ip=details[0]
        subnet=details[1]
        gateway=details[2]
        print(f"Controlling with {ip} {gateway}")

class Connect():
    def __init__(self,details):
        self.host=details[0]
        self.username=details[1]
        self.password=details[2]

    def connect_mik(self):
        print("Passed")

# class Wireless():
#     def __init__(self,details):
#         self.ssid=details[0]
#         self.passphrase=details[1]
#     def execute_wifi_config():
#         pass
    
def main():
    parse=Parser()
    parse.confirm_operation()
    #parse.checker()
    x=parse.redirector()
    if x=='--config':
        if arg_list[2]=="static":
            if len(arg_list)==6 :
                check_configure=Configure()
                check_configure.execute_static(arg_list[3:])
            else:
                print("Please Provide IP address , Subnetmask , Gateway ")

        elif arg_list[2]=="dynamic":
            if len(arg_list)==3:
                check_configure=Configure()
                check_configure.execute_dynamic()
            else:
                print("Please Follow Documentation Syntax")

        
    elif x=='--connect':
        if len(arg_list)==5:
            connect_para=Connect(arg_list[2:])
            connect_para.connect_mik()
        else:
            print("Please Follow Documentation Syntax")
    

    else:
        print("Please Read the Documentation")

main()