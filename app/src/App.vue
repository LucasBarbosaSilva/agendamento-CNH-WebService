<script setup lang="ts">
  import HeaderComponent from './components/HeaderComponent.vue';
  import HomeView from './views/HomeView.vue';
</script>

<template>
  <v-layout>
    <HeaderComponent/>
    <v-main>
      <HomeView/>
    </v-main>
  </v-layout>
</template>
