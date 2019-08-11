<template>
  <span>
    <favorite-things></favorite-things>
  </span>
</template>

<script>
import FavoriteThings from '@/components/FavoriteThings';
export default {
  name: 'Home',
  components: {
    FavoriteThings
  },
  created() {
    console.log(this.$store.state.apiBaseUrl);
    console.log(process.env);
  }
};
</script>
