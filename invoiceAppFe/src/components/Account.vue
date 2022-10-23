<template>
    <div v-if="loaded" class="signUp_user">
        <div class="container_signUp_user">
            <form>
                <h6>Correo electrónico: <span>{{email}}</span></h6>
                <span v-if="rol == 'Empleado'">
                    <button type="button" v-if="!is_auth" v-on:click="loadProveedor" > Registar Proveedor </button>
                    <button type="button" v-if="!is_auth" v-on:click="loadActions" > Consultar  Proveedor</button>
                    <button type="button" v-if="!is_auth" v-on:click="loadActions" > Registar Producto </button>
                    <button type="button" v-if="!is_auth" v-on:click="loadProducts" > Administrar  Productos</button>
                    <button type="button" v-if="!is_auth" v-on:click="loadActions" > Consultar  Factura</button>
                </span>
                <span v-else-if="rol == 'Cliente'">
                    <button type="button" v-if="!is_auth" v-on:click="loadPurchase" > Realizar Compra</button>
                    <button type="button" v-if="!is_auth" v-on:click="loadActions" > Consultar mis Facturas</button>
                </span>
            </form>
        </div>
    </div>
</template>
<script>
    import jwt_decode from "jwt-decode";
    import axios from 'axios';
    export default {
        name: "Invoice",        
        data: function(){
            return {
                email: "",
                rol: "",
                loaded: false,
                userID: ""
            }
        },
        methods: {
            getData: async function () {
                if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                    this.$emit('logOut');
                    return;
                }
                await this.verifyToken();
                let token = localStorage.getItem("token_access");
                let userId = jwt_decode(token).user_id.toString();
                axios.get(`http://127.0.0.1:8000/usuario/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}}
                )
                .then((result) => {
                    this.name = result.data.name;
                    this.email = result.data.email;
                    this.rol = result.data.rol;
                    this.loaded = true;
                })
                .catch(() => {
                    this.$emit('logOut');
                });
            },
            verifyToken: function () {
                return axios.post("http://127.0.0.1:8000/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}}
                )
                .then((result) => {
                    localStorage.setItem("token_access", result.data.access);
                })
                .catch(() => {
                    this.$emit('logOut');
                });
            },
            loadProducts: function(){
                this.$router.push({name: "products"})
            },
            loadPurchase: function(){
                let token = localStorage.getItem("token_access");
                let userId = jwt_decode(token).user_id.toString();
                axios.get(`http://127.0.0.1:8000/cliente/${userId}/`, {headers: {}})
                .then((result) => {
                    localStorage.setItem("clienteId", result.data.id);
                    this.$router.push({name: "invoice"});                 
                    
                    })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");
                });
                /*axios.post(`http://127.0.0.1:8000/factura/`, {
                    cliente: localStorage.getItem('clienteId')

                    }).then(() => {
                        this.$router.push({name: "invoice"});
                    })
                    .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");
                });*/
                
            },
        },
        created: async function(){
            this.getData();
        },
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
}
.container_signUp_user {
    border: 3px solid #283747;
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


