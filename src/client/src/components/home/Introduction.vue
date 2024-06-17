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
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque
                id, dolorem temporibus explicabo placeat vero veritatis culpa
                quod quidem, hic voluptatum corporis incidunt odio corrupti
                nihil ut saepe quibusdam! Qui, aliquid modi praesentium a odio
                corporis assumenda ipsum ea animi, quibusdam illum, temporibus
                repudiandae dolores enim quas molestias vitae voluptatem
                consequatur optio et nam saepe!
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
    max-width: 1200px;
    margin-inline: auto;

    display: grid;

    &__text {
        padding: 1rem;
        margin-inline: auto;

        * {
            display: block;
            margin-inline: auto;
        }

        h2 {
            text-align: center;
            color: var(--orange-color);
            max-width: 14ch;
            margin-bottom: 2rem;
        }

        p {
            margin-top: 1.2rem;
            line-height: 1.5;
            width: 100%;
            max-width: 35ch;
            object-fit: contain;
        }
    }

    &__brand {
        display: grid;
        place-items: center;

        img {
            width: 85%;
            max-width: 30em;
            padding: 0.5rem;
            aspect-ratio: 1 / 1;
            border-radius: 20px;
        }
    }
}

@media (min-width: 768px) {
    .introduction {
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));

        &__text {
            margin-left: auto;
            margin-right: initial;

            p {
                max-width: 50ch;
            }
        }
    }
}
</style>
