<template>
  <v-contianer fluid grid-list-lg>
    <v-layout row wrap align-center>
      <v-flex xs12 class="text-xs-center display-3 my-5">Favorite Things</v-flex>
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
    <v-layout row wrap align-center></v-layout>
    <v-layout row wrap align-center>
      <v-flex xs8 offset-md2>
        <!-- New category & favorite thing pop up-->
        <new-category v-on:successfulCreation="showSuccessMessage"></new-category>
        <new-favorite-things v-on:successfulCreation="showSuccessMessage"></new-favorite-things>
        <!-- End -->
        <!-- View Full Dets -->
        <v-layout row justify-end fill-height xs8 offset-md-2>
          <v-dialog v-model="fullDetsDialog" max-width="600px">
            <v-form ref="favoriteThingForm">
              <v-card>
                <v-card-title>
                  <div class="headline text-sm-center">Favorite Thing Details</div>
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
                          readonly="true"
                          :rules="categoryRules"
                          v-model="favoriteThing.category_name"
                          label="Category"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          readonly="true"
                          :rules="titleRules"
                          v-model="favoriteThing.title"
                          label="Title*"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-textarea
                          readonly="true"
                          name="input-7-1"
                          label="Description"
                          persistent-hint
                          v-model="favoriteThing.description"
                          hint="Can be left unfilled, but if filled characters can't be less than 3 and greater than 20."
                        ></v-textarea>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field
                          readonly="true"
                          :rules="rankingRules"
                          v-model="favoriteThing.ranking"
                          type="number"
                          label="Ranking"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-textarea
                          readonly="true"
                          name="input-7-1"
                          label="Meta"
                          persistent-hint
                          v-model="favoriteThing.meta"
                          hint="JSON object representing need fields."
                        ></v-textarea>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <!--<small>*indicates required field</small>-->
                </v-card-text>
                <v-card-actions>
                  <!--<v-spacer></v-spacer>-->
                  <v-btn color="brown darken-1" block flat @click="closeFullDetsDialog">Close</v-btn>
                  <!--<v-btn color="brown darken-1" flat @click="createNewFavoriteThing">Save</v-btn>-->
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </v-layout>
        <!-- End -->
        <!-- Edit Favorite Things Dets -->
        <v-layout row justify-end fill-height xs8 offset-md-2>
          <v-dialog v-model="editThingDialog" max-width="600px">
            <v-form ref="editFavoriteThingForm">
              <v-card>
                <v-card-title>
                  <div class="headline text-sm-center">Favorite Thing Details</div>
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
                          type="number"
                          label="Ranking"
                          required
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
                  <v-btn color="brown darken-1" flat @click="cancelDialog">Cancel</v-btn>
                  <v-btn color="brown darken-1" flat @click="updateThing">Update</v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
          </v-dialog>
        </v-layout>
        <!-- End -->
        <v-card v-for="(thing, idx) in favoriteItems" :key="idx" class="my-2">
          <v-card-text class="p-0">
            <div>
              <div>
                <span
                  class="caption font-weight-light"
                >#{{thing.ranking}} of {{thing.category_name}}</span>
              </div>
              <v-divider class="my-3"></v-divider>
              <div class="title font-weight-regular">{{thing.title}}</div>
              <span class="body-1">{{thing.description}}</span>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-icon
              color="brown darken-4"
              @click="showEditThingDialog(thing)"
              class="icons mx-3"
            >edit</v-icon>
            <v-icon color="brown darken-4" @click="deleteThing(thing.id)" class="icons mx-3">delete</v-icon>
            <v-spacer></v-spacer>
            <v-btn
              flat
              outline
              color="brown darken-4"
              @click="showFullDetsDialog(thing)"
            >View Full Details</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-contianer>
</template>

<script>
import axios from 'axios';
import NewCategory from '../components/NewCategory';
import NewFavoriteThings from './NewFavoriteThings';
export default {
  name: 'favoriteThings',
  components: {
    NewCategory,
    NewFavoriteThings
  },
  data() {
    return {
      favoriteThings: [],
      sucVal: '',
      sucStatus: false,
      dialog: false,
      fullDetsDialog: false,
      editThingDialog: false,
      favoriteThing: {},
      categoryRules: [category => !!category || 'Please select a category'],
      titleRules: [title => !!title || 'Please enter a title.'],
      rankingRules: [ranking => !!ranking || 'Please enter the ranking.']
    };
  },
  created() {
    this.$store.dispatch('getFavoriteThing');
    this.$store.dispatch('getCategories');
  },
  computed: {
    favoriteItems() {
      return this.$store.state.favoriteThings;
    },
    categoryList() {
      return this.$store.state.categories;
    }
  },
  methods: {
    showFullDetsDialog(thing) {
      this.favoriteThing = thing;
      this.fullDetsDialog = true;
    },
    cancelDialog() {
      this.editThingDialog = false;
    },
    closeFullDetsDialog() {
      this.favoriteThing = {};
      this.fullDetsDialog = false;
    },
    showEditThingDialog(thing) {
      this.favoriteThing = thing;
      this.editThingDialog = true;
    },
    async updateThing() {
      if (!this.$refs.editFavoriteThingForm.validate()) {
        return;
      }
      // perform update
      let api_url = `${this.$store.state.apiBaseUrl}/thing/${
        this.favoriteThing.id
      }/`;

      try {
        let response = await axios.put(api_url, this.favoriteThing);
      } catch (error) {
        console.log(`${error}`);
      }
      this.$store.dispatch('getFavoriteThing');
      this.sucVal = 'Update operation was successful.';
      this.sucStatus = true;
      this.editThingDialog = false;
    },
    async deleteThing(thing_id) {
      if (confirm('Are you sure you want to delete this favorite item?')) {
        let api_url = `${this.$store.state.apiBaseUrl}/thing/${thing_id}`;
        try {
          let response = await axios.delete(api_url);
          this.sucVal = 'Delete operation was successful.';
          this.sucStatus = true;
          this.$store.dispatch('getFavoriteThing');
        } catch (error) {
          console.log(`${error}`);
        }
      } else {
        return;
      }
    },
    editThing(thing_id) {
      console.log(`Edit: ${thing_id}`);
    },
    showSuccessMessage(value) {
      this.sucVal = value.message;
      this.sucStatus = value.status;
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


