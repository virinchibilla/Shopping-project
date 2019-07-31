<template>
  <div class="Welcome">
   <div class="container columns">
    <div class="column is-full">
      <div class="tabs is-centered">
        <ul>
          <li :class="{'is-active' : tabSelected=='shopping'}" @click="tabSelected='shopping'"><a>My Shoppings</a></li>
          <li :class="{'is-active' : tabSelected=='my_invoices'}" @click="tabSelected='my_invoices'"><a>My Invoices</a></li>
          <li :class="{'is-active' : tabSelected=='profile'}"><a @click="tabSelected='profile'">My profile</a></li>
          <li :class="{'is-active' : tabSelected=='address'}"><a @click="tabSelected='address'">My Address</a></li>
          <li :class="{'is-active' : tabSelected=='admin'}"><a @click="tabSelected='admin'">Admin</a></li>
          <li :class="{'is-active' : tabSelected=='logout'}"><a @click="logout">Logout</a></li>
        </ul>
      </div>
      <div class="column">
        <h1 class="title is-4" id="adrs" v-show="tabSelected==''">First fill your address before you Buy a Product</h1>
      </div>
      <div id="shopping" class="container columns" v-if="tabSelected==='shopping'">
        <div class="column is-12">
          <div class="columns is-8">
            <div class="column is-1">
              <label class="label">Items</label>
            </div>
             <div class="column is-3">
               <div class="select">
                 <select v-model="currentitem">
                   <option :value="item" v-for="item in items">
                    {{ item[1] }} {{ item[3]}}
                  </option>
                </select>
              </div>
            </div>
            <div class="column is-1">
              <a class="button" @click="selectedItem()">ADD</a>
            </div>
          </div>
          <div class="columns is-8">
            <div class="column">
              <table class="table">
                <thead>
                  <tr>
                    <th> Name</abbr></th>
                    <th>Quantity</abbr></th>
                    <th>price</abbr></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="item in selectedItems">
                    <td v-html="item[1]"></td>
                    <td>
                      <div class="select">
                        <select v-model=item[2]>
                          <option :value="i" v-for="i in 10">
                            {{ i }}
                          </option>
                        </select>
                      </div>
                    </td>
                    <td>
                      {{ item[3] * item[2] }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="columns">
            <div class="column is-2">
            <p class="control">
                  <button
                  class="button is-primary"
                  v-on:click = "save_shopping"
                  >Create Invoice</button>
                </p>
              </div>
          </div>
          <div class="columns">
            <div class="column">
              <table class="table" v-show="invoice">
                <thead>
                  <tr>
                    <th>ID</abbr></th>
                    <th>items</abbr></th>
                    <th>date</abbr></th>
                    <th>sum</abbr></th>
                    <th>address</abbr></th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      {{ invoice.id }}
                    </td>
                    <td>
                      {{ invoice.items }}
                    </td>
                    <td>{{ invoice.date }}</td>
                    <td>
                      {{ invoice.sum }}
                    </td>
                    <td>
                      {{ invoice.address }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <div id="profile" class="container columns" v-if="tabSelected==='profile'">
        <div class="column is-8">
          <div class="columns">
            <div class="column is-2">
             <label class="label paddingtopless">first name</label> 
           </div>
           <div class="column is-2">
             <input v-model="user_data.first_name" class="input" type="text" placeholder="">
           </div>
         </div>
         <div class="columns">
          <div class="column is-2">
           <label class="label paddingtopless">Last name</label> 
         </div>
         <div class="column is-2">
           <input v-model="user_data.last_name" class="input" type="text" placeholder="">
         </div>
       </div>
       <div class="columns">
        <div class="column is-2">
         <label class="label paddingtopless">Email</label> 
       </div>
       <div class="column is-3">
         <input v-model="user_data.email" class="input" type="text" placeholder="">
       </div>
     </div>
     <div class="columns">
      <div class="column is-2">
       <label class="label paddingtopless">User name</label> 
     </div>
     <div class="column is-2">
       <input v-model="user_data.username" class="input" type="text" placeholder="">
     </div>
    </div>
    </div>
    </div>
      <div id="address" class="container columns" v-if="tabSelected==='address'">
        <div class="column is-8">
          <div v-for='address, i in addresses'>
            address {{ i }}
            <div class="columns">
              <div class="column is-2">
               <label class="label paddingtopless">Country</label> 
             </div>
             <div class="column is-2">
               <input v-model="address.country" class="input" type="text" placeholder="">
             </div>
           </div>
           <div class="columns">
            <div class="column is-2">
             <label class="label paddingtopless">City</label> 
           </div>
           <div class="column is-2">
             <input v-model="address.city" class="input" type="text" placeholder="">
           </div>
         </div>
         <div class="columns">
          <div class="column is-2">
           <label class="label paddingtopless">Street</label> 
         </div>
         <div class="column is-2">
           <input v-model="address.street" class="input" type="text" placeholder="">
         </div>
       </div>
       <div class="columns">
        <div class="column is-2">
         <label class="label paddingtopless">Postal code</label> 
       </div>
       <div class="column is-2">
         <input v-model="address.postalcode" class="input" type="text" placeholder="">
       </div>
      </div>
      </div>
      <hr>
      <div class="columns">
        <div class="column is-2">
          <button class="button is-primary" v-on:click='save_address'>Submit</button>
        </div>
      </div>
      </div>
      </div>
      <div id="admin" class="container columns" v-if="tabSelected==='admin'">
        <div class="column is-8" v-if="isAdmin">
          <table class="table">
            <thead>
              <tr>
                <th>First Name</abbr></th>
                <th>Lastname</abbr></th>
                <th>Email</abbr></th>
                <th>Role</abbr></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users_data_all">
                <td v-html="user.first_name"></td>
                <td v-html= "user.last_name"></td>
                <td v-html= "user.email"></td>
                <td>
                  <select class="select" v-model="user.role">
                    <option :value="r[0]" v-for="r in roles">
                      {{ r[0] }}
                    </option>
                  </select>
                </td>
              </tr>
            </tbody>
          </table>
              <p class="control">
              <label class="checkbox">
                <input type="checkbox">
                Is active
              </label>
            </p>
              <div class="column is-1">
             <div class="button" v-on:click="update_user">Update</div>
             {{ msg }}
           </div>
        </div>
        <div v-else class="column">
          <h1 class="title is-4">You are not an Admin</h1>
        </div>
      </div>
      <div id="my_invoices" class="container columns" v-if="tabSelected==='my_invoices'">
        <div class="column is-8">
          <table class="table">
            <thead>
              <tr>
                <th>Invoice</abbr></th>
                <th>Date</abbr></th>
                <th>sum</abbr></th>
                <th>Delievery Address</abbr></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="invoice in invoices">
                <td v-html="invoice.id"></td>
                <td v-html= "invoice.date"></td>
                <td v-html= "invoice.sum"></td>
                <td v-html= "invoice.address"></td>
                <td>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="button is-primary" v-on:click="get_invoice">get invoice</div>
        </div>
      </div>
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
    name: 'welcome',
    data() {
      return {
        users_data_all: '',
        user_data: '',
        table: '',
        items: [],
        title: 'Welcome to Your Vue.js App',
        timeline: 'deude',
        addresses: [{
          country: '',
          city: '',
          street: '',
          postalcode: '',
        }],
        tabSelected: '',
        // shoppingData: {
        //   itemname: ['xj'],
        //   quantity: '',
        //   price: '',
        // },
        currentitem: '',
        selectedItems: [],
        itemShop: {},
        invoice: '',
        invoices: [],
        isAdmin: '',
        roles: [],
        msg: '',
      };
    },
    methods: {
      save_address() {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1:8000/api/v1/address/',
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
          data: this.addresses[this.addresses.length - 1], // save the last element
        })
        .then(() => {
          this.msg = 'address saved';
          this.addresses.push({
            country: '',
            city: '',
            street: '',
            postalcode: '',
          });
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      update_user() {
        axios({
          method: 'PUT',
          url: 'http://127.0.0.1:8000/api/v1/user_data/update/',
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
          data: this.users_data_all, // save the last element
        })
        .then(() => {
          this.msg = 'users is updated';
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      save_shopping() {
        const dataToSend = { address: this.user_data.address[0].id };
        const arrIds = [];
        const arrQqt = [];
        for (let i = 0; i < this.selectedItems.length; i += 1) {
          arrIds.push(this.selectedItems[i][0]);
          arrQqt.push(this.selectedItems[i][2]);
        }
        dataToSend.item_id = arrIds;
        dataToSend.quantity = arrQqt;
        console.log(dataToSend);

        axios({
          method: 'POST',
          url: 'http://127.0.0.1:8000/api/v1/shopping/',
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
          data: dataToSend, // save the last element
        })
        .then((response) => {
          this.invoice = response.data;
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      loaditems() {
        axios({
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/v1/items/',
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.items = response.data;
          for (let i = this.items.length - 1; i >= 0; i -= 1) {
            this.items[i] = [this.items[i].id, this.items[i].item_name, 1, this.items[i].price];
          }
        })
        .catch((error) => {
          this.errorMessage = error.message;
        });
      },
      get_users_data_all() {
        axios({
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/v1/user_data/all/',
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.users_data_all = response.data.users_data;
          this.roles = response.data.roles;
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      get_invoice() {
        axios({
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/v1/user_data/invoice/',
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.invoices = response.data;
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      get_user_data() {
        const username = this.$session.get('username');
        axios({
          method: 'GET',
          url: `http://127.0.0.1:8000/api/v1/user_data/${username}/`,
          headers: {
            Authorization: `Token ${this.$session.get('token')}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.user_data = response.data;
          if (this.user_data.address) {
            // replace the addresses dict only if the user have oone or more adresses
            for (let i = 0; i < this.user_data.address.length; i += 1) {
              this.addresses.unshift(this.user_data.address[i]);
            }
          }
          router.push('/welcome');
        })
        .catch((error) => {
          this.msg = error.message;
        });
      },
      logout() {
        this.$session.destroy();
        router.push('/*');
      },
      selectedItem() {
        const item = this.currentitem;
        if (item === '') {
          return;
        }
        if (item[0] in this.itemShop) {
          // item[1] += 1;
          return;
        }

        this.selectedItems.push(item);
        this.itemShop[item[0]] = null;
      },
    },
    beforeMount() {
      this.get_user_data();
      this.loaditems();
      this.get_invoice();
      console.log(this.$session);
      this.isAdmin = this.$session.get('admin');
      if (this.isAdmin) {
        this.get_users_data_all();
      }
    },
    /*
    */
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
@import '~bulma';
h1, h2 {
  font-weight: normal;
}

a {
  color: #42b983;
}
#adrs {
  color: red;
}
</style>
