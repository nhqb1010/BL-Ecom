<script setup lang="ts"></script>

<template>
    <div class="container home-blogs">
        <h2 class="home-blogs__title">Bài Viết</h2>

        <div class="home-blogs__container">
            <div class="home-blogs_list">
                <!-- <BlogCard />
                <BlogCard />
                <BlogCard /> -->
            </div>
            <div class="home-blogs_more">
                <a href="#" class="">
                    Xem thêm <i class="bx bx-right-arrow-alt"></i>
                </a>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.home-blogs {
    margin-block: 2.2rem;
    max-width: 1200px;

    &__title {
        text-align: center;
        color: var(--orange-color);
        margin-inline: auto;
        margin-bottom: 2rem;
    }
}
</style>
