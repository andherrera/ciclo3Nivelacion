<template>    
    <div v-if="loaded" class="signUp_user">
        <div class="container_signUp_user">
            <h2>Seleccione el producto</h2>
                <br>
                <br>
                <br>
                <select class="form-select form-select-sm" aria-label=".form-select-sm example" v-model="selectedApp">
                    <option selected disabled value="">Choose</option>
                    <option v-for="result in productsData" :value="result.id">{{ result.nombre }}</option>
                </select>
                <div>ID producto seleccionado: {{ selectedApp }}</div>
                <button type="button" v-if="!is_auth" v-on:click="findProduct" >Agregar Producto</button>                
        </div>
    </div>
</template>
<script>
    import axios from 'axios';
    export default {
        name: "Productos",        
        data: function(){
            return {
                selectedApp: "",
                productsData: [],
                loaded: false,
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
                axios.get(`http://127.0.0.1:8000/producto/`, {headers: {'Authorization': `Bearer ${token}`}}
                )
                .then((result) => {
                    this.productsData = result.data
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
            findProduct: function(){
                console.log(this.selectedApp)
                axios.get(`http://127.0.0.1:8000/producto/${this.selectedApp}/`, {headers: {}}
                )
                .then((result) => {
                    alert(JSON.stringify(result.data, null, ' '));
                })
                .catch(() => {
                    this.$emit('logOut');
                });
            },
            deleteProduct: function(){
                console.log(this.selectedApp)
                axios.delete(`http://127.0.0.1:8000/producto/${this.selectedApp}/`, {headers: {}}
                )
                .then(() => {
                    alert('Producto con ID: ' +this.selectedApp+ ' eliminado correctamente');
                })
                .catch(() => {
                    this.$emit('logOut');
                });
            }

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
    border: 3px solid #fafafa;
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


