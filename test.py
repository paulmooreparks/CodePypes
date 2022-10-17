
import CodePypes as cp

def main():
    # cp.refresh_token()

    print("Config:")
    print(cp.config)
    print()

    rsp = cp.get_profile()
    print("Profile:")
    print(rsp)
    print()

    rsp = cp.get_organizations()
    print("Organizations:")
    print(rsp)

main()
