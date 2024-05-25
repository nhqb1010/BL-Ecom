<script setup lang="ts">
import AppBannerSlide from "@/components/home/AppSlide.vue";
</script>

<template>
    <section id="home-section">
        <!-- Banner Slides -->
        <AppBannerSlide />
    </section>
</template>

<style scoped>
#home-section {
    overflow-x: hidden;
    padding-top: var(--nav-height);
}
</style>
