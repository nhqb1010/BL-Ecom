<script setup lang="ts">
import AppBannerSlide from "@/components/home/AppSlide.vue";
import Introduction from "@/components/home/Introduction.vue";
import Products from "@/components/home/Products.vue";
</script>

<template>
    <section id="home-section">
        <!-- Banner Slides -->
        <AppBannerSlide />

        <!-- Introduction Section -->
        <Introduction />

        <!-- Products Section -->
        <Products />
    </section>
</template>

<style scoped>
#home-section {
    overflow-x: hidden;
    padding-top: var(--nav-height);
}
</style>
