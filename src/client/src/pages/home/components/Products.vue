<script setup lang="ts">
import { computed, onMounted } from "vue";

import type { IProductDetailType } from "@/types/products";

import { useProductsStore } from "@/stores/products";

import ProductCard from "@/components/ProductCard.vue";
import { RouterLink } from "vue-router";

const productsStore = useProductsStore();

const featuredProducts = computed<IProductDetailType[]>(
    () => productsStore.featuredProducts
);

onMounted(async () => {
    if (productsStore.featuredProducts.length) return;

    await productsStore.fetchProducts();
});
</script>

<template>
    <section class="container products">
        <!-- Title -->
        <h2 class="products__title">Sản Phẩm</h2>

        <!-- Products -->
        <div class="products__container">
            <div class="products_list">
                <ProductCard
                    v-for="(product, index) of featuredProducts"
                    :key="index"
                    v-bind="product"
                />
            </div>
            <div class="products_more">
                <!-- <a href="#" class="btn-link see-more">
                    Xem thêm <i class="bx bx-right-arrow-alt"></i>
                </a> -->

                <RouterLink to="/products" class="btn-link see-more">
                    Xem thêm <i class="bx bx-right-arrow-alt"></i>
                </RouterLink>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped>
.products {
    margin-block: 3rem;
    max-width: 840px;
    margin-inline: auto;
    padding-inline: 0.5rem;

    display: grid;

    &__title {
        text-align: center;
        color: var(--orange-color);
        margin-inline: auto;
        margin-bottom: 2rem;
    }

    &__container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;

        .products_list {
            width: 100%;

            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.5rem;

            & > * {
                box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
                margin-inline: auto;
            }
        }

        .products_more {
            a {
                display: block;
                width: fit-content;
                white-space: nowrap;
            }
        }
    }
}

@media (min-width: 584px) {
    .products {
        &__container {
            .products_list {
                max-width: 90%;
            }
        }
    }
}

@media (min-width: 768px) {
    .products {
        &__container {
            flex-direction: row;
        }
    }
}
</style>
