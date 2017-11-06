import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '@/components/Login';
import Welcome from '@/components/Welcome';
import Signup from '@/components/Signup';

Vue.use(VueRouter);


const routes = [
{ path: '/signup', name: 'Signup', component: Signup },
{ path: '/welcome', name: 'Welcome', component: Welcome },
{ path: '/*', name: 'Login', component: Login },
];


const router = new VueRouter({
  // mode: 'history',
  routes,
});


export default router;

