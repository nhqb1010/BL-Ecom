<script setup lang="ts">
import { onMounted, ref } from "vue";

import { vAutoAnimate } from "@formkit/auto-animate";
import PVButton from "primevue/button";

import type { IProductDetailType } from "@/types/products";

import { filterProductsByCategory, getProducts } from "@/api/products";
import ProductCard from "@/components/ProductCard.vue";

const products = ref<IProductDetailType[]>([]);

onMounted(async () => {
    const data = await getProducts();
    products.value = data;
});

function removeItem(id: string) {
    products.value = products.value.filter((product) => product.id !== id);
}

async function getAllProducts() {
    products.value = await getProducts();
}

async function getOnlyTProducts() {
    products.value = await filterProductsByCategory("Phụ kiện máy tính");
}

async function getOnlySProducts() {
    products.value = await filterProductsByCategory("Tai nghe");
}
</script>

<template>
    <div class="container">
        <div class="products-filter">
            <PVButton label="Tất cả" @click="getAllProducts" />

            <PVButton label="Something Else" @click="getOnlyTProducts" />

            <PVButton label="Something Else 2" @click="getOnlySProducts" />
        </div>

        <br />

        <div class="products-grid products-grid__container" v-auto-animate>
            <ProductCard
                v-for="(product, index) of products"
                :key="product.id || index"
                v-bind="product"
            />
        </div>
    </div>
</template>

<style lang="scss">
.products-filter {
    --button-width: 8em;

    width: 100%;

    display: flex;
    justify-content: center;
    gap: 1rem;

    margin-bottom: 1.5rem;

    & > * {
        width: var(--button-width);
        font-size: 12px !important;
    }

    @media (min-width: 584px) {
        --button-width: 10em;
        font-size: 14px !important;
    }

    @media (min-width: 768px) {
        --button-width: 12em;
    }
}

.products-grid {
    --min-card-width: 150px;

    width: 100%;

    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(var(--min-card-width), 1fr));
    gap: 0.5rem;

    & > * {
        box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
        margin-inline: auto;
        max-width: 260px;
    }

    @media (min-width: 584px) {
        --min-card-width: 200px;
        gap: 1rem;
    }

    @media (min-width: 940px) {
        --min-card-width: 260px;
        gap: 1.2rem;
    }
}
</style>
