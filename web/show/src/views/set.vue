<template>
    <div class="my">
        <div class="card">
            <h2 class="title">修改用户信息</h2>
            <div class="edit">
                <el-upload>
                    <el-button type="primary">上传新头像</el-button>
                    <template #tip>
                        <div class="el-upload__tip">
                            jpg/png files with a size less than 500KB.
                        </div>
                    </template>
                </el-upload>
                <input type="text" placeholder="请输入新的昵称">
                <input type="text" placeholder="请输入密码">
                <input type="text" placeholder="请输入新密码">
            </div>
            <div class="quit">
                <el-button type="primary">保存</el-button>
                <el-button type="info">取消</el-button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style lang="scss" scoped>
.my {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    .card {
        width: 300px;
        height: 500px;
        border-radius: 5% 5% 0 0;
        box-shadow: 0 0 10px #000;
        padding:20px;
        .title {
            margin-bottom: 40px;
        }
        .edit {
            display: flex;
            flex-direction: column;
            justify-content: space-evenly;
            input {
                margin-top:20px;
                width: 100%;
                height: 40px;
                line-height: 40px;
                border:none;
                border-bottom:1px solid #000;
                outline: none;

            }
        }
        .quit {
            margin-top: 20px;
        }
    }


}
</style>