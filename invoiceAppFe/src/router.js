import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';
import LogIn from './components/LogIn.vue'
import SignUpCliente from './components/SignUpCliente.vue'
import SignUpEmpleado from './components/SignUpEmpleado.vue'
import Home from './components/Home.vue'
import Account from './components/Account.vue'
import RolChoice from './components/RoleChoice.vue'
import Products from './components/Products.vue'
import Invoice from './components/Invoice.vue'
const routes = [{
        path: '/',
        name: 'root',
        component: App
    },
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/signUpCliente',
        name: "signUpCliente",
        component: SignUpCliente
    },
    {
        path: '/user/signUpEmpleado',
        name: "signUpEmpleado",
        component: SignUpEmpleado
    },
    {
        path: '/user/home',
        name: "home",
        component: Home
    },
    {
        path: '/user/account',
        name: "account",
        component: Account
    },
    {
        path: '/user/rolChoice',
        name: "rolChoice",
        component: RolChoice
    },
    {
        path: '/user/productos',
        name: "products",
        component: Products
    },
    {
        path: '/user/factura',
        name: "invoice",
        component: Invoice
    }
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;