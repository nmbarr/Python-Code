from modules import read_cdl, read_configs, validation, build_mwl

def main():
    data = read_configs.main()
    read_cdl.main(data)
    # validation.main()
    # build_mwl.main()

if __name__ == '__main__':
    main()