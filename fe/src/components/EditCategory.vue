<template>
  <v-layout row justify-end fill-height xs8 offset-md2>
    <v-dialog v-model="dailogStatus" max-width="500px">
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
                  <v-text-field label="Category Name*" required></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="brown darken-1" flat>Close</v-btn>
            <v-btn color="brown darken-1" flat>Update</v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </v-layout>
</template>

<script>
export default {
  name: 'EditCategory',
  props: {
    dailogStatus: Boolean,
    category: Object
  }
};
</script>

<style scoped>
</style>
