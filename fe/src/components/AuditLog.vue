<template>
  <v-container fluid grid-list-lg>
    <v-layout row wrap align-center>
      <v-flex xs12 class="text-xs-center display-3 my-5">Audit Logs</v-flex>
    </v-layout>
    <v-layout row wrap align-center>
      <v-flex xs8 offset-md2>
        <!-- Audit log details -->
        <v-layout row justify-end fill-height xs8 offset-md-2>
          <v-dialog v-model="auditLogDialog" max-width="600px">
            <v-form ref="favoriteThingForm">
              <v-card>
                <v-card-title>
                  <div class="headline text-sm-center">Audit Log</div>
                </v-card-title>
                <v-card-text>
                  <v-container grid-list-md>
                    <v-layout wrap>
                      <v-flex xs12 v-for="(category, idx) in categoryList" :key="idx">
                        <p>Olakunle</p>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <!--<small>*indicates required field</small>-->
                </v-card-text>
                <v-card-actions>
                  <!--<v-spacer></v-spacer>-->
                  <v-btn color="brown darken-1" block flat @click="closeAuditLogDialog">Close</v-btn>
                  <!--<v-btn color="brown darken-1" flat @click="createNewFavoriteThing">Save</v-btn>-->
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </v-layout>
        <!-- end of audit log details-->

        <v-card v-for="(category, idx) in categoryList" :key="idx" class="my-2">
          <v-card-text>
            <v-layout row wrap>
              <v-flex xs6 align-left>
                <span class="body-1 align-left">{{category.name}}</span>
              </v-flex>
              <v-flex xs6 class="text-xs-right"></v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CategoryList',
  components: {},
  data() {
    return {
      sucVal: '',
      sucStatus: false,
      errorVal: '',
      errorStatus: false,
      auditLogDialog: false,
      currCategory: {}
    };
  },
  created() {
    this.$store.dispatch('getCategories');
  },
  computed: {
    categoryList() {
      return this.$store.state.categories;
    }
  },
  methods: {
    closeAuditLogDialog(){

    },
    showSuccessMessage(value) {
      this.sucVal = value.message;
      this.sucStatus = value.status;
      this.$store.dispatch('getCategories');
    }
  }
};
</script>
<style scoped>
.icons {
  cursor: pointer;
}
icon .icons:hover {
  color: #6d4c41;
}
</style>
