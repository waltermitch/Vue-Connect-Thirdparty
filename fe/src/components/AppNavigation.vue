<template>
  <span>
    <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>
      <v-list>
        <template v-for="(item, index) in items">
          <v-list-tile :key="index">
            <v-list-tile-content>{{item.title}}</v-list-tile-content>
          </v-list-tile>
          <v-divider :key="`divider-${index}`"></v-divider>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app color="brown darken-4 white--text">
      <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-spacer class="hidden-md-and-up"></v-spacer>
      <router-link to="/">
        <v-toolbar-title>{{appTitle}}</v-toolbar-title>
      </router-link>
      <v-btn flat class="hidden-sm-and-down white--text" @click="goTo('home')">Favorite Things</v-btn>
      <v-btn flat class="hidden-sm-and-down white--text" @click="goTo('category')">Category</v-btn>
      <!--<v-btn flat class="hidden-sm-and-down white--text" @click="goTo('audit-log')">Audit Logs</v-btn>-->
    </v-toolbar>
  </span>
</template>
<script>
export default {
  name: 'AppNavigation',
  data() {
    return {
      appTitle: 'Brite Core',
      drawer: false,
      items: [
        { title: 'Favorite Things' },
        { title: 'Category' } /*,
        { title: 'Audit Logs' }*/
      ]
    };
  },
  methods: {
    goTo(routeName) {
      this.$router.push({ name: routeName });
      console.log('me');
    }
  }
};
</script>

<style scoped>
a {
  color: white;
  text-decoration: none;
}
</style>
