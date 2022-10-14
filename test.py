
import CodePypes as cp

def main():
    print("Config:")
    print(cp.config)
    print()

    rsp = cp.get_self()
    print("Profile:")
    print(rsp)
    print()

    rsp = cp.get_organizations()
    print("Organizations:")
    print(rsp)

main()
