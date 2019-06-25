<template>
  <div class="signup">
    <div class="container columns">
      <div class="column is-8">
        <div class="columns">
          <div class="column is-4">
        <h1 class="title is-1">{{ title }}</h1>
      </div>
    </div><br>
        <div class="columns">
          <div class="column is-2">
            <b>First Name</b>
          </div>
          <div class="column is-4">
            <input v-model="firstname" class="input" type="text">
          </div>
        </div>
        <div class="columns">
          <div class="column is-2">
            <b>Last Name</b>
          </div>
          <div class="column is-4">
            <input v-model="lastname" class="input" type="text">
          </div>
        </div>
        <div class="columns">
          <div class="column is-2">
            <b>Email</b>
          </div>
          <div class="column is-4">
            <input v-model="email" class="input" type="Email">
          </div>
        </div>
        <div class="columns">
          <div class="column is-2">
            <b>Password</b>
          </div>
          <div class="column is-4">
            <input v-model="password" class="input" type="password">
          </div>
        </div>
        <div class="columns">
          <div class="column is-2">
            <b>Confirm password</b>
          </div>
          <div class="column is-4">
            <input v-model="confirmpassword" class="input" type="password">
          </div>
        </div>
        <div class="columns">
          <div class="column is-2">
            <b>User Name</b>
          </div>
          <div class="column is-4">
            <input v-model="username" class="input" type="text">
          </div>
        </div>
        <div class="column is-4">
              <p class="control">
                <button
                class="button is-primary"
                v-on:click = 'signup'
                >Sign up</button>
              </p>
            </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import router from '../router';

  export default {
    name: 'signup',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        firstname: '',
        lastname: '',
        email: '',
        password: '',
        confirmpassword: '',
        username: '',
        title: 'Signup',
        error: '',
      };
    },
    methods: {
      signup() {
        if (this.confirmpassword !== this.password) {
          this.error = 'Cannot sign up. Password should match';
          return;
        }

        const data = { firstname: this.firstname,
          lastname: this.lastname,
          email: this.email,
          password: this.password,
          username: this.username,
          confirmpassword: this.confirmpassword };
        axios.post('http://127.0.0.1:8000/api/v1/signup/', data)
        .then(() => {
          this.msg = 'sign in successful';

          router.push('/*');
        })
        .catch((error) => {
          this.msg = error.message;
        });
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
