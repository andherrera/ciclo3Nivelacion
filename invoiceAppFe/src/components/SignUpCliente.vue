<template>
    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2>Registro Cliente</h2>
            <form v-on:submit.prevent="processSignUp" >
                <input type="text" v-model="usuario.user.username" placeholder="Username">
                <br>
                <input type="password" v-model="usuario.user.password" placeholder="Password">
                <br>
                <input type="text" v-model="usuario.user.name" placeholder="Nombres">
                <br>
                <input type="email" v-model="usuario.user.email" placeholder="Email">
                <br>
                <input type="text" v-model="usuario.user.ciudad" placeholder="Ciudad">
                <br>
                <input type="text" v-model="usuario.direccion" placeholder="Direccion">
                <br>
                <button type="submit">Registrarse</button>
            </form>
        </div>
    </div>
</template>
<script>
    import axios from 'axios';
    export default {
        name: "signUpCliente",
        data: function(){
            return {
                usuario: {
                    user: {
                        username : "",
                        password : "",
                        name : "",
                        lastname : "",
                        city: "",
                        email : "",
                        address: "",
                        cellphone: ""                        
                    }
                }
            }
        },
        methods: {
            processSignUp: function(){
                axios.post(
                    "http://127.0.0.1:8000/cliente/",
                    this.usuario,
                    {headers: {}}
                    )
                    .then((result) => {
                        let dataSignUp = {
                            username: this.usuario.user.username,
                            token_access: result.data.access,
                            token_refresh: result.data.refresh,
                        }
                        this.$emit('completedSignUp', dataSignUp)
                    })
                    .catch((error) => {
                        console.log(error)
                        alert("ERROR: Fallo en el registro.");
                    }
                );
            }
        }
    }
</script>
<style>
    .signUp_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .container_signUp_user {
        border: 3px solid #FFFFFF;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .signUp_user h2{
        color: #283747;
    }
    .signUp_user form{
        width: 70%;
    }
    .signUp_user input{
        height: 40px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #283747;
    }
    .signUp_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }
    .signUp_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }
</style>