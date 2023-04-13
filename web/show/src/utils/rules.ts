// 用户名的校验规则
export const checkName = (rule:any,value:string,callback:any)=>{
    // 去除两边空格
    value = value.trim()
    if (value.length == 0){
        callback(new Error("用户名不能为空或空格"))
    }else if(value.length<2 || value.length >7){
         callback(new Error("用户名的长度应在2到7"))
    }else {
        callback()
    }
}
// 密码的校验规则
export const checkPassword = (rule:any,value:string,callback:any)=>{
    // 去除两边空格
    value = value.trim()
    if (value.length == 0){
        callback(new Error("密码不能为空或空格"))
    }else if(value.length<6 || value.length >12){
         callback(new Error("密码长度应在6到12"))
    }else {
        callback()
    }
}