<script setup lang="ts">
import AppBannerSlide from "@/components/home/AppSlide.vue";
import Introduction from "@/components/home/Introduction.vue";
</script>

<template>
    <section id="home-section">
        <!-- Banner Slides -->
        <AppBannerSlide />

        <Introduction />
    </section>
</template>

<style scoped>
#home-section {
    overflow-x: hidden;
    padding-top: var(--nav-height);
}
</style>
