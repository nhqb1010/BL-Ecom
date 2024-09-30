<script setup lang="ts">
import { useMediaQuery } from "@vueuse/core";
import { computed, ref, watch } from "vue";
import { useRoute } from "vue-router";

import { COMPANY } from "@/constants/commons";
import { capitalizeString } from "../../utils";
import NavBasketIcon from "./NavBasketIcon.vue";

interface NavLink {
    name: string;
    href?: string;
    hash?: string;
    label?: string;
    routeType?: "vueRouter" | "section" | "external";
}

const route = useRoute();
const isLargeScreen = useMediaQuery("(min-width: 1024px)");

const navLinks: NavLink[] = [
    { name: "Home", label: "Trang Chủ" },
    { name: "Products", label: "Sản phẩm" },
    { name: "Payments", label: "Thanh Toán" },
    { name: "About", label: "Về Chúng tôi", routeType: "vueRouter" },
];

const isActiveLinkIndex = computed(() => {
    return navLinks.findIndex((link) => {
        if (route.hash) {
            return link.name === route.name && link.hash === route.hash;
        }
        return link.name === route.name;
    });
});

// Mobile Nav
const isOpenMobileNav = ref(false);

const toggleMobileNav = () => {
    isOpenMobileNav.value = !isOpenMobileNav.value;
};

watch(route, () => {
    if (!isLargeScreen.value) {
        isOpenMobileNav.value = false;
    }

    if (route.hash) {
        const el = document.querySelector(route.hash);
        if (el) {
            el.scrollIntoView({ behavior: "smooth" });
        }
    }
});
</script>

<template>
    <nav>
        <!-- Menu Icon -->
        <div class="bx bx-menu" id="menu-icon" @click="toggleMobileNav"></div>

        <!-- Nav Links (Mobile) -->
        <ul
            class="nav-mobile__links"
            :class="{ open: isOpenMobileNav }"
            v-if="!isLargeScreen"
        >
            <li
                v-for="(link, index) in navLinks"
                :key="index"
                class="nav__link"
            >
                <!-- Vue Router Link -->
                <RouterLink
                    :to="{ name: link.name, hash: link.hash }"
                    :class="{ active: index === isActiveLinkIndex }"
                >
                    {{ capitalizeString(link.label || link.name) }}
                </RouterLink>

                <!-- Section/External link -->
                <!-- <a v-else :href="link.href">{{ link.name }}</a> -->
            </li>
        </ul>

        <!-- Basket Icon -->
        <RouterLink :to="{ name: 'Home' }" class="nav__logo">
            <i class="bx bx-basket"></i>{{ COMPANY.name }}
        </RouterLink>

        <!-- Navbar Links (Desktop) -->
        <ul class="nav-desktop__links">
            <li
                v-for="(link, index) in navLinks"
                :key="index"
                class="nav__link"
            >
                <!-- Vue Router Link -->
                <RouterLink
                    :to="{ name: link.name, hash: link.hash }"
                    :class="{ active: index === isActiveLinkIndex }"
                >
                    {{ (link.label || link.name).toUpperCase() }}
                </RouterLink>

                <!-- Section/External link -->
                <!-- <a v-else :href="link.href">{{ link.name }}</a> -->
            </li>
        </ul>

        <!-- Profile -->
        <!-- <div class="nav__profile">
            <img src="../assets/images/profile.jpg" alt="profile-avatar" />

            <div class="detail">
                <span>John Doe</span>
                <i class="bx bx-caret-down"></i>
            </div>
        </div> -->

        <!-- Basket -->
        <div class="nav__basket">
            <p>Giỏ Hàng</p>

            <NavBasketIcon :items="0" />
        </div>
    </nav>
</template>

<style lang="scss" scoped>
nav {
    position: fixed;
    width: 100%;
    height: var(--nav-height);
    top: 0;
    right: 0;
    z-index: 1000;

    display: grid;
    grid-auto-flow: column;
    grid-template-columns: 20% 1fr 20%;
    place-items: center;

    background: var(--bg-color);
    box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
        rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;

    .nav__logo {
        display: flex;
        align-items: center;
        font-size: 1.2rem;
        font-weight: 600;
        font-family: var(--primary-font) !important;
        color: var(--orange-color);
        gap: 0.5rem;

        .bx {
            font-size: 24px;
            color: var(--orange-color);
        }
    }

    .nav__link a {
        font-weight: 500;
        transition: all 0.4s ease;
    }

    .nav-desktop__links {
        display: none;

        .nav__link {
            a {
                font-size: 0.75rem;
                color: var(--text-color);
                padding: 0.5rem 1rem;

                &:hover,
                &.active {
                    background-color: var(--orange-color);
                    color: var(--bg-color);
                    border-radius: 5rem;
                }

                @media (min-width: 1280px) {
                    font-size: 0.85rem;
                    padding: 0.5rem 1.5rem;
                }
            }
        }
    }

    .nav-mobile__links {
        position: fixed;
        top: 0;
        left: 0;

        width: min(300px, 80%);
        padding-top: calc(var(--nav-height) + 1rem);
        min-width: none;
        min-height: 100vh;

        background-color: rgba(247, 95, 29, 0.4);
        backdrop-filter: blur(1rem);

        transform: translateX(-100%);
        transition: transform 0.4s ease-in-out;

        &.open {
            transform: translateX(0);
        }

        .nav__link {
            display: block;
            margin-left: auto;

            display: grid;
            place-items: center;
            margin-block: 1rem;

            a {
                width: 90%;
                font-size: 1.2rem;
                color: #fff;
                padding: 1rem 1.5rem;

                &.active {
                    background-color: var(--green-color);
                    color: var(--bg-color);
                    border-radius: 5rem;
                }
            }
        }
    }

    .nav__profile {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;

        img {
            width: 35px;
            aspect-ratio: 1/1;
            object-fit: cover;
            object-position: center;
            border-radius: 50%;
        }

        .detail {
            display: none;

            span {
                font-size: 13px;
                font-weight: 500;
            }
        }
    }

    .nav__basket {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;

        p {
            font-size: 1rem;
            font-weight: 600;
            color: var(--orange-color);
            display: none;
        }
    }

    #menu-icon {
        display: block;
        font-size: 24px;
        color: var(--text-color);
        cursor: pointer;
        z-index: 1001;
    }

    @media screen and (min-width: 768px) {
        .nav__logo {
            font-size: 1.4rem;

            .bx {
                font-size: 30px;
            }
        }

        .nav__basket p {
            display: initial;
        }
    }

    @media screen and (min-width: 1024px) {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 100px;

        .nav-desktop__links,
        .nav__profile {
            display: flex;
        }

        .nav-desktop__links {
            position: initial;
            width: auto;
            height: auto;
            flex-direction: row;

            gap: 0.5rem;
        }

        .nav__profile {
            img {
                width: 40px;
            }

            .detail {
                display: flex;
            }
        }

        #menu-icon {
            display: none;
        }
    }

    @media screen and (min-width: 1200px) {
        .nav__logo {
            font-size: 1.6rem;

            .bx {
                font-size: 38px;
            }
        }
    }
}
</style>
