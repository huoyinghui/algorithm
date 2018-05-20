function isObj(object) {
    return object && typeof (object) == 'object' && Object.prototype.toString.call(object).toLowerCase() == "[object object]";
}

function isArray(object) {
    return object && typeof (object) == 'object' && object.constructor == Array;
}
/*
1.nan/undefine 不比较
2.array:
    for i=0; i<length; i++:
        递归(obj1[i], obj2[i])

3.map:
    for k in obj1:
       if k in obj2:
            递归
       else:
            失败
*/
function cmp(obj1, obj2, flag) {
    //nan/undefine/false/0
    if (!obj1 && !obj2) {
        return true;
    }

    if (!flag) {
        return false;
    }

    if (isObj(obj1)) {
        for (var key in obj1) {
            if (key in obj2) {
                flag = cmp(obj1[key], obj2[key], flag);
                if (!flag) {
                    return flag;
                }
            }else{
                console.log("key:", key, "v:", obj1[key], "not in obj2");
                return false;
            }
        }
    }else if (isArray(obj1)) {
        if (obj1.length != obj2.length) {
            console.log("obj1.len:", getLength(obj1), 'obj2.len:', getLength(obj2));
            return false;
        }

        for (var i = 0, l = obj1.length; i < l; i++) {
            flag = cmp(obj1[i], obj2[i], flag);
            if (!flag) {
                return flag;
            }
        }
    }else{
        if (obj1 == obj2) {
            return true;
        }else{
            console.log("(obj1)", obj1, "!=", "(obj2)", obj2);
            return false;
        }
    }
    return true;
}
exports.compare = cmp;