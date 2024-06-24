<script setup lang="ts">
import AppBannerSlide from "./AppSlide.vue";
import BlogsSection from "./Blogs.vue";
import IntroductionSection from "./Introduction.vue";
import ProductsSection from "./Products.vue";
</script>

<template>
    <section id="home-section">
        <!-- Banner Slides -->
        <AppBannerSlide />

        <!-- Introduction Section -->
        <IntroductionSection />

        <!-- Products Section -->
        <ProductsSection />

        <!-- Blogs Section -->
        <BlogsSection />
    </section>
</template>

<style scoped>
#home-section {
    overflow-x: hidden;
    padding-top: var(--nav-height);
}
</style>
