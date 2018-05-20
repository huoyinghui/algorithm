from config.config import data_map


def cmp(src_data, dst_data, flag=True):
    # False, 0, None 暂定为相等
    if src_data in (0, False, None) and dst_data in (0, False, None):
        print('eq: {} == {}'.format(src_data, dst_data))
        return True

    if not flag:
        return False

    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in src_data:
            if key in dst_data:
                flag = cmp(src_data[key], dst_data[key])
                if not flag:
                    return flag
            else:
                print('{} not exist'.format(key))
                return False
    elif isinstance(src_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data):
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
            return False

        for src_list, dst_list in zip(src_data, dst_data):
            """递归"""
            flag = cmp(src_list, dst_list)
            if not flag:
                return flag
    else:
        # str/int
        if str(src_data) == str(dst_data):
            return True
        else:
            print("src_data:{} != dst_data:{}".format(src_data, dst_data))
            return False

    return True


def cmp2(obj1, obj2):
    # 空，返回true
    if obj1 in (0, False, None) and obj2 in (0, False, None):
        print('eq: {} == {}'.format(obj1, obj2))
        return True

    # 会失效
    return obj1 == obj2


def main():
    # ret = cmp(obj1, obj2)
    key = "com.catcto.jumping"
    key_test = "com.catcto.jumping_test"
    ret = cmp(data_map[key], data_map[key_test])
    print("ret1:", ret)
    # ret2 = cmp2(data_map[key], data_map[key_test])
    # print("ret2:", ret2)

if __name__ == '__main__':
    main()