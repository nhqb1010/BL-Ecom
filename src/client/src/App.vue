<script setup lang="ts">
import AppFooter from "./components/AppFooter.vue";
import AppNav from "./components/AppNav.vue";
</script>

<template>
    <!-- Nav bar -->
    <AppNav />

    <!-- Page View -->
    <RouterView />

    <!-- Footer -->
    <AppFooter />
</template>
