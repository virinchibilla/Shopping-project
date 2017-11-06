<template>
  <div class="login">
    <div class="container columns">
      <div class="column is-8">
        <div class="columns">
          <div class="column is-4">
            <h1 class="title is-1">{{ title }}</h1>
          </div>
        </div>
        <form class="column is-half">
          <div class="field">
            <label class="label">username</label>
            <p class="control">
              <input v-model="username" class="input" type="text" placeholder="username">
            </p>
          </div>
          <br>
          <div class="field">
            <label class="label">Password</label>
            <p class="control">
              <input v-model="password" class="input" type="password" placeholder="Password">
            </p>
          </div>
          <br>
          <div class="columns">
            <div class="column is-3">
              <p class="control">
                <button
                class="button is-primary"
                v-on:click = 'loguser'
                >Sign in</button>
              </p>
              <p v-if="loginFailed" class="help is-danger">{{ loginError }}</p>
            </div> <br>
            <div class="column is-2">
              <p class="control">
                <button
                class="button is-primary"
                v-on:click = 'signup'
                >Sign up</button>
              </p>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import VueSession from 'vue-session';
  import Vue from 'vue';
  import axios from 'axios';
  import router from '../router';
  
  Vue.use(VueSession);

  export default {
    name: 'login',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        username: '',
        password: '',
        title: '',
        loginFailed: false,
      };
    },
    methods: {
      loguser() {
        const data = { username: this.username, password: this.password };
        axios.post('http://127.0.0.1:8000/api/v1/loguser/', data)
        .then((response) => {
          this.msg = 'log in successful';
          this.$session.start();
          this.$session.set('username', response.data.username);
          this.$session.set('token', response.data.token);
          this.$session.set('admin', response.data.admin);
          console.log(response);
          router.push('/welcome');
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      signup() {
        router.push('/signup');
      },
    },
    beforeMount() {
   // this.loguser();
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
@import '~bulma';

</style>
