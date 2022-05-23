<template id="login-form">
    <el-row :gutter="20" class="login-form">
        <el-col :span="8" :offset="6">
            <el-card shadow="always">
                <img height="100" src="/wisk-logo-black.png" srcr="/bar_bg.jpg">
                <el-form :model="user" label-width="80px">
                    <el-form-item label="用户名">
                        <el-input v-model="user.username"></el-input>
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="user.password"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" round>Login</el-button>
                    </el-form-item>
                </el-form>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
import axios from "axios";
export default {
    name: "LoginForm",
    template: "#login-form",
    data() {
        return {
            user: {
                username: "",
                password: ""
            },
        };
    },
    methods: {
        login() {
            //we should handle errors in a more scalabe way, but this works for now
            axios.post("http://localhost:8000/login", {
                    body: {
                        user: this.user
                    }
                })
                .then(response => {
                    alert(response);
                    //handle response and save JWT
                })
                .catch(err => {
                    alert(err);
                });
        }
    }
};
</script>
<style>
.login-form {
   text-align: center;

}
</style>