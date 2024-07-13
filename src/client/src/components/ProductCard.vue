<script setup lang="ts">
import { useImage } from "@vueuse/core";

import type { IProductDetailType } from "@/types/products";

const { imageUrl, name, price, originalPrice } =
    defineProps<IProductDetailType>();

const { isReady: isLoadedImage } = useImage({ src: imageUrl });
</script>

<template>
    <div class="product-detail">
        <div class="product-detail__image">
            <!-- Lazy Load the image -->
            <img
                v-if="isLoadedImage"
                :src="imageUrl"
                alt="Product"
                class="product-detail__image-image"
            />

            <div v-else class="skeleton skeleton__square"></div>
        </div>

        <div class="product-detail__info">
            <h3 class="product-detail__info-name">{{ name }}</h3>

            <p class="product-detail__info-price">
                {{ price }} VND

                <span v-if="originalPrice" class="og-price">
                    {{ originalPrice }}
                </span>
            </p>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.product-detail {
    width: 100%;
    max-width: 260px;
    border-radius: 0.3rem;
    overflow: hidden;
    display: flex;
    flex-flow: column;

    cursor: pointer;

    transition: transform 0.2s ease-out;

    &__image {
        img {
            width: 100%;
            aspect-ratio: 1 / 1;
            object-fit: fit;
        }
    }

    &__info {
        padding: 1rem;
        padding-bottom: 2rem;
        height: auto;
        flex: 1 1 auto;

        display: flex;
        flex-direction: column;
        justify-content: space-between;

        &-name {
            margin-bottom: 1rem;

            font-size: 0.8rem;
            line-height: 1.5;

            transition: color 0.2s ease;

            @media (min-width: 584px) {
                font-size: 1rem;
                max-width: 20ch;
            }
        }

        &-price {
            font-size: 0.8rem;

            .og-price {
                display: none;

                font-size: 0.7rem;
                text-decoration: line-through;
                color: var(--gray-color);
            }

            @media (min-width: 584px) {
                font-size: 1rem;

                .og-price {
                    display: initial;
                }
            }
        }
    }

    &:hover {
        transform: translateY(-0.2rem);

        .product-detail__info {
            &-name {
                color: var(--orange-color);
            }
        }
    }
}
</style>
