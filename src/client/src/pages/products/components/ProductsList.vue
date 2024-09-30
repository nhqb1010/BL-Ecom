<script setup lang="ts">
import { onMounted, ref } from "vue";

import { vAutoAnimate } from "@formkit/auto-animate";
import PVButton from "primevue/button";

import type { IProductDetailType } from "@/types/products";

import {
    filterProductsByCategory,
    getProducts,
    sortProductsByPrice,
} from "@/api/products";
import ProductCard from "@/components/ProductCard.vue";

const products = ref<IProductDetailType[]>([]);
const orderDir = ref<"asc" | "desc" | null>(null);

onMounted(async () => {
    const data = await getProducts();
    products.value = data;
});

async function getAllProducts() {
    products.value = await getProducts();
}

async function getOnlyTProducts() {
    products.value = await filterProductsByCategory("bag");
}

async function sortProducts() {
    if (!orderDir.value) {
        orderDir.value = "asc";
    } else {
        orderDir.value = orderDir.value === "asc" ? "desc" : "asc";
    }

    const data = await sortProductsByPrice(products.value, orderDir.value);
    products.value = [...data];
}
</script>

<template>
    <div class="container">
        <div class="products-filter">
            <PVButton label="Tất cả" @click="getAllProducts" />

            <PVButton label="Túi" @click="getOnlyTProducts" />

            <PVButton label="Sắp Xếp" @click="sortProducts" />
        </div>

        <br />

        <div class="products-grid products-grid__container" v-auto-animate>
            <ProductCard
                v-for="(product, index) of products"
                :key="product.id"
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
    --min-card-width: 170px;

    width: 100%;
    padding-inline: 0.1rem;

    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(var(--min-card-width), 1fr));
    gap: 1rem;

    & > * {
        box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
        margin-inline: auto;
        max-width: 260px;
    }

    @media (min-width: 584px) {
        padding: initial;
        gap: 1rem;
        --min-card-width: 200px;
    }

    @media (min-width: 940px) {
        --min-card-width: 240px;
        gap: 1.2rem;
        grid-template-columns: repeat(4, minmax(var(--min-card-width), 1fr));
    }
}
</style>
