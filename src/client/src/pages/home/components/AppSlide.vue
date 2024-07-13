<script setup lang="ts">
import { COMPANY } from "@/constants/commons";
import { useScriptTag } from "@vueuse/core";

const swiperScriptLink = `https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js`;

// Load 'swiper' script
useScriptTag(
    swiperScriptLink,
    // On loaded 'swiper' script
    () => {
        // Initialize Swiper
        // @ts-ignore
        const swiper = new Swiper(".swiper__container", {
            spaceBetween: 30,
            centeredSlides: true,
            autoplay: {
                delay: 10000,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
        });
    }
);
</script>

<template>
    <div class="swiper__container swiper">
        <!-- Swiper -->
        <div class="swiper-wrapper">
            <!-- Home Banner -->
            <div class="swiper-slide swiper__slide">
                <div class="swiper__text">
                    <span>We are {{ COMPANY.name }}</span>
                    <h1>
                        Choose {{ COMPANY.name }} <br />
                        the best healthy <br />
                        chicken salad
                    </h1>

                    <a href="#" class="btn">
                        Shop Now<i class="bx bx-right-arrow-alt"></i>
                    </a>
                </div>

                <img
                    src="../../../assets/images/banners/banner2.png"
                    alt="home banner"
                />
            </div>

            <!-- Other Banner -->
            <div class="swiper-slide swiper__slide">
                <div class="swiper__text">
                    <span
                        >Lorem ipsum dolor sit amet consectetur adipisicing
                        elit. Facilis, inventore.</span
                    >
                    <h1>
                        Choose delicacy <br />
                        the best healthy <br />
                        chicken salad
                    </h1>

                    <a href="#" class="btn">
                        Shop Now<i class="bx bx-right-arrow-alt"></i>
                    </a>
                </div>

                <img
                    src="../../../assets/images/banners/banner1.jpg"
                    alt="home salad"
                />
            </div>
        </div>

        <!-- Swiper Buttons -->
        <div class="swiper-button-next">
            <i class="bx bxs-chevron-right"></i>
        </div>
        <div class="swiper-button-prev">
            <i class="bx bxs-chevron-left"></i>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.swiper__container {
    width: 100vw;
    max-width: 1920px;

    .swiper-wrapper {
        width: 100%;

        .swiper__slide {
            width: 100%;
            height: 100%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;

            .swiper__text {
                display: none;
            }

            img {
                width: 100%;
                margin-inline: auto;
                object-fit: cover;
            }

            // display grid, divided to 2 columns 60/40
            // display: grid;
            // grid-template-columns: 40% 60%;
            // gap: 1rem;

            // & > * {
            //     margin-block: auto;
            // }

            // .swiper__text {
            //     margin-left: auto;

            //     & > * {
            //         text-align: right;
            //     }
            // }

            // img {
            //     object-fit: cover;
            //     width: 100%;
            //     max-height: 100%;
            //     margin-block: auto;
            // }
        }
    }

    .swiper-button-next,
    .swiper-button-prev {
        i {
            font-size: 2rem;
            color: black;
            transition: ease 0.25s scale;
        }

        &::after {
            display: none;
        }

        &:hover {
            i {
                scale: 1.3;
            }
        }
    }
}

@media only screen and (min-width: 700px) {
    .swiper__container {
        .swiper__slide {
            img {
                // width: 95vw !important;
                max-height: 65vh;
            }
        }
    }
}
</style>
