<template>
  <v-layout row justify-end fill-height xs8 offset-md-2>
    <v-dialog v-model="newFavoriteThingsDialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn flat outline color="brown" dark v-on="on">
          <v-icon>add</v-icon>New Favorite Thing
        </v-btn>
      </template>
      <v-form ref="favoriteThingForm">
        <v-card>
          <v-card-title>
            <div class="headline text-md-center">New Favorite Thing</div>
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
                  <v-select
                    :items="categoryList"
                    item-value="id"
                    item-text="name"
                    label="Category*"
                    v-model="favoriteThing.category"
                    :rules="categoryRules"
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    :rules="titleRules"
                    v-model="favoriteThing.title"
                    label="Title*"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-textarea
                    name="input-7-1"
                    label="Description"
                    persistent-hint
                    v-model="favoriteThing.description"
                    hint="Can be left unfilled, but if filled characters can't be less than 3 and greater than 20."
                  ></v-textarea>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    :rules="rankingRules"
                    v-model="favoriteThing.ranking"
                    type="numeric"
                    label="Ranking*"
                    required
                    mask="####"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-textarea
                    name="input-7-1"
                    label="Meta"
                    persistent-hint
                    v-model="favoriteThing.meta"
                    hint="JSON object representing need fields."
                  ></v-textarea>
                </v-flex>
              </v-layout>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="brown darken-1" flat @click="closeDialog">Close</v-btn>
            <v-btn color="brown darken-1" flat @click="createNewFavoriteThing">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </v-layout>
</template>

<script>
import axios from 'axios';
export default {
  name: 'NewFavoriteThings',
  components: {},
  data() {
    return {
      newFavoriteThingsDialog: false,
      errorVal: '',
      errorStatus: false,
      favoriteThing: {
        category: '',
        title: '',
        description: '',
        ranking: '',
        meta: ''
      },
      categoryRules: [category => !!category || 'Please select a category'],
      titleRules: [title => !!title || 'Please enter a title.'],
      rankingRules: [ranking => !!ranking || 'Please enter the ranking.']
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
    setAll(obj, val) {
      Object.keys(obj).forEach(function(index) {
        obj[index] = val;
      });
    },
    closeDialog() {
      //this.setAll(this.favoriteThing, null);
      console.log(process.env.NODE_ENV);
      this.$refs.favoriteThingForm.reset();
      this.$refs.favoriteThingForm.resetValidation();
      this.newFavoriteThingsDialog = false;
    },
    async createNewFavoriteThing() {
      if (!this.$refs.favoriteThingForm.validate()) {
        return;
      }
      let api_url = `${this.$store.state.apiBaseUrl}/thing/`;
      try {
        let response = await axios.post(api_url, this.favoriteThing);
        let data = {
          message: 'Favorite thing created successfully.',
          status: true
        };
        this.$emit('successfulCreation', data);
        this.$store.dispatch('getFavoriteThing');
        this.closeDialog();
      } catch (error) {
        console.log(`${error}`);
        this.errorVal = error;
        this.errorStatus = true;
      }
    }
  }
};
</script>
<style scoped>
</style>
