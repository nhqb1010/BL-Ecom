<script setup lang="ts">
import { useImage } from "@vueuse/core";

import type { IBlogCardProps } from "@/types/blogs";

const { imageUrl, title, description } = defineProps<IBlogCardProps>();

const { isReady: isImageLoaded } = useImage({ src: imageUrl });
</script>

<template>
    <div class="blog-card blog-card__container">
        <div class="blog-card__header">
            <!-- Lazy Load the image -->
            <img
                :src="imageUrl"
                alt="Blog"
                class="blog-card-image"
                v-if="isImageLoaded"
            />

            <div class="blog-card-image skeleton" v-else></div>
        </div>

        <div class="blog-card__body">
            <a href="#" class="blog-card__body-title">
                <span>{{ title }}</span>

                <i class="bx bx-right-arrow-alt"></i>
            </a>

            <p class="blog-card__body-description">
                {{ description }}
            </p>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.blog-card {
    --border-radius: 1.5rem;
    --transition-time: 0.2s;

    border-radius: var(--border-radius);
    overflow: hidden;

    transition: transform var(--transition-time) ease-out;

    &__header {
        margin-bottom: 1rem;

        .blog-card-image {
            width: 100%;
            aspect-ratio: 16 / 9;
            border-radius: var(--border-radius);
            object-fit: cover;
        }
    }

    &__body {
        padding: 0.5rem;

        &-title {
            font-size: 1.4rem;
            font-weight: 600;
            line-height: 1.2;
            color: black;
            display: block;
            width: 100%;
            margin-bottom: 1rem;
            transition: color var(--transition-time) ease;

            span {
                display: inline-block;
                width: calc(100% - 30px);
                text-align: left;
            }

            i {
                display: inline-block;
                width: 30px;
                aspect-ratio: 1/1;
                margin-left: auto;
                rotate: -30deg;
                transition: scale var(--transition-time) ease-out,
                    transform var(--transition-time) ease-out;
            }
        }

        &-description {
            line-height: 1.4;
        }
    }

    &:hover,
    &:focus-within {
        // transform: translateY(-10px);
        cursor: pointer;

        .blog-card__body {
            &-title {
                color: var(--orange-color);

                i {
                    transform: translate(8px, 0);
                    scale: 1.3;
                }
            }
        }
    }
}
</style>
