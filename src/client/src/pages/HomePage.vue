<script setup lang="ts">
import AppBannerSlide from "@/components/home/AppSlide.vue";
</script>

<template>
    <section id="home-section">
        <!-- Banner Slides -->
        <AppBannerSlide />

        <div class="content" id="categories">Categories</div>
        <div class="content" id="products">Products</div>
        <div class="content" id="customers">Customers</div>
    </section>
</template>

<style scoped>
#home-section {
    overflow-x: hidden;
    padding-top: var(--nav-height);

    .content {
        margin-top: 1rem;
        margin-inline: 1rem;
        min-height: 40vh;
        outline: 2px solid salmon;
    }
}
</style>
