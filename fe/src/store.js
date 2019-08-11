import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    favoriteThings: [],
    categories: [],
    apiBaseUrl: `${process.env.VUE_APP_BACKEND_URL}/api/v1`
  },
  mutations: {
    setFavoriteThings: function (state, payload) {
      state.favoriteThings = payload;
    },
    setCategories: function (state, payload) {
      state.categories = payload;
    }
  },
  actions: {
    async getFavoriteThing({
      state,
      commit
    }) {
      try {
        let response = await axios.get(`${state.apiBaseUrl}/thing`);
        commit('setFavoriteThings', response.data.results);
      } catch (error) {
        commit('setFavoriteThings', []);
      }
    },
    async getCategories({
      state,
      commit
    }) {
      try {
        let response = await axios.get(`${state.apiBaseUrl}/category`);
        commit('setCategories', response.data);
      } catch (error) {
        commit('categories', []);
      }
    }
  }
});