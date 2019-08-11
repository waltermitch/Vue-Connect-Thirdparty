<template>
  <v-container fluid grid-list-lg>
    <v-layout row wrap align-center>
      <v-flex xs12 class="text-xs-center display-3 my-5">Category</v-flex>
      <v-flex xs8 offset-md2 class="text-xs-left body-2">
        <v-alert
          v-model="sucStatus"
          dismissible
          color="success"
          icon="check_circle"
          outline
        >{{sucVal}}</v-alert>
      </v-flex>
    </v-layout>
    <v-layout row wrap align-center>
      <v-flex xs8 offset-md2>
        <!-- Edit Dialog -->
        <v-layout row justify-end fill-height xs8 offset-md2>
          <v-dialog v-model="editDialog" max-width="500px">
            <v-form ref="editCategoryForm">
              <v-card>
                <v-card-title>
                  <div class="headline">Edit Category</div>
                </v-card-title>
                <v-card-text>
                  <v-container grid-list-md>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-alert
                          :value="errorStatus"
                          color="error"
                          icon="warning"
                          outline
                          transition="scale-transition"
                        >{{errorVal}}</v-alert>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          label="Category Name*"
                          :rules="categoryRules"
                          v-model="currCategory.name"
                          required
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="brown darken-1" flat @click="closeEditDialog">Close</v-btn>
                  <v-btn color="brown darken-1" flat @click="updateCategory">Update</v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </v-layout>
        <!-- end -->
        <!--<edit-category :dialogStatus="editDialog"></edit-category>-->
        <new-category v-on:successfulCreation="showSuccessMessage"></new-category>
        <v-card v-for="(category, idx) in categoryList" :key="idx" class="my-2">
          <v-card-text>
            <v-layout row wrap>
              <v-flex xs6 align-left>
                <span class="body-1 align-left">{{category.name}}</span>
              </v-flex>
              <v-flex xs6 class="text-xs-right">
                <v-icon
                  color="brown darken-4"
                  class="icons mx-3"
                  @click="editCategory(category)"
                >edit</v-icon>
                <v-icon
                  color="brown darken-4"
                  class="icons mx-3"
                  @click="deleteCategory(category.id)"
                >delete</v-icon>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import NewCategory from './NewCategory';
import EditCategory from './EditCategory';
import axios from 'axios';
export default {
  name: 'CategoryList',
  components: {
    NewCategory,
    EditCategory
  },
  data() {
    return {
      sucVal: '',
      sucStatus: false,
      errorVal: '',
      errorStatus: false,
      editDialog: false,
      categoryRules: [category => !!category || 'Category name is required.'],
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
    showSuccessMessage(value) {
      this.sucVal = value.message;
      this.sucStatus = value.status;
      this.$store.dispatch('getCategories');
    },
    editCategory(cat) {
      this.currCategory = cat;
      this.editDialog = true;
    },
    closeEditDialog() {
      this.currCategory = {};
      this.editDialog = false;
      this.errorVal = '';
      this.errorStatus = false;
    },
    async updateCategory() {
      if (!this.$refs.editCategoryForm.validate()) {
        return;
      }
      if (this.currCategory == null) {
        return;
      }
      // perform update
      let api_url = `${this.$store.state.apiBaseUrl}/category/${
        this.currCategory.id
      }/`;
      try {
        let response = await axios.put(api_url, this.currCategory);
      } catch (error) {
        errorVal = 'An error occured, please try again later.';
        errorStatus = true;
      }
      this.$store.dispatch('getCategories');
      this.sucVal = 'Update operation was successful.';
      this.sucStatus = true;
      this.editDialog = false;
    },
    async deleteCategory(category_id) {
      if (confirm('Are you sure you want to delete this category?')) {
        try {
          let api_url = `${
            this.$store.state.apiBaseUrl
          }/category/${category_id}/`;
          console.log(api_url);
          let response = await axios.delete(api_url);
        } catch (error) {
          console.log(`${error}`);
        }
        this.$store.dispatch('getCategories');
        this.sucVal = 'Delete operation was successful.';
        this.sucStatus = true;
      }
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
