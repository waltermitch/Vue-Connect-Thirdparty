<template>
  <!-- New category pop up-->
  <v-layout row justify-end fill-height xs8 offset-md2>
    <v-dialog v-model="dialog" persistent max-width="500px">
      <template v-slot:activator="{ on }">
        <v-btn flat outline color="brown" dark v-on="on">
          <v-icon>add</v-icon>New Category
        </v-btn>
      </template>
      <v-form ref="categoryForm">
        <v-card>
          <v-card-title>
            <div class="headline">New Category</div>
          </v-card-title>
          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-alert
                    v-model="errorStatus"
                    color="error"
                    icon="warning"
                    outline
                    transition="scale-transition"
                  >{{errorVal}}</v-alert>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    v-model="categoryData.name"
                    label="Category Name*"
                    :rules="categoryRules"
                    required
                  ></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="brown darken-1" flat @click="closeDialog">Close</v-btn>
            <v-btn color="brown darken-1" flat @click="createNewCategory">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </v-layout>
  <!-- End -->
</template>
<script>
import axios from 'axios';
export default {
  name: 'NewCategory',
  data() {
    return {
      errorStatus: false,
      errorVal: '',
      categoryRules: [category => !!category || 'Category name is required.'],
      categoryData: {
        name: ''
      },
      dialog: false
    };
  },
  methods: {
    closeDialog() {
      this.categoryData.name = '';
      this.dialog = false;
      this.errorVal = '';
      this.errorStatus = false;
      this.$refs.categoryForm.reset();
      this.$refs.categoryForm.resetValidation();
    },
    async createNewCategory() {
      if (!this.$refs.categoryForm.validate()) {
        return;
      }
      let api_url = `${this.$store.state.apiBaseUrl}/category/`;
      try {
        let status = await axios.post(api_url, this.categoryData);
        this.categoryData.name = '';
        let data = {
          message: 'Category creation was successful.',
          status: true
        };

        this.$emit('successfulCreation', data);
        //this.sucVal = 'Category creation was successful.';
        //this.sucStatus = true;
        this.closeDialog();
      } catch (error) {
        console.log(`${error}`);
        this.errorVal = 'An error occured, please try again later.';
        this.errorStatus = true;
      }
    }
  }
};
</script>

<style scoped>
</style>


