<script setup lang="ts"></script>

<template>
    <section class="container introduction">
        <!-- Text -->
        <div class="introduction__text">
            <h2 class="introduction__title">
                Câu Chuyện Về
                <span>PMBL-shee</span>
            </h2>

            <p class="introduction__description">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
                eget felis eget nunc ultrices ultricies. Donec nec nunc nec nunc
                ultrices ultricies. Donec nec nunc nec nunc ultrices ultricies.
            </p>

            <p class="introduction__description">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
                eget felis eget nunc ultrices ultricies. Donec nec nunc nec nunc
                ultrices ultricies. Donec nec nunc nec nunc ultrices ultricies.
            </p>
        </div>

        <!-- Brand Image -->
        <div class="introduction__brand">
            <img
                src="../../assets/images/dummy-brand.jpg"
                alt="Brand"
                class="introduction__brand-image"
            />
        </div>
    </section>
</template>

<style lang="scss" scoped>
.introduction {
    margin-top: 1rem;
    max-width: 1000px;
    margin-inline: auto;

    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    border: 1px solid red;

    &__text {
        padding: 1rem;

        * {
            display: block;
            margin-inline: auto;
        }

        h2 {
            text-align: center;
            color: var(--orange-color);
            max-width: 14ch;
        }

        p {
            margin-top: 1.2rem;
            text-align: justify;
            width: 100%;
            max-width: 40ch;
            object-fit: contain;
        }
    }

    &__brand {
        display: grid;
        place-items: center;
        img {
            width: 70%;
            max-width: 30em;
            padding: 0.5rem;
            aspect-ratio: 1 / 1;
        }
    }
}

.dummy-image {
    max-width: 100%;
    aspect-ratio: 1 / 3;
    border: 1px solid blue;
}
</style>
