<script setup lang="ts">
import AppFooter from "./components/AppFooter.vue";
import AppNav from "./components/NavBar/AppNav.vue";
</script>

<template>
    <!-- Nav bar -->
    <AppNav />

    <!-- Page View -->
    <RouterView />

    <!-- Footer -->
    <AppFooter />
</template>
