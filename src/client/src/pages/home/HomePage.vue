<script setup lang="ts">
import AppBannerSlide from "./components/AppSlide.vue";
import BlogsSection from "./components/Blogs.vue";
import IntroductionSection from "./components/Introduction.vue";
import JoinUs from "./components/JoinUs.vue";
import ProductsSection from "./components/Products.vue";
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

        <!-- Join Us Section -->
        <JoinUs />
    </section>
</template>

<style scoped>
#home-section {
    overflow-x: hidden;
    padding-top: var(--nav-height);
}
</style>
