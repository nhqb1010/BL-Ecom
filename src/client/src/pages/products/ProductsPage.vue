<script setup lang="ts">
import ProductsLists from "./components/ProductsList.vue";
</script>

<template>
    <section class="products products__container">
        <!-- Title -->
        <h2 class="products__title">Sản Phẩm</h2>

        <!-- Products Lists -->
        <ProductsLists />
    </section>
</template>

<style lang="scss" scoped>
.products {
    margin-top: 5rem;
    max-width: 1200px;

    &__title {
        font-size: 2.5rem;
        line-height: 1.5;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        color: var(--orange-color);
    }

    @media (min-width: 768px) {
        margin-inline: auto;
        width: 90% !important;
    }
}
</style>
