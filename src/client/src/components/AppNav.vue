<script setup lang="ts">
interface NavLink {
    name: string;
    href: string;
}

const nav_links: NavLink[] = [
    { name: "Home", href: "#home" },
    { name: "Categories", href: "#categories" },
    { name: "Products", href: "#products" },
    { name: "About", href: "#about" },
    { name: "Customers", href: "#customers" },
];
</script>

<template>
    <nav>
        <!-- Basket Icon -->
        <a href="#" class="nav__logo"><i class="bx bx-basket"></i>Delicacy</a>

        <!-- Menu Icon -->
        <div class="bx bx-menu" id="menu-icon"></div>

        <!-- Navbar Links -->
        <ul class="nav__links">
            <li v-for="link in nav_links" :key="link.name" class="nav__link">
                <a :href="link.href">{{ link.name }}</a>
            </li>
        </ul>

        <!-- Profile -->
        <div class="nav__profile">
            <img src="../assets/images/profile.jpg" alt="profile-avatar" />
            <span>John Doe</span>
            <i class="bx bx-caret-down"></i>
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
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 100px;
    background: var(--bg-color);
    box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
        rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
    transition: all 0.5s ease;

    .nav__logo {
        display: flex;
        align-items: center;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-color);
        gap: 0.5rem;

        .bx {
            font-size: 24px;
            color: var(--orange-color);
        }
    }

    .nav__links {
        display: flex;
        gap: 0.5rem;

        .nav__link {
            a {
                font-size: 1rem;
                font-weight: 500;
                color: var(--text-color);
                padding: 0.5rem 1rem;

                &:hover,
                &.active {
                    background-color: var(--green-color);
                    color: var(--bg-color);
                    border-radius: 5rem;
                    transition: all 0.3s ease;
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
            width: 40px;
            aspect-ratio: 1/1;
            object-fit: cover;
            object-position: center;
            border-radius: 50%;
        }

        span {
            font-size: 13px;
            font-weight: 500;
        }
    }

    #menu-icon {
        display: none;
        font-size: 24px;
        color: var(--text-color);
        cursor: pointer;
        z-index: 1001;
    }
}
</style>
